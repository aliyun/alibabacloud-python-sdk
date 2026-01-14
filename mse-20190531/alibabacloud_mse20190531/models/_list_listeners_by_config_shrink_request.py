# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListListenersByConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        data_id: str = None,
        ext_gray_rules_shrink: str = None,
        group: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        request_pars: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the data.
        # 
        # This parameter is required.
        self.data_id = data_id
        self.ext_gray_rules_shrink = ext_gray_rules_shrink
        # The name of the group.
        # 
        # This parameter is required.
        self.group = group
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The extended request parameters in the JSON format.
        self.request_pars = request_pars

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.data_id is not None:
            result['DataId'] = self.data_id

        if self.ext_gray_rules_shrink is not None:
            result['ExtGrayRules'] = self.ext_gray_rules_shrink

        if self.group is not None:
            result['Group'] = self.group

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('DataId') is not None:
            self.data_id = m.get('DataId')

        if m.get('ExtGrayRules') is not None:
            self.ext_gray_rules_shrink = m.get('ExtGrayRules')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        return self

