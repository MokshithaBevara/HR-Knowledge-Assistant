import re


def split_text(text, chunk_size=800, overlap=150):

    sections = re.split(r"(?m)(?=^#{1,3}\s)", text)

    chunks = []

    for section in sections:
        section = section.strip()

        if len(section) < 100:
            continue

        # Extract section heading
        heading_match = re.match(r"^#{1,3}\s+(.+)", section)

        heading = heading_match.group(1).strip() if heading_match else "General"

        if len(section) <= chunk_size:
            chunks.append({
                "content": section,
                "section": heading
            })

        else:
            start = 0

            while start < len(section):
                end = start + chunk_size
                chunk = section[start:end].strip()

                if chunk:
                    chunks.append({
                        "content": chunk,
                        "section": heading
                    })

                start += chunk_size - overlap

    return chunks