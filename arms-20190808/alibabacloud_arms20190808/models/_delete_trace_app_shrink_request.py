# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTraceAppShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        delete_reason_shrink: str = None,
        pid: str = None,
        region_id: str = None,
        type: str = None,
    ):
        # The ID of the application that you want to delete. You can call the SearchTraceAppByName operation to query the application ID. For more information, see [SearchTraceAppByName](https://help.aliyun.com/document_detail/130676.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The reason(s) to delete application.
        self.delete_reason_shrink = delete_reason_shrink
        # The PID of the application. For more information about how to query the PID, see [QueryMetricByPage](https://www.alibabacloud.com/help/zh/doc-detail/186100.htm?spm=a2cdw.13409063.0.0.7a72281f0bkTfx#title-imy-7gj-qhr).
        # 
        # This parameter is required.
        self.pid = pid
        # The ID of the region in which the application is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The type of the application that you want to delete. You can call the SearchTraceAppByName operation to query the application type. For more information, see [SearchTraceAppByName](https://help.aliyun.com/document_detail/130676.html). Valid values:
        # 
        # *   `TRACE`: Application Monitoring
        # *   `RETCODE`: frontend monitoring
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.delete_reason_shrink is not None:
            result['DeleteReason'] = self.delete_reason_shrink

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DeleteReason') is not None:
            self.delete_reason_shrink = m.get('DeleteReason')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

