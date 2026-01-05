# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListResourceGroupAssociateProjectsResponseBody(DaraModel):
    def __init__(
        self,
        project_id_list: List[int] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of workspace IDs.
        self.project_id_list = project_id_list
        # The request ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_id_list is not None:
            result['ProjectIdList'] = self.project_id_list

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectIdList') is not None:
            self.project_id_list = m.get('ProjectIdList')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

