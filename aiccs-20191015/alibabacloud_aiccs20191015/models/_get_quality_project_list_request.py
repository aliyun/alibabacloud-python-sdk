# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQualityProjectListRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        project_id: int = None,
        project_name: str = None,
        status: int = None,
        check_freq_type: int = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
        self.project_id = project_id
        self.project_name = project_name
        self.status = status
        self.check_freq_type = check_freq_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.status is not None:
            result['Status'] = self.status

        if self.check_freq_type is not None:
            result['checkFreqType'] = self.check_freq_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('checkFreqType') is not None:
            self.check_freq_type = m.get('checkFreqType')

        return self

