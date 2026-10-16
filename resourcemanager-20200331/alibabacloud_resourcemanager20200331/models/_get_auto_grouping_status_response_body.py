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
        # Indicates whether the attached-resource allocation for existing resources is enabled. Valid values:
        # - true: Enabled.
        # - false: Not enabled.
        self.enable_existed_resources_transfer = enable_existed_resources_transfer
        # The status of automatic resource group transfer. Valid values:
        # - Enabling: Being enabled.
        # - Enable: Enabled.
        # - Partial_Enable: Attached-resource allocation is enabled, but custom condition-based resource group transfer is not enabled. To enable custom condition-based resource group transfer, call [EnableAutoGrouping](~~EnableAutoGrouping~~).
        # - Disable: Not enabled.
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

