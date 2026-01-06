# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDeploymentJobRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        job_type: str = None,
        show_size: int = None,
        status: str = None,
    ):
        # The page number. Default value: 1.
        self.current_page = current_page
        # The type of the deployment task.
        # 
        # Valid values:
        # 
        # *   cloud: multi-cloud deployment task.
        # *   user: cloud service deployment task. This type of task does not support Elastic Compute Service (ECS) instances.
        self.job_type = job_type
        # The number of certificates per page. Default value: **50**.
        self.show_size = show_size
        # The status of the deployment task.
        # 
        # Valid values:
        # 
        # *   success
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
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

