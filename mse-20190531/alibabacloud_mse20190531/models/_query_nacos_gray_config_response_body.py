# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class QueryNacosGrayConfigResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QueryNacosGrayConfigResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.QueryNacosGrayConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryNacosGrayConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        content: str = None,
        data_id: str = None,
        gray_rule: str = None,
        gray_rule_name: str = None,
        gray_rule_priority: str = None,
        gray_type: str = None,
        group: str = None,
        last_modified: str = None,
        md_5: str = None,
    ):
        self.app_name = app_name
        self.content = content
        self.data_id = data_id
        self.gray_rule = gray_rule
        self.gray_rule_name = gray_rule_name
        self.gray_rule_priority = gray_rule_priority
        self.gray_type = gray_type
        self.group = group
        self.last_modified = last_modified
        self.md_5 = md_5

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.content is not None:
            result['Content'] = self.content

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.gray_rule is not None:
            result['GrayRule'] = self.gray_rule

        if self.gray_rule_name is not None:
            result['GrayRuleName'] = self.gray_rule_name

        if self.gray_rule_priority is not None:
            result['GrayRulePriority'] = self.gray_rule_priority

        if self.gray_type is not None:
            result['GrayType'] = self.gray_type

        if self.group is not None:
            result['Group'] = self.group

        if self.last_modified is not None:
            result['LastModified'] = self.last_modified

        if self.md_5 is not None:
            result['Md5'] = self.md_5

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('GrayRule') is not None:
            self.gray_rule = m.get('GrayRule')

        if m.get('GrayRuleName') is not None:
            self.gray_rule_name = m.get('GrayRuleName')

        if m.get('GrayRulePriority') is not None:
            self.gray_rule_priority = m.get('GrayRulePriority')

        if m.get('GrayType') is not None:
            self.gray_type = m.get('GrayType')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('LastModified') is not None:
            self.last_modified = m.get('LastModified')

        if m.get('Md5') is not None:
            self.md_5 = m.get('Md5')

        return self

