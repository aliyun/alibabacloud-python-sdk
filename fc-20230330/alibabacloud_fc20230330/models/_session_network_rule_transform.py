# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_fc20230330 import models as main_models
from darabonba.model import DaraModel

class SessionNetworkRuleTransform(DaraModel):
    def __init__(
        self,
        header_value_replacements: List[main_models.SessionNetworkHeaderValueReplacement] = None,
        headers: Dict[str, str] = None,
    ):
        # The list of rules for replacing placeholders in HTTP header values before the request is forwarded to the matched host.
        self.header_value_replacements = header_value_replacements
        # The HTTP headers injected or overwritten before the request is forwarded to the matched host. Header values are returned in plaintext in GetSession and ListSessions.
        self.headers = headers

    def validate(self):
        if self.header_value_replacements:
            for v1 in self.header_value_replacements:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['headerValueReplacements'] = []
        if self.header_value_replacements is not None:
            for k1 in self.header_value_replacements:
                result['headerValueReplacements'].append(k1.to_map() if k1 else None)

        if self.headers is not None:
            result['headers'] = self.headers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.header_value_replacements = []
        if m.get('headerValueReplacements') is not None:
            for k1 in m.get('headerValueReplacements'):
                temp_model = main_models.SessionNetworkHeaderValueReplacement()
                self.header_value_replacements.append(temp_model.from_map(k1))

        if m.get('headers') is not None:
            self.headers = m.get('headers')

        return self

