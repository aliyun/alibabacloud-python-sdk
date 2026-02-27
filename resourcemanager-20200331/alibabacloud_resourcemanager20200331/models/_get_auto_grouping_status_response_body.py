# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAutoGroupingStatusResponseBody(DaraModel):
    def __init__(
        self,
        enable_existed_resources_transfer: bool = None,
        enable_status: str = None,
        request_id: str = None,
    ):
        # Indicates whether the Transfer Existing Associated Resources feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.enable_existed_resources_transfer = enable_existed_resources_transfer
        # The status of the Automatic Resource Transfer feature. Valid values:
        # 
        # *   Enabling: The feature is being enabled.
        # *   Enable: The feature is enabled.
        # *   Partial_Enable: The transfer of associated resources is enabled, but custom transfer rule-based resource transfer is disabled. You can call the [EnableAutoGrouping](https://help.aliyun.com/document_detail/2870380.html) operation to enable custom transfer rule-based resource transfer.
        # *   Disable: The feature is disabled.
        self.enable_status = enable_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_existed_resources_transfer is not None:
            result['EnableExistedResourcesTransfer'] = self.enable_existed_resources_transfer

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableExistedResourcesTransfer') is not None:
            self.enable_existed_resources_transfer = m.get('EnableExistedResourcesTransfer')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

