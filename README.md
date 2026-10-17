<div align="center">

# ☁️🔍 Cloud Leak Scanner

### 🛡️ AWS S3 Anonymous Access Checker

**A Python + Boto3 cloud-security learning project**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![AWS S3](https://img.shields.io/badge/AWS-S3-FF9900?style=for-the-badge&logo=amazons3&logoColor=white)](https://aws.amazon.com/s3/)
[![Boto3](https://img.shields.io/badge/SDK-Boto3-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
[![Security](https://img.shields.io/badge/Focus-Cloud%20Security-16A34A?style=for-the-badge&logo=shieldsdotio&logoColor=white)](#-security-first)

*Check whether anonymous users can list objects in specified S3 buckets.*

</div>

---

## 🌟 Project at a Glance

| 🔎 Capability | 📝 Description |
|---|---|
| ☁️ S3 access check | Tests anonymous `ListObjectsV2` access |
| 🐍 Python | Uses Python 3 and Boto3 |
| 📋 Clear output | Reports common AWS responses |
| 🧪 Learning lab | Helps explore cloud-storage permissions |

> [!IMPORTANT]
> **Authorized testing only:** Check buckets you own or have explicit permission to assess. This tool does not discover every public bucket on AWS.

## 🧰 Tech Stack

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <img alt="Boto3" src="https://img.shields.io/badge/Boto3-232F3E?style=flat-square&logo=amazonaws&logoColor=white">
  <img alt="Amazon S3" src="https://img.shields.io/badge/Amazon_S3-FF9900?style=flat-square&logo=amazons3&logoColor=white">
  <img alt="PowerShell" src="https://img.shields.io/badge/PowerShell-5391FE?style=flat-square&logo=powershell&logoColor=white">
</p>

## 📁 Project Structure

```text
Cloud-Leak-Scanner/
├── leak_scanner.py       # 🔍 S3 anonymous-listing check
├── requirements.txt      # 📦 Python dependency
└── README.md             # 📘 Project documentation
```

## 🚀 Quick Start

### 1️⃣ Open PowerShell in your project folder

```powershell
cd "$HOME\Desktop\Projects\S3 Bucket Leak Scanner"
```

Adjust the path if your project is stored elsewhere.

### 2️⃣ Install dependencies

```powershell
python -m pip install -r requirements.txt
```

If you do not have a `requirements.txt` yet, create one containing:

```text
boto3
```

Or install Boto3 directly:

```powershell
python -m pip install boto3
```

### 3️⃣ Run with a bucket name

⚠️ **A bucket name is required.** Running `python leak_scanner.py` by itself shows an argument error.

```powershell
python leak_scanner.py YOUR_TEST_BUCKET
```

Replace `YOUR_TEST_BUCKET` with the name of an S3 bucket you own or are authorized to test.

**Example with a placeholder name:**

```powershell
python leak_scanner.py hemesh-security-lab-demo
```

This example bucket name is illustrative and may not exist.

### 4️⃣ Check multiple authorized buckets

```powershell
python leak_scanner.py TEST_BUCKET_ONE TEST_BUCKET_TWO
```

Replace both placeholders with actual bucket names you are permitted to assess.

## 🖥️ Example Terminal Output

The output below is illustrative. Your results depend on the real bucket and AWS response.

```text
Cloud Storage Access Check
----------------------------------------

[*] Checking bucket: YOUR_TEST_BUCKET
[OK] Anonymous listing denied.

[+] Check complete.
Note: this checks anonymous listing access only.
```

### 🧭 How to interpret results

| Output | Meaning |
|---|---|
| 🟢 `Anonymous object listing is permitted` | The anonymous listing request succeeded |
| 🔒 `Anonymous listing denied` | AWS denied anonymous listing |
| ⚪ `Bucket not found` | AWS returned a not-found response |
| 🟡 `Other error` | Review the AWS error code and HTTP status |

A successful listing does **not** prove every object is publicly readable. A denied listing does **not** prove every object is private.

## 🧯 Troubleshooting

<details>
<summary>🔴 <code>ModuleNotFoundError: No module named 'boto3'</code></summary>

Install Boto3 into the Python environment used to run the script:

```powershell
python -m pip install boto3
```

Verify the installation:

```powershell
python -c "import boto3; print(boto3.__version__)"
```
</details>

<details>
<summary>🟠 <code>the following arguments are required: buckets</code></summary>

You ran the script without a bucket name. Supply an authorized test bucket:

```powershell
python leak_scanner.py YOUR_TEST_BUCKET
```
</details>

<details>
<summary>🟡 Access denied</summary>

This may be the expected result: anonymous object listing is denied. Check that the bucket name is correct and interpret the response as a listing-permission result, not a full security audit.
</details>

## 🛡️ Security First

- ✅ Only test buckets you own or have explicit permission to assess.
- 🔐 Do not store AWS access keys in this repository.
- 🧱 Review S3 Block Public Access, bucket policies, access-point policies, and relevant IAM controls for a fuller assessment.
- 🧩 This script checks anonymous **object listing only**. It does not test every object or every access path.

## 🎓 Learning Outcomes

- Understand anonymous access in Amazon S3.
- Learn how to call AWS APIs with Boto3.
- Interpret common access-control responses.
- Practice documenting cloud-security checks responsibly.

---

<div align="center">

### 💙 Built for learning cloud security

**Python 🐍 · Boto3 📦 · Amazon S3 ☁️**

</div>
