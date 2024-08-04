from typing import Any

# Имитация базы данных
DB: dict[str, list[dict[str, Any]]] = {}

# DB = {
#     "valid-token": [
#         {
#             "type": "date",
#             "context": {},
#         },
#     ]
# }

# EXAMPLE
# {
#     "url-token": [
#         {
#             "type": "date",
#             "url": "http://example.com"
#             "context": {
#                 "start": "2000-01-01",
#             },
#         },
#     ]
# }
