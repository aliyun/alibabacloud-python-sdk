# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRandomPasswordRequest(DaraModel):
    def __init__(
        self,
        exclude_characters: str = None,
        exclude_lowercase: str = None,
        exclude_numbers: str = None,
        exclude_punctuation: str = None,
        exclude_uppercase: str = None,
        password_length: str = None,
        require_each_included_type: str = None,
    ):
        # The characters that are not included in the password to be generated.
        # 
        # Valid values:
        # 
        # `Valid characters: 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ! \\"#$%&\\"()*+,-. /:;<=>? @[\\] your_project_id} ~ `.
        # 
        # This parameter is empty by default.
        self.exclude_characters = exclude_characters
        # Specifies whether to exclude lowercase letters.
        # 
        # Valid values:
        # 
        # - true
        # 
        # - false
        self.exclude_lowercase = exclude_lowercase
        # Specifies whether to exclude digits.
        # 
        # Valid values:
        # 
        # - true
        # 
        # - false
        self.exclude_numbers = exclude_numbers
        # Specifies whether to exclude special characters.
        # 
        # Valid values:
        # 
        # - true
        # 
        # - false
        self.exclude_punctuation = exclude_punctuation
        # Specifies whether to exclude uppercase letters.
        # 
        # Valid values:
        # 
        # - true
        # 
        # - false
        self.exclude_uppercase = exclude_uppercase
        # The number of bytes that the password to be generated contains.
        # 
        # Valid values: 8 to 128.
        # 
        # Default value: 32
        self.password_length = password_length
        # Specifies whether to include all the preceding character types.
        # 
        # Valid values:
        # 
        # - true
        # 
        # - false
        self.require_each_included_type = require_each_included_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_characters is not None:
            result['ExcludeCharacters'] = self.exclude_characters

        if self.exclude_lowercase is not None:
            result['ExcludeLowercase'] = self.exclude_lowercase

        if self.exclude_numbers is not None:
            result['ExcludeNumbers'] = self.exclude_numbers

        if self.exclude_punctuation is not None:
            result['ExcludePunctuation'] = self.exclude_punctuation

        if self.exclude_uppercase is not None:
            result['ExcludeUppercase'] = self.exclude_uppercase

        if self.password_length is not None:
            result['PasswordLength'] = self.password_length

        if self.require_each_included_type is not None:
            result['RequireEachIncludedType'] = self.require_each_included_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeCharacters') is not None:
            self.exclude_characters = m.get('ExcludeCharacters')

        if m.get('ExcludeLowercase') is not None:
            self.exclude_lowercase = m.get('ExcludeLowercase')

        if m.get('ExcludeNumbers') is not None:
            self.exclude_numbers = m.get('ExcludeNumbers')

        if m.get('ExcludePunctuation') is not None:
            self.exclude_punctuation = m.get('ExcludePunctuation')

        if m.get('ExcludeUppercase') is not None:
            self.exclude_uppercase = m.get('ExcludeUppercase')

        if m.get('PasswordLength') is not None:
            self.password_length = m.get('PasswordLength')

        if m.get('RequireEachIncludedType') is not None:
            self.require_each_included_type = m.get('RequireEachIncludedType')

        return self

