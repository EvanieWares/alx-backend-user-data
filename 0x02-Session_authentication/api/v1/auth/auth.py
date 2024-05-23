#!/usr/bin/env python3
"""
Auth class
"""

from tabnanny import check
from flask import request
from typing import TypeVar, List
from os import getenv
User = TypeVar('User')


class Auth:
    """
    a class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        returns False - path and excluded_paths
        """
        if not path or not excluded_paths:
            return True
        check = path.rstrip("/")
        for excluded_path in excluded_paths:
            if excluded_path.endswith("*") and \
                  check.startswith(excluded_path[:-1]):
                return False
            elif check == excluded_path.rstrip("/"):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        returns None - request
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> User:
        """
        returns None - request
        """
        return None

    def session_cookie(self, request=None):
        """
        returns a cookie value from a request
        """
        if request:
            session_name = getenv("SESSION_NAME")
            return request.cookie.get(session_name, None)
