import os
import sys

from jose import jwt

ALGORITHM = "HS256"


def main():

    secret = os.getenv("JWT_SECRET")

    if not secret:

        print("JWT_SECRET is not set.")

        sys.exit(1)

    role = sys.argv[1] if len(sys.argv) > 1 else "clinical_ops"

    token = jwt.encode(
        {
            "sub": "demo-user-1",
            "role": role,
        },
        secret,
        algorithm=ALGORITHM,
    )

    print(token)


if __name__ == "__main__":
    main()
