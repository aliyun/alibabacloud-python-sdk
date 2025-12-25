# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from darabonba.model import DaraModel

class AddDesensitizationRuleRequest(DaraModel):
    def __init__(
        self,
        function_params: List[Dict[str, str]] = None,
        function_type: str = None,
        rule_description: str = None,
        rule_name: str = None,
        rule_type: str = None,
        tid: int = None,
    ):
        # The parameters of the algorithm.
        self.function_params = function_params
        # The type of the masking algorithm.
        # 
        # Valid values:
        # 
        # *   FIX_POS : masks characters in the specified position.
        # *   DATE_ROUNDING: rounds the date.
        # *   PLAINTEXT: does not mask data.
        # *   SHA1: masks characters by using the secure hash algorithm 1 (SHA-1)
        # *   HMAC: masks characters by using the hash-based message authentication code (HMAC).
        # *   STRING_TRANSFORM: shift characters.
        # *   NUMBER_ROUNDING: rounds numbers.
        # *   AES: masks characters by using the advanced encryption standard (AES) algorithm.
        # *   SHA256: masks characters by using SHA-256 algorithm.
        # *   DES: masks characters by using the data encryption standard (DES) algorithm.
        # *   MAP_REPLACE: masks the mapped data.
        # *   FIX_CHAR: masks fixed characters.
        # *   DEFAULT: masks all characters.
        # *   RANDOM_REPLACE: randomly replaces characters.
        # *   MD5: masks characters by using the MD5 algorithm.
        # 
        # This parameter is required.
        self.function_type = function_type
        # The description of the rule.
        self.rule_description = rule_description
        # The name of the rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The masking algorithm.
        # 
        # Valid values:
        # 
        # *   PLAINTEXT
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   TRANSFORM
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   ENCRYPT
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   REPLACE
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   HASH
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   MASK
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # This parameter is required.
        self.rule_type = rule_type
        # The tenant ID.
        # 
        # >  To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see the [View information about the current tenant](https://help.aliyun.com/document_detail/181330.html) section of the "Manage DMS tenants" topic.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function_params is not None:
            result['FunctionParams'] = self.function_params

        if self.function_type is not None:
            result['FunctionType'] = self.function_type

        if self.rule_description is not None:
            result['RuleDescription'] = self.rule_description

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FunctionParams') is not None:
            self.function_params = m.get('FunctionParams')

        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')

        if m.get('RuleDescription') is not None:
            self.rule_description = m.get('RuleDescription')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

