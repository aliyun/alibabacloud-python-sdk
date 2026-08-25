# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOperationAuditLogsRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        end_time: str = None,
        event_type: str = None,
        operation_func: str = None,
        operation_status: str = None,
        operation_type: str = None,
        operator_id: str = None,
        page_size: int = None,
        start_time: str = None,
    ):
        # The page number of the current page in paging. The value starts from 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The end time of the query. This value is a UNIX timestamp in seconds. The value must be later than StartTime.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The event source type. Valid values:
        # - **console**: console call.
        # - **sdk**: SDK call.
        self.event_type = event_type
        # The operation function module. The value is the English code of the function module. If other values are specified, no records are returned. Valid values:
        # - **PrivateAccess**: private access.
        # - **OfficeNetworkAccess**: office network access.
        # - **AppAcceleration**: application acceleration.
        # - **InternetAccess**: Internet access.
        # - **OfficeDataProtection**: office data protection.
        # - **IdentityAccessManagement**: identity and access management.
        # - **DeviceManagement**: device management.
        # - **ApprovalCenter**: approval center.
        # - **SoftwareManagement**: software management.
        # - **LogAnalysis**: log analysis.
        # - **Setting**: settings.
        # - **DigitalWatermark**: digital watermarking.
        # - **DynamicDecision**: dynamic decision.
        # - **InternetBehaviorManagement**: Internet behavior management.
        # - **AgentOfficeSecurity**: Agent office security.
        # - **NetworkAccess**: network access.
        # - **RiskManagement**: risk management.
        # - **EndpointProtection**: endpoint protection.
        # - **Overview**: overview page.
        # - **ITManagement**: IT management.
        # - **InstanceManagement**: instance management.
        self.operation_func = operation_func
        # The operation status. Valid values:
        # - **success**: The operation succeeded. Equivalent values: true, 成功.
        # - **failure**: The operation failed. Equivalent values: fail, failed, false, 失败.
        # 
        # If this parameter is not specified, only successful operation records are returned.
        self.operation_status = operation_status
        # The operation type. The value must exactly match the original operation type recorded in the log. The OperationType value in the response is localized based on the request language and may differ from this filter value.
        self.operation_type = operation_type
        # The Alibaba Cloud account ID (AliUid) of the operator.
        self.operator_id = operator_id
        # The number of entries per page. Settings: 1 to 100. Used in paging.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The start time of the query. This value is a UNIX timestamp in seconds. The value must be earlier than EndTime. The interval between StartTime and EndTime cannot exceed 30 days, and StartTime cannot be more than 31 days before the current time.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.operation_func is not None:
            result['OperationFunc'] = self.operation_func

        if self.operation_status is not None:
            result['OperationStatus'] = self.operation_status

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.operator_id is not None:
            result['OperatorId'] = self.operator_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('OperationFunc') is not None:
            self.operation_func = m.get('OperationFunc')

        if m.get('OperationStatus') is not None:
            self.operation_status = m.get('OperationStatus')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('OperatorId') is not None:
            self.operator_id = m.get('OperatorId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

