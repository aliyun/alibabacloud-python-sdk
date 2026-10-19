# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDeploymentJobRequest(DaraModel):
    def __init__(
        self,
        cert_id: int = None,
        current_page: int = None,
        instance_id: str = None,
        job_type: str = None,
        show_size: int = None,
        status: str = None,
    ):
        # The certificate ID.
        # > You can obtain this ID by calling the [ListUserCertificateOrder](https://help.aliyun.com/document_detail/455804.html) operation.
        self.cert_id = cert_id
        # The current page number. Default value: 1.
        self.current_page = current_page
        # The instance ID.
        self.instance_id = instance_id
        # The task type.
        self.job_type = job_type
        # The paging Settings for the number of certificates to return on each page during a paged query. Default value: **50**.
        self.show_size = show_size
        # The deployment task status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cert_id is not None:
            result['CertId'] = self.cert_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertId') is not None:
            self.cert_id = m.get('CertId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

