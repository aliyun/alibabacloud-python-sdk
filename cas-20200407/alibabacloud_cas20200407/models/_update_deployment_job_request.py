# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateDeploymentJobRequest(DaraModel):
    def __init__(
        self,
        cert_ids: str = None,
        contact_ids: str = None,
        job_id: int = None,
        name: str = None,
        resource_ids: str = None,
        schedule_time: int = None,
    ):
        # The ID of the certificate. Separate multiple certificate IDs with commas (,). You can call the [ListUserCertificateOrder](https://help.aliyun.com/document_detail/455804.html) operation to obtain the ID of a certificate from the **CertificateId** parameter.
        self.cert_ids = cert_ids
        # The ID of the contact. Separate multiple contact IDs with commas (,). You can call the [ListContact](https://help.aliyun.com/document_detail/2712221.html) operation to obtain the ID of a contact from the **ContactId** parameter.
        self.contact_ids = contact_ids
        # The ID of the deployment task. You can call the [CreateDeploymentJob](https://help.aliyun.com/document_detail/2712234.html) operation to obtain the ID of a deployment task from the JobId parameter. You can also call the [ListDeploymentJob](https://help.aliyun.com/document_detail/2712223.html) operation to obtain the ID of a deployment task.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The name of the deployment task.
        self.name = name
        # The ID of the cloud resource. Separate multiple resource IDs with commas (,). You can call the [ListCloudResources](https://help.aliyun.com/document_detail/2712230.html) operation to obtain the ID of a cloud resource from the **Id** parameter.
        self.resource_ids = resource_ids
        # The time when the task starts. The value is a UNIX timestamp. If you do not specify this parameter, the system immediately starts the task after it is created.
        self.schedule_time = schedule_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_ids is not None:
            result['CertIds'] = self.cert_ids

        if self.contact_ids is not None:
            result['ContactIds'] = self.contact_ids

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.name is not None:
            result['Name'] = self.name

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertIds') is not None:
            self.cert_ids = m.get('CertIds')

        if m.get('ContactIds') is not None:
            self.contact_ids = m.get('ContactIds')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        return self

