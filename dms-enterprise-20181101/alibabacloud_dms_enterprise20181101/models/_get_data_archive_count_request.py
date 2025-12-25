# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataArchiveCountRequest(DaraModel):
    def __init__(
        self,
        order_result_type: str = None,
        plugin_type: str = None,
        search_date_type: str = None,
        tid: int = None,
    ):
        # The type of the identity. Default value: AS_ADMIN.
        self.order_result_type = order_result_type
        # The plugin type. Default value: DATA_ARCHIVE.
        self.plugin_type = plugin_type
        # The time when the ticket is modified or created. The statistics of data archiving tickets are calculated based on the creation time.
        self.search_date_type = search_date_type
        # The tenant ID.
        # 
        # >  To view the tenant ID, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_result_type is not None:
            result['OrderResultType'] = self.order_result_type

        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type

        if self.search_date_type is not None:
            result['SearchDateType'] = self.search_date_type

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderResultType') is not None:
            self.order_result_type = m.get('OrderResultType')

        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')

        if m.get('SearchDateType') is not None:
            self.search_date_type = m.get('SearchDateType')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

