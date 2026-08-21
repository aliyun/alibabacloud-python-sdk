# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDiagnosisRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        current: int = None,
        page_size: int = None,
        params: str = None,
        service_name: str = None,
        status: str = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The current page number.
        self.current = current
        # The number of entries per page.
        self.page_size = page_size
        # The diagnostic parameters. Different diagnostic types require different diagnostic parameters. You can use this field to filter records whose parameters match the specified values.
        self.params = params
        # The diagnostic type.
        self.service_name = service_name
        # The execution status of the diagnostic task.
        # 
        # Valid values:
        # - **Ready**: Ready.
        # - **Running**: Running.
        # - **Success**: Succeeded.
        # - **Fail**: Failed.
        self.status = status
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.current is not None:
            result['current'] = self.current

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.params is not None:
            result['params'] = self.params

        if self.service_name is not None:
            result['service_name'] = self.service_name

        if self.status is not None:
            result['status'] = self.status

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('current') is not None:
            self.current = m.get('current')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('params') is not None:
            self.params = m.get('params')

        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

