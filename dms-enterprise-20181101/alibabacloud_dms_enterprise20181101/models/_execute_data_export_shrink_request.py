# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteDataExportShrinkRequest(DaraModel):
    def __init__(
        self,
        action_detail_shrink: str = None,
        order_id: int = None,
        real_login_user_uid: str = None,
        tid: int = None,
    ):
        # The parameters that are required to perform the operation. Sample code:
        # 
        # ```json
        # {
        #   "mode" : "FAST",   // The mode in which data is exported. Default value: FAST. A value of NORMAL specifies that the export task can be terminated during the export.  "encoding" : "UTF8",  // The encoding format.  "startTime" : "2022-12-22 00:00:00",  // The point in time at which data export starts.  "transaction" : false,    // Specifies whether to enable transactions.  "fileType" : "SQL"    // The format of the exported file.}
        # ```
        # 
        # >  You can also set mode, encoding, and fileType to the following values:
        # 
        # *   mode: NORMAL
        # 
        # *   encoding: UTF8MB4, GB2312, ISO_8859_1, GBK, LATAIN1, or CP1252
        # 
        # *   fileType: XLSX, CSV, JSON, or TXT
        self.action_detail_shrink = action_detail_shrink
        # The ID of the ticket.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The ID of the Alibaba Cloud account that is used to call the API operation.
        self.real_login_user_uid = real_login_user_uid
        # The ID of the tenant.
        # 
        # > : To view the ID of the tenant, log on to the Data Management (DMS) console and move the pointer over the profile picture in the upper-right corner. For more information, see [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_detail_shrink is not None:
            result['ActionDetail'] = self.action_detail_shrink

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.real_login_user_uid is not None:
            result['RealLoginUserUid'] = self.real_login_user_uid

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionDetail') is not None:
            self.action_detail_shrink = m.get('ActionDetail')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

