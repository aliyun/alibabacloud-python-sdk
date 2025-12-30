# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class ListProgramsResponseBody(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        programs: List[main_models.ChannelAssemblyProgram] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 20. Valid values: 1 to 100.
        self.page_size = page_size
        # The programs.
        self.programs = programs
        # **Request ID**
        self.request_id = request_id
        # The total number of programs returned.
        self.total_count = total_count

    def validate(self):
        if self.programs:
            for v1 in self.programs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Programs'] = []
        if self.programs is not None:
            for k1 in self.programs:
                result['Programs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.programs = []
        if m.get('Programs') is not None:
            for k1 in m.get('Programs'):
                temp_model = main_models.ChannelAssemblyProgram()
                self.programs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

