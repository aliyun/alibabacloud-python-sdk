# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class OperateAgentClientInstallResponseBody(DaraModel):
    def __init__(
        self,
        aegis_celint_install_respose_list: List[main_models.OperateAgentClientInstallResponseBodyAegisCelintInstallResposeList] = None,
        request_id: str = None,
    ):
        # An array that consists of the returned results.
        self.aegis_celint_install_respose_list = aegis_celint_install_respose_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.aegis_celint_install_respose_list:
            for v1 in self.aegis_celint_install_respose_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AegisCelintInstallResposeList'] = []
        if self.aegis_celint_install_respose_list is not None:
            for k1 in self.aegis_celint_install_respose_list:
                result['AegisCelintInstallResposeList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aegis_celint_install_respose_list = []
        if m.get('AegisCelintInstallResposeList') is not None:
            for k1 in m.get('AegisCelintInstallResposeList'):
                temp_model = main_models.OperateAgentClientInstallResponseBodyAegisCelintInstallResposeList()
                self.aegis_celint_install_respose_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OperateAgentClientInstallResponseBodyAegisCelintInstallResposeList(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        record_id: int = None,
        uuid: str = None,
    ):
        # The ID of the server.
        self.instance_id = instance_id
        # The ID of the installation task.
        self.record_id = record_id
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

