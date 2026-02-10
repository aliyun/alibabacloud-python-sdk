# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateAgentClientInstallRequest(DaraModel):
    def __init__(
        self,
        instance_ids: str = None,
        lang: str = None,
        os: str = None,
        region: str = None,
        uuids: str = None,
    ):
        # The IDs of the servers on which you want to install the Security Center agent. Separate multiple IDs with commas (,).
        # 
        # > : You must specify at least one of **InstanceIds** and **Uuids**. If you specify **InstanceIds**, you must also specify **Region** and **Os**.
        self.instance_ids = instance_ids
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The operating system of the servers. Valid values:
        # 
        # *   **linux**
        # *   **windows**
        self.os = os
        # The region where the servers reside. Valid values include the following regions:
        # 
        # *   cn-hangzhou: China (Hangzhou)
        # *   cn-beijing: China (Beijing)
        # *   cn-shanghai: China (Shanghai)
        # *   cn-zhangjiakou: China (Zhangjiakou)
        # *   cn-shenzhen: China (Shenzhen)
        self.region = region
        # The UUIDs of the servers on which you want to install the Security Center agent. Separate multiple UUIDs with commas (,).
        # 
        # > You must specify at least one of the **InstanceIds** and **Uuids** parameters before you can call this operation.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.os is not None:
            result['Os'] = self.os

        if self.region is not None:
            result['Region'] = self.region

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

