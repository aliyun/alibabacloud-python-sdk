# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateExportTaskRequest(DaraModel):
    def __init__(
        self,
        export_fields: List[str] = None,
        query_param_json: str = None,
        task_type: str = None,
    ):
        # The list of field codes for the export columns. This parameter is optional and applies only to WUYING_SERVER_LIST. Do not pass this parameter for other task types. You can pass up to 100 elements. The codes are case-sensitive. Leading and trailing whitespace in fields is removed, and blank elements are ignored. Duplicate codes are retained in the order of their first appearance. WuyingServerId is always the first column, and the remaining columns are exported in the order of the request. If this parameter is not passed, only WuyingServerId is exported.
        # 
        # Supported codes: WuyingServerId, WuyingServerName, Status, BizRegionId, ZoneId, OfficeSiteId, ServerInstanceType, ServerInstanceTypeId, Cpu, Memory, Image, OsType, ImageId, SystemDisk, DataDisks, NetworkInterfaceIp, PrivateIpSets, SecurityGroupIds, Bandwidth, ChargeType, SubPayType, VirtualNodePool, CreateTime, ExpiredTime, and VirtualKubeletInfo.
        # 
        # In the original RPC request, pass the values sequentially by using ExportFields.1, ExportFields.2, and so on. For example, ExportFields.1=WuyingServerId and ExportFields.2=Status.
        self.export_fields = export_fields
        # The JSON string serialized from the query condition object. This parameter is required and cannot be an empty string. Field names must use the following lower camel case format.
        # 
        # - WUYING_SERVER_LIST: If no filter condition is specified, pass the JSON string corresponding to {}. Only wuyingServerIdList, wuyingServerNameOrId, status, bizRegionId, zoneId, officeSiteId, serverInstanceType, imageId, chargeType, virtualNodePoolId, addVirtualNodePoolStatusList, users, networkInterfaceIp, createTimeStart, createTimeEnd, expiredTimeStart, and expiredTimeEnd are supported. The semantics of each field are the same as those in ListWuyingServer. Pagination or other unlisted fields cannot be passed. The values of wuyingServerIdList, addVirtualNodePoolStatusList, and users must be serialized into JSON array strings before the outer query object is serialized.
        # - BROWSER_BOOKMARK_LIST and BROWSER_RESTRICTED_URL_LIST: The object must and can only contain browserInstanceGroupId, and the value must be a non-empty cloud browser delivery group ID string. It cannot contain Keyword, pagination, or other fields.
        # - USER_USAGE_REPORT: Use productType, startDate, and endDate to specify the product type and query time range. You can use appInstanceGroupId, bizRegionId, userId, and connectionStatus for filtering. startDate and endDate must be in the yyyy-MM-dd HH:mm:ss format. Query parameters are parsed and verified during the asynchronous execution phase. A successful creation does not mean that all these query conditions have passed the verification.
        self.query_param_json = query_param_json
        # The type of the export task. This parameter is required and case-sensitive. Valid values:
        # - WUYING_SERVER_LIST: WUYING server list.
        # - USER_USAGE_REPORT: user usage report.
        # - BROWSER_BOOKMARK_LIST: cloud browser bookmark list.
        # - BROWSER_RESTRICTED_URL_LIST: cloud browser URL whitelist.
        # 
        # Different task types use different QueryParamJson query conditions. Only WUYING_SERVER_LIST supports selecting export columns by using ExportFields.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.export_fields is not None:
            result['ExportFields'] = self.export_fields

        if self.query_param_json is not None:
            result['QueryParamJson'] = self.query_param_json

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportFields') is not None:
            self.export_fields = m.get('ExportFields')

        if m.get('QueryParamJson') is not None:
            self.query_param_json = m.get('QueryParamJson')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

