# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCAInstanceStatusRequest(DaraModel):
    def __init__(
        self,
        identifier: str = None,
        instance_id: str = None,
    ):
        # The unique identifier of the certificate.
        self.identifier = identifier
        # The ID of the private CA instance.
        # 
        # >  After you purchase a private CA instance by using the [SSL Certificates Service console](https://yundun.console.aliyun.com/?p=cas#/pca/rootlist), you can click **Details** for the private CA instance on the **Private Certificates** page to query the ID of the private CA instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

