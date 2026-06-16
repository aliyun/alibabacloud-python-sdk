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
        # The unique identifier of the client certificate or server-side certificate to query.
        # 
        # > Call [ListClientCertificate](https://help.aliyun.com/document_detail/330884.html) to query the unique identifiers of all client certificates and server-side certificates.
        self.identifier = identifier
        # The ID of the private CA instance to query.
        # 
        # > After you purchase a private CA instance in the [CAS console](https://yundun.console.aliyun.com/?p=cas#/pca/rootlist), you can go to the **Private Certificates** page and view the **details** of the instance to obtain its ID.
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

