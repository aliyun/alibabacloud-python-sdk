# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProjectRequest(DaraModel):
    def __init__(
        self,
        project_name: str = None,
        with_statistics: bool = None,
    ):
        # The name of the project. You can obtain the name from the response of the [CreateProject](https://help.aliyun.com/document_detail/478153.html) operation.
        # 
        # This parameter is required.
        self.project_name = project_name
        # Specifies whether to enable real-time retrieval of file statistics. Default value: false.
        # 
        # *   If you set the value to true, the returned values of FileCount and TotalFileSize in the response are valid.
        # *   If you set the value to false, the returned values of FileCount and TotalFileSize in the response are invalid or equal to 0.
        self.with_statistics = with_statistics

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.with_statistics is not None:
            result['WithStatistics'] = self.with_statistics

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('WithStatistics') is not None:
            self.with_statistics = m.get('WithStatistics')

        return self

