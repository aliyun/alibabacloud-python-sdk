# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeClusterRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        instance_id: str = None,
        request_pars: str = None,
        upgrade_version: str = None,
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
        # The extended request parameters in the JSON format.
        self.request_pars = request_pars
        # The destination version.
        # 
        # This parameter is required.
        self.upgrade_version = upgrade_version

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

        if self.request_pars is not None:
            result['RequestPars'] = self.request_pars

        if self.upgrade_version is not None:
            result['UpgradeVersion'] = self.upgrade_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestPars') is not None:
            self.request_pars = m.get('RequestPars')

        if m.get('UpgradeVersion') is not None:
            self.upgrade_version = m.get('UpgradeVersion')

        return self

