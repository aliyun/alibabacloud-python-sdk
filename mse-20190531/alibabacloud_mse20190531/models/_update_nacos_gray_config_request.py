# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateNacosGrayConfigRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        app_name: str = None,
        content: str = None,
        data_id: str = None,
        gray_rule: str = None,
        gray_rule_name: str = None,
        gray_rule_priority: int = None,
        gray_type: str = None,
        group: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        op_type: str = None,
        region_id: str = None,
        request_pars: str = None,
        stop_gray: bool = None,
    ):
        self.accept_language = accept_language
        self.app_name = app_name
        self.content = content
        # This parameter is required.
        self.data_id = data_id
        self.gray_rule = gray_rule
        self.gray_rule_name = gray_rule_name
        self.gray_rule_priority = gray_rule_priority
        # This parameter is required.
        self.gray_type = gray_type
        self.group = group
        # This parameter is required.
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.op_type = op_type
        self.region_id = region_id
        self.request_pars = request_pars
        self.stop_gray = stop_gray

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.op_type is not None:
            result['OpType'] = self.op_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        if self.stop_gray is not None:
            result['StopGray'] = self.stop_gray

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

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

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('OpType') is not None:
            self.op_type = m.get('OpType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        if m.get('StopGray') is not None:
            self.stop_gray = m.get('StopGray')

        return self

