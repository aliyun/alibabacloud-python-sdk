# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCommonLogsShrinkRequest(DaraModel):
    def __init__(
        self,
        action_name_shrink: str = None,
        action_status: str = None,
        cluster_id: str = None,
        from_: int = None,
        is_reverse: bool = None,
        log_request_id: str = None,
        log_type: str = None,
        operator_uid: str = None,
        page_number: int = None,
        page_size: int = None,
        resource: str = None,
        to: int = None,
    ):
        # The action types.
        self.action_name_shrink = action_name_shrink
        # The action status. Logs associated with the specific action status are returned.
        # 
        # Valid values:
        # 
        # *   Finished: The action is completed.
        # *   Failed: The action failed.
        # *   InProgress: The action is being performed.
        self.action_status = action_status
        # The cluster ID.
        self.cluster_id = cluster_id
        # The start time of the time range. The time is a timestamp. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.from_ = from_
        # Specifies whether to display results in reverse order.
        # 
        # Default value: true
        self.is_reverse = is_reverse
        # The request ID of the action. Logs associated with the specific request ID are returned.
        self.log_request_id = log_request_id
        # The log type. Logs of the specific type are returned.
        self.log_type = log_type
        # The account ID of the operator.
        self.operator_uid = operator_uid
        # The page number of the page to return.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.page_size = page_size
        # The name of the resource involved in the action. Logs associated with the specific resource are returned. This parameter is not recommended.
        self.resource = resource
        # The end time of the time range. The time is a timestamp. This value is a UNIX timestamp representing the number of seconds that have elapsed since the epoch time January 1, 1970, 00:00:00 UTC.
        # 
        # This parameter is required.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_name_shrink is not None:
            result['ActionName'] = self.action_name_shrink

        if self.action_status is not None:
            result['ActionStatus'] = self.action_status

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.from_ is not None:
            result['From'] = self.from_

        if self.is_reverse is not None:
            result['IsReverse'] = self.is_reverse

        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.operator_uid is not None:
            result['OperatorUid'] = self.operator_uid

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionName') is not None:
            self.action_name_shrink = m.get('ActionName')

        if m.get('ActionStatus') is not None:
            self.action_status = m.get('ActionStatus')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('IsReverse') is not None:
            self.is_reverse = m.get('IsReverse')

        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('OperatorUid') is not None:
            self.operator_uid = m.get('OperatorUid')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

