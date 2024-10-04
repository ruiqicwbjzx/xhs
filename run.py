import hashlib

def md5_hash(text):
    # 计算 MD5 哈希值
    return hashlib.md5(text.encode('utf-8')).hexdigest()

def generate_activation_code(hardware_id):
    # 第一次 MD5 加密
    encrypted_hardware_id = md5_hash(hardware_id)

    # 按 "-" 分割硬件 ID
    hardware_parts = hardware_id.split('-')

    if len(hardware_parts) < 3:
        raise ValueError("硬件 ID 格式不正确")

    # 提取第二段和第三段
    second_part = hardware_parts[1]
    third_part = hardware_parts[2]

    # 组合字符串
    combined_string = f"{encrypted_hardware_id}-{third_part}-xhs-{second_part}"

    # 第二次 MD5 加密
    final_activation_code = md5_hash(combined_string)

    return final_activation_code

# 示例使用
if __name__ == "__main__":
    # 输入你要计算的机器码
    hardware_id = "000000-DEB2XD-D39SD4-DEB2XDGQ"  # 请根据需要替换
    activation_code = generate_activation_code(hardware_id)
    print(f"根据机器码 {hardware_id} 生成的激活码是: {activation_code}")
