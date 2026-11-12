# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAICallDetailsRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        end_time: str = None,
        gateway_region: str = None,
        model_id: str = None,
        page_number: int = None,
        page_size: int = None,
        search_request_id: str = None,
        start_time: str = None,
        wy_ids: List[str] = None,
    ):
        # The business edition. Valid values: ENTERPRISE or 1 for Enterprise Edition, and BUSINESS or 20 for Business Edition. Default value: Enterprise Edition.
        self.biz_type = biz_type
        # The end time of the query, exclusive. Specify the time in ISO 8601 format with time zone, accurate to seconds. Default value: the current time. The end time must be later than StartTime and cannot be later than the current time.
        self.end_time = end_time
        # The region of the AI gateway logs. Valid values: cn-shanghai (Shanghai), cn-hongkong (Hong Kong), ap-southeast-1 (Singapore), and us-east-1 (US East). The cn-hangzhou value is also supported and routed to cn-shanghai in the production environment. If this parameter is not specified, the default value is cn-shanghai for the China site and ap-southeast-1 for the international site.
        self.gateway_region = gateway_region
        # The requested model ID during invocation for exact match. Fuzzy match is not supported. This ID may be different from the actual executed model Model returned in the response. If this parameter is not specified or is left empty, no filtering is performed. The value can be up to 128 characters in length and cannot contain control characters or vertical bars.
        self.model_id = model_id
        # The page number. Pages start from page 1. Default value: 1. The product of PageNumber and PageSize cannot exceed 1,000,000.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 50. Default value: 10.
        self.page_size = page_size
        # The model invocation request ID for exact match. This ID is different from the RequestId of the current API operation. If this parameter is not specified or is left empty, no filtering is performed. The value can be up to 128 characters in length and cannot contain control characters or vertical bars. This condition is combined with other filter conditions by using the AND operator.
        self.search_request_id = search_request_id
        # The start time of the query, inclusive. Specify the time in ISO 8601 format with time zone, accurate to seconds. Default value: 00:00:00 (UTC+8) of the current day. The start time cannot be earlier than three calendar months before the current time, and the query time range cannot exceed 30 days.
        self.start_time = start_time
        # The list of user IDs. You can specify up to 50 user IDs. If this parameter is not specified or an empty array is passed, no filtering is performed. The user IDs in the list are combined by using the OR operator, and this condition is combined with other filter conditions by using the AND operator.
        self.wy_ids = wy_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gateway_region is not None:
            result['GatewayRegion'] = self.gateway_region

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_request_id is not None:
            result['SearchRequestId'] = self.search_request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.wy_ids is not None:
            result['WyIds'] = self.wy_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GatewayRegion') is not None:
            self.gateway_region = m.get('GatewayRegion')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchRequestId') is not None:
            self.search_request_id = m.get('SearchRequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WyIds') is not None:
            self.wy_ids = m.get('WyIds')

        return self

