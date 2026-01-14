# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListListenersByIpRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
        ip: str = None,
        namespace_id: str = None,
        request_pars: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The IP address of the listener.
        # 
        # This parameter is required.
        self.ip = ip
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        return self

