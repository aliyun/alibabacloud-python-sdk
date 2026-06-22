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
        # The project name. For information about how to obtain the project name, see [创建项目](https://help.aliyun.com/document_detail/478153.html).
        # 
        # This parameter is required.
        self.project_name = project_name
        # Specifies whether to collect file statistics. Default value: false, which indicates that file statistics are not collected.
        # 
        # - File statistics are collected. The FileCount and TotalFileSize values in the returned Project struct are valid.
        # 
        # - File statistics are not collected. The FileCount and TotalFileSize values in the returned Project struct may be inaccurate or both may be 0.
        # 
        # >Notice: Only files in datasets created before December 20, 2025 can be counted..
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

