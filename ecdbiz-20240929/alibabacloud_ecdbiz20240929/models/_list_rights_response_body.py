# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecdbiz20240929 import models as main_models
from darabonba.model import DaraModel

class ListRightsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListRightsResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The business processing result code.
        self.code = code
        # The list of rights on the current page.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The maximum number of results per page. Specify a positive integer from 1 to 200.
        self.max_results = max_results
        # The description of the processing result. This is used for troubleshooting when a failure occurs.
        self.message = message
        # The pagination token for the next page. An empty value indicates that the current query has ended. If the value is not empty, pass it exactly as it is in the next query. The example is for illustration purposes only.
        self.next_token = next_token
        # The unique identifier of the request. This is used to troubleshoot call issues.
        self.request_id = request_id
        # Indicates whether the request was processed successfully. A successful activation request does not mean that the resource has been created.
        self.success = success
        # The total number of rights that meet the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListRightsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRightsResponseBodyData(DaraModel):
    def __init__(
        self,
        add_data_disk_size: int = None,
        add_root_disk_size: int = None,
        ai_desktop: bool = None,
        business_scene_code: str = None,
        calculating_code: str = None,
        data_disk_size: int = None,
        gmt_create: str = None,
        hibernate: int = None,
        monthly_credit: str = None,
        overseas: int = None,
        rights_active_failure_cause: str = None,
        rights_active_status: str = None,
        rights_active_time: str = None,
        rights_assigned_user: str = None,
        rights_expire_time: str = None,
        rights_gpu_spec: str = None,
        rights_id: str = None,
        rights_inventory_spec: str = None,
        rights_period: str = None,
        rights_resource_area: str = None,
        rights_resource_expire_time: str = None,
        rights_resource_id: str = None,
        rights_resource_region: str = None,
        rights_resource_status: str = None,
        rights_resource_type: str = None,
        rights_source_name: str = None,
        rights_spec: str = None,
        system_disk_size: int = None,
        value_package_infos: List[main_models.ListRightsResponseBodyDataValuePackageInfos] = None,
    ):
        # The size of the additional data cloud disk. Unit: GiB.
        self.add_data_disk_size = add_data_disk_size
        # The size of the additional system cloud disk. Unit: GiB.
        self.add_root_disk_size = add_root_disk_size
        # Indicates whether the cloud computer is an AI cloud computer. Valid values:
        # - true: AI cloud computer.
        # - false: Regular cloud computer.
        self.ai_desktop = ai_desktop
        # The scenario code for the commercial edition.
        self.business_scene_code = business_scene_code
        # The compute plan code. Refer to the actual returned value of the rights.
        self.calculating_code = calculating_code
        # The size of the data cloud disk. Unit: GiB.
        self.data_disk_size = data_disk_size
        # The time when the rights record was created. The time is in RFC 3339 UTC format and ends with Z.
        self.gmt_create = gmt_create
        # The hibernation options for the rights. The actual policy is determined in combination with the compute plan.
        self.hibernate = hibernate
        # The monthly credit information corresponding to the rights. This value may be empty if this configuration is not available.
        self.monthly_credit = monthly_credit
        # Specifies whether the rights apply to regions outside the Chinese mainland, including Hong Kong (China), Macao (China), and Taiwan (China). Valid values:
        # - 0: The Chinese mainland.
        # - 1: Regions outside the Chinese mainland, including Hong Kong (China), Macao (China), and Taiwan (China).
        self.overseas = overseas
        # The cause of the rights activation failure. This value may be empty if the activation is successful.
        self.rights_active_failure_cause = rights_active_failure_cause
        # The rights activation status. Use the returned value to determine whether the activation is complete.
        self.rights_active_status = rights_active_status
        # The time when the rights were activated. This value may be empty if the rights are not yet activated. The time is in RFC 3339 UTC format and ends with Z.
        self.rights_active_time = rights_active_time
        # The end user to whom the rights are assigned. For convenience accounts, use EndUserId.
        self.rights_assigned_user = rights_assigned_user
        # The deadline for manual activation of the rights. This is different from RightsResourceExpireTime, which is the expiration time of the resource after activation. The time is in RFC 3339 UTC format and ends with Z.
        self.rights_expire_time = rights_expire_time
        # The GPU specification. Refer to the returned value in the rights details.
        self.rights_gpu_spec = rights_gpu_spec
        # The rights ID. Use this value for activation. This is not the cloud computer resource ID.
        self.rights_id = rights_id
        # The inventory specification corresponding to the rights.
        self.rights_inventory_spec = rights_inventory_spec
        # The rights period code.
        self.rights_period = rights_period
        # The area to which the rights belong. This cannot replace the resource region in a new activation request.
        self.rights_resource_area = rights_resource_area
        # The actual expiration time of the resource. This is different from the deadline for rights activation. The time is in RFC 3339 UTC format and ends with Z.
        self.rights_resource_expire_time = rights_resource_expire_time
        # The ID of the resource associated with the rights. This value is returned after the resource is created.
        self.rights_resource_id = rights_resource_id
        # The region ID of the resource. This is configured separately from the POP request routing region.
        self.rights_resource_region = rights_resource_region
        # The status of the associated resource. Refer to the returned value for the actual status.
        self.rights_resource_status = rights_resource_status
        # The rights resource type. Use Desktop for regular cloud computers. For other commodities, specify the actual rights type.
        self.rights_resource_type = rights_resource_type
        # The name of the rights source.
        self.rights_source_name = rights_source_name
        # The rights specification code. Refer to the rights query results for the actual value.
        self.rights_spec = rights_spec
        # The size of the system cloud disk. Unit: GiB.
        self.system_disk_size = system_disk_size
        # The list of value-added feature information associated with the rights.
        self.value_package_infos = value_package_infos

    def validate(self):
        if self.value_package_infos:
            for v1 in self.value_package_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_data_disk_size is not None:
            result['AddDataDiskSize'] = self.add_data_disk_size

        if self.add_root_disk_size is not None:
            result['AddRootDiskSize'] = self.add_root_disk_size

        if self.ai_desktop is not None:
            result['AiDesktop'] = self.ai_desktop

        if self.business_scene_code is not None:
            result['BusinessSceneCode'] = self.business_scene_code

        if self.calculating_code is not None:
            result['CalculatingCode'] = self.calculating_code

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.hibernate is not None:
            result['Hibernate'] = self.hibernate

        if self.monthly_credit is not None:
            result['MonthlyCredit'] = self.monthly_credit

        if self.overseas is not None:
            result['Overseas'] = self.overseas

        if self.rights_active_failure_cause is not None:
            result['RightsActiveFailureCause'] = self.rights_active_failure_cause

        if self.rights_active_status is not None:
            result['RightsActiveStatus'] = self.rights_active_status

        if self.rights_active_time is not None:
            result['RightsActiveTime'] = self.rights_active_time

        if self.rights_assigned_user is not None:
            result['RightsAssignedUser'] = self.rights_assigned_user

        if self.rights_expire_time is not None:
            result['RightsExpireTime'] = self.rights_expire_time

        if self.rights_gpu_spec is not None:
            result['RightsGpuSpec'] = self.rights_gpu_spec

        if self.rights_id is not None:
            result['RightsId'] = self.rights_id

        if self.rights_inventory_spec is not None:
            result['RightsInventorySpec'] = self.rights_inventory_spec

        if self.rights_period is not None:
            result['RightsPeriod'] = self.rights_period

        if self.rights_resource_area is not None:
            result['RightsResourceArea'] = self.rights_resource_area

        if self.rights_resource_expire_time is not None:
            result['RightsResourceExpireTime'] = self.rights_resource_expire_time

        if self.rights_resource_id is not None:
            result['RightsResourceId'] = self.rights_resource_id

        if self.rights_resource_region is not None:
            result['RightsResourceRegion'] = self.rights_resource_region

        if self.rights_resource_status is not None:
            result['RightsResourceStatus'] = self.rights_resource_status

        if self.rights_resource_type is not None:
            result['RightsResourceType'] = self.rights_resource_type

        if self.rights_source_name is not None:
            result['RightsSourceName'] = self.rights_source_name

        if self.rights_spec is not None:
            result['RightsSpec'] = self.rights_spec

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        result['ValuePackageInfos'] = []
        if self.value_package_infos is not None:
            for k1 in self.value_package_infos:
                result['ValuePackageInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddDataDiskSize') is not None:
            self.add_data_disk_size = m.get('AddDataDiskSize')

        if m.get('AddRootDiskSize') is not None:
            self.add_root_disk_size = m.get('AddRootDiskSize')

        if m.get('AiDesktop') is not None:
            self.ai_desktop = m.get('AiDesktop')

        if m.get('BusinessSceneCode') is not None:
            self.business_scene_code = m.get('BusinessSceneCode')

        if m.get('CalculatingCode') is not None:
            self.calculating_code = m.get('CalculatingCode')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Hibernate') is not None:
            self.hibernate = m.get('Hibernate')

        if m.get('MonthlyCredit') is not None:
            self.monthly_credit = m.get('MonthlyCredit')

        if m.get('Overseas') is not None:
            self.overseas = m.get('Overseas')

        if m.get('RightsActiveFailureCause') is not None:
            self.rights_active_failure_cause = m.get('RightsActiveFailureCause')

        if m.get('RightsActiveStatus') is not None:
            self.rights_active_status = m.get('RightsActiveStatus')

        if m.get('RightsActiveTime') is not None:
            self.rights_active_time = m.get('RightsActiveTime')

        if m.get('RightsAssignedUser') is not None:
            self.rights_assigned_user = m.get('RightsAssignedUser')

        if m.get('RightsExpireTime') is not None:
            self.rights_expire_time = m.get('RightsExpireTime')

        if m.get('RightsGpuSpec') is not None:
            self.rights_gpu_spec = m.get('RightsGpuSpec')

        if m.get('RightsId') is not None:
            self.rights_id = m.get('RightsId')

        if m.get('RightsInventorySpec') is not None:
            self.rights_inventory_spec = m.get('RightsInventorySpec')

        if m.get('RightsPeriod') is not None:
            self.rights_period = m.get('RightsPeriod')

        if m.get('RightsResourceArea') is not None:
            self.rights_resource_area = m.get('RightsResourceArea')

        if m.get('RightsResourceExpireTime') is not None:
            self.rights_resource_expire_time = m.get('RightsResourceExpireTime')

        if m.get('RightsResourceId') is not None:
            self.rights_resource_id = m.get('RightsResourceId')

        if m.get('RightsResourceRegion') is not None:
            self.rights_resource_region = m.get('RightsResourceRegion')

        if m.get('RightsResourceStatus') is not None:
            self.rights_resource_status = m.get('RightsResourceStatus')

        if m.get('RightsResourceType') is not None:
            self.rights_resource_type = m.get('RightsResourceType')

        if m.get('RightsSourceName') is not None:
            self.rights_source_name = m.get('RightsSourceName')

        if m.get('RightsSpec') is not None:
            self.rights_spec = m.get('RightsSpec')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        self.value_package_infos = []
        if m.get('ValuePackageInfos') is not None:
            for k1 in m.get('ValuePackageInfos'):
                temp_model = main_models.ListRightsResponseBodyDataValuePackageInfos()
                self.value_package_infos.append(temp_model.from_map(k1))

        return self



class ListRightsResponseBodyDataValuePackageInfos(DaraModel):
    def __init__(
        self,
        function: str = None,
        value_package_code: str = None,
    ):
        # The content of the value-added feature.
        self.function = function
        # The value-added feature code.
        self.value_package_code = value_package_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.function is not None:
            result['Function'] = self.function

        if self.value_package_code is not None:
            result['ValuePackageCode'] = self.value_package_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Function') is not None:
            self.function = m.get('Function')

        if m.get('ValuePackageCode') is not None:
            self.value_package_code = m.get('ValuePackageCode')

        return self

