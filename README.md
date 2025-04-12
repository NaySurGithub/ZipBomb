# 🔥 Zip Bomb Generator (Educational Purposes ONLY)

A Python script demonstrating recursive archive compression that can generate extremely large outputs from small inputs.

## 🚨 CRITICAL WARNING 
**THIS TOOL CAN:**
- Crash systems by exhausting storage
- Trigger antivirus protections
- Cause denial of service conditions

**INTENDED USE CASES:**
- Security research
- System hardening tests
- Educational demonstrations

## 🛠️ Technical Implementation

```python
# Core compression function
def generate_zip_bomb(final_name="bomb.zip", layers=5, 
                     files_per_layer=10, payload_size_gb=100):
    """Recursively nests compressed archives"""
    # Implementation details...
```

## 📊 Exponential Growth Matrix

| Layers | Files/Layer | Output Size | Decompressed Size |
|--------|-------------|-------------|--------------------|
| 3      | 10          | ~1MB        | ~1TB               |
| 5      | 10          | ~10MB       | ~100PB             |
| 7      | 10          | ~100MB      | ~1EB               |

## 🧰 Usage Instructions

1. Clone repository
2. Run with Python 3.6+:
   ```bash
   python zip_bomb.py --layers 3 --files 5 --size 50
   ```
3. Output will be generated in `/tmp` directory

## 🔒 Security Considerations

✔ Always test in isolated environments  
✔ Requires explicit user confirmation  
✔ Automatic temp directory cleanup  
✔ Size limit safeguards (configurable)

## 📜 License & Ethics

MIT Licensed - By using this software you agree:
- Not to use for malicious purposes
- To obtain proper authorization before testing
- To assume all liability for usage
