# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListWorkerResourceRequest(DaraModel):
    def __init__(
        self,
        cloud_product: str = None,
        current_page: int = None,
        job_id: int = None,
        show_size: int = None,
        status: str = None,
    ):
        # The cloud service in the deployment task.
        self.cloud_product = cloud_product
        # The page number. Default value: **1**.
        self.current_page = current_page
        # The ID of the deployment task. You can call the [CreateDeploymentJob](https://help.aliyun.com/document_detail/2712234.html) operation to obtain the ID of a deployment task from the **ID** parameter. You can also call the [ListDeploymentJob](https://help.aliyun.com/document_detail/2712223.html) operation to obtain the ID of a deployment task.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The number of entries per page. Default value: 50.
        self.show_size = show_size
        # The status of the worker task.
        # 
        # Valid values:
        # 
        # *   rollback
        # *   rollback_error
        # *   success
        # *   rollback_success
        # *   pending
        # *   scheduling
        # *   processing
        # *   error
        # *   editing
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_product is not None:
            result['CloudProduct'] = self.cloud_product

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudProduct') is not None:
            self.cloud_product = m.get('CloudProduct')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

