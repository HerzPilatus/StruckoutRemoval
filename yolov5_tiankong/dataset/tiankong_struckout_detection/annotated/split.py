import os
import random
import shutil

def split_dataset(images_folder, labels_folder, out_images_folder, out_labels_folder):
    # 创建输出文件夹的train、val和test子文件夹
    images_train_folder = os.path.join(out_images_folder, 'train')
    images_val_folder = os.path.join(out_images_folder, 'val')
    images_test_folder = os.path.join(out_images_folder, 'test')
    os.makedirs(images_train_folder, exist_ok=True)
    os.makedirs(images_val_folder, exist_ok=True)
    os.makedirs(images_test_folder, exist_ok=True)

    labels_train_folder = os.path.join(out_labels_folder, 'train')
    labels_val_folder = os.path.join(out_labels_folder, 'val')
    labels_test_folder = os.path.join(out_labels_folder, 'test')
    os.makedirs(labels_train_folder, exist_ok=True)
    os.makedirs(labels_val_folder, exist_ok=True)
    os.makedirs(labels_test_folder, exist_ok=True)

    # 获取所有图片文件的路径列表
    image_files = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]

    # 打乱图片文件的顺序
    random.shuffle(image_files)

    # 计算划分的索引位置
    num_images = len(image_files)
    train_split = int(0.6 * num_images)
    val_split = int(0.8 * num_images)

    # 将图片和对应的标注文件复制到相应的文件夹中
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(images_folder, image_file)
        label_file = image_file[:-4] + '.txt'
        label_path = os.path.join(labels_folder, label_file)

        if i < train_split:
            shutil.copy(image_path, images_train_folder)
            if os.path.exists(label_path):
                shutil.copy(label_path, labels_train_folder)
            else:
                open(os.path.join(labels_train_folder, label_file), 'w').close()
        elif i < val_split:
            shutil.copy(image_path, images_val_folder)
            if os.path.exists(label_path):
                shutil.copy(label_path, labels_val_folder)
            else:
                open(os.path.join(labels_val_folder, label_file), 'w').close()
        else:
            shutil.copy(image_path, images_test_folder)
            if os.path.exists(label_path):
                shutil.copy(label_path, labels_test_folder)
            else:
                open(os.path.join(labels_test_folder, label_file), 'w').close()

# 使用示例：
split_dataset('./images_all/', './labels_all/', './images/', './labels/')
