# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_nas20170626 import models as nas20170626_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-chengdu': 'nas.aliyuncs.com',
            'me-east-1': 'nas.ap-northeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'nas.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('nas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_client_to_black_list_with_options(
        self,
        request: nas20170626_models.AddClientToBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.AddClientToBlackListResponse:
        """
        @deprecated OpenAPI AddClientToBlackList is deprecated
        
        @summary Adds a client to the blacklist of a Cloud Parallel File Storage (CPFS) file system and revokes the write access from the client. The blacklist serves as an I/O fence.
        
        @description The API operation is available only for CPFS file systems.
        
        @param request: AddClientToBlackListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddClientToBlackListResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddClientToBlackList',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.AddClientToBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_client_to_black_list_with_options_async(
        self,
        request: nas20170626_models.AddClientToBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.AddClientToBlackListResponse:
        """
        @deprecated OpenAPI AddClientToBlackList is deprecated
        
        @summary Adds a client to the blacklist of a Cloud Parallel File Storage (CPFS) file system and revokes the write access from the client. The blacklist serves as an I/O fence.
        
        @description The API operation is available only for CPFS file systems.
        
        @param request: AddClientToBlackListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddClientToBlackListResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddClientToBlackList',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.AddClientToBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_client_to_black_list(
        self,
        request: nas20170626_models.AddClientToBlackListRequest,
    ) -> nas20170626_models.AddClientToBlackListResponse:
        """
        @deprecated OpenAPI AddClientToBlackList is deprecated
        
        @summary Adds a client to the blacklist of a Cloud Parallel File Storage (CPFS) file system and revokes the write access from the client. The blacklist serves as an I/O fence.
        
        @description The API operation is available only for CPFS file systems.
        
        @param request: AddClientToBlackListRequest
        @return: AddClientToBlackListResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.add_client_to_black_list_with_options(request, runtime)

    async def add_client_to_black_list_async(
        self,
        request: nas20170626_models.AddClientToBlackListRequest,
    ) -> nas20170626_models.AddClientToBlackListResponse:
        """
        @deprecated OpenAPI AddClientToBlackList is deprecated
        
        @summary Adds a client to the blacklist of a Cloud Parallel File Storage (CPFS) file system and revokes the write access from the client. The blacklist serves as an I/O fence.
        
        @description The API operation is available only for CPFS file systems.
        
        @param request: AddClientToBlackListRequest
        @return: AddClientToBlackListResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_client_to_black_list_with_options_async(request, runtime)

    def apply_auto_snapshot_policy_with_options(
        self,
        request: nas20170626_models.ApplyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ApplyAutoSnapshotPolicyResponse:
        """
        @summary Applies an automatic snapshot policy to one or more file systems.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        You can apply only one automatic snapshot policy to each file system.
        Each automatic snapshot policy can be applied to multiple file systems.
        If an automatic snapshot policy is applied to a file system, you can call the ApplyAutoSnapshotPolicy operation to change the automatic snapshot policy.
        
        @param request: ApplyAutoSnapshotPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ApplyAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.ApplyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ApplyAutoSnapshotPolicyResponse:
        """
        @summary Applies an automatic snapshot policy to one or more file systems.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        You can apply only one automatic snapshot policy to each file system.
        Each automatic snapshot policy can be applied to multiple file systems.
        If an automatic snapshot policy is applied to a file system, you can call the ApplyAutoSnapshotPolicy operation to change the automatic snapshot policy.
        
        @param request: ApplyAutoSnapshotPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ApplyAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_auto_snapshot_policy(
        self,
        request: nas20170626_models.ApplyAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.ApplyAutoSnapshotPolicyResponse:
        """
        @summary Applies an automatic snapshot policy to one or more file systems.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        You can apply only one automatic snapshot policy to each file system.
        Each automatic snapshot policy can be applied to multiple file systems.
        If an automatic snapshot policy is applied to a file system, you can call the ApplyAutoSnapshotPolicy operation to change the automatic snapshot policy.
        
        @param request: ApplyAutoSnapshotPolicyRequest
        @return: ApplyAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_auto_snapshot_policy_with_options(request, runtime)

    async def apply_auto_snapshot_policy_async(
        self,
        request: nas20170626_models.ApplyAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.ApplyAutoSnapshotPolicyResponse:
        """
        @summary Applies an automatic snapshot policy to one or more file systems.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        You can apply only one automatic snapshot policy to each file system.
        Each automatic snapshot policy can be applied to multiple file systems.
        If an automatic snapshot policy is applied to a file system, you can call the ApplyAutoSnapshotPolicy operation to change the automatic snapshot policy.
        
        @param request: ApplyAutoSnapshotPolicyRequest
        @return: ApplyAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_auto_snapshot_policy_with_options_async(request, runtime)

    def apply_data_flow_auto_refresh_with_options(
        self,
        request: nas20170626_models.ApplyDataFlowAutoRefreshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ApplyDataFlowAutoRefreshResponse:
        """
        @summary Adds AutoRefresh configurations to a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can add AutoRefresh configurations only to the dataflows that are in the `Running` state.
        You can add a maximum of five AutoRefresh configurations to a dataflow.
        It generally takes 2 to 5 minutes to create an AutoRefresh configuration. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the dataflow status.
        AutoRefresh depends on the object modification events collected by EventBridge from the source Object Storage Service (OSS) bucket. You must first [activate EventBridge](https://help.aliyun.com/document_detail/182246.html).
        > The event buses and event rules created for CPFS in the EventBridge console contain the `Create for cpfs auto refresh` description. The event buses and event rules cannot be modified or deleted. Otherwise, AutoRefresh cannot work properly.
        The AutoRefresh configuration applies only to the prefix and is specified by the RefreshPath parameter. When you add an AutoRefresh configuration to the prefix for a CPFS dataflow, an event bus is created at the user side and an event rule is created for the prefix of the source OSS bucket. When an object is modified in the prefix of the source OSS bucket, an OSS event is generated in the EventBridge console. The event is processed by the CPFS dataflow.
        After AutoRefresh is configured, if the data in the source OSS bucket is updated, the updated metadata is automatically synchronized to the CPFS file system. You can load the updated data when you access files, or run a dataflow task to load the updated data.
        AutoRefreshInterval refers to the interval at which CPFS checks whether data is updated in the prefix of the source OSS bucket. If data is updated, CPFS runs an AutoRefresh task. If the frequency of triggering the object modification event in the source OSS bucket exceeds the processing capability of the CPFS dataflow, AutoRefresh tasks are accumulated, metadata updates are delayed, and the dataflow status becomes Misconfigured. To resolve these issues, you can increase the dataflow specifications or reduce the frequency of triggering the object modification event.
        
        @param request: ApplyDataFlowAutoRefreshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyDataFlowAutoRefreshResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not UtilClient.is_unset(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not UtilClient.is_unset(request.auto_refreshs):
            query['AutoRefreshs'] = request.auto_refreshs
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyDataFlowAutoRefresh',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ApplyDataFlowAutoRefreshResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_data_flow_auto_refresh_with_options_async(
        self,
        request: nas20170626_models.ApplyDataFlowAutoRefreshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ApplyDataFlowAutoRefreshResponse:
        """
        @summary Adds AutoRefresh configurations to a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can add AutoRefresh configurations only to the dataflows that are in the `Running` state.
        You can add a maximum of five AutoRefresh configurations to a dataflow.
        It generally takes 2 to 5 minutes to create an AutoRefresh configuration. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the dataflow status.
        AutoRefresh depends on the object modification events collected by EventBridge from the source Object Storage Service (OSS) bucket. You must first [activate EventBridge](https://help.aliyun.com/document_detail/182246.html).
        > The event buses and event rules created for CPFS in the EventBridge console contain the `Create for cpfs auto refresh` description. The event buses and event rules cannot be modified or deleted. Otherwise, AutoRefresh cannot work properly.
        The AutoRefresh configuration applies only to the prefix and is specified by the RefreshPath parameter. When you add an AutoRefresh configuration to the prefix for a CPFS dataflow, an event bus is created at the user side and an event rule is created for the prefix of the source OSS bucket. When an object is modified in the prefix of the source OSS bucket, an OSS event is generated in the EventBridge console. The event is processed by the CPFS dataflow.
        After AutoRefresh is configured, if the data in the source OSS bucket is updated, the updated metadata is automatically synchronized to the CPFS file system. You can load the updated data when you access files, or run a dataflow task to load the updated data.
        AutoRefreshInterval refers to the interval at which CPFS checks whether data is updated in the prefix of the source OSS bucket. If data is updated, CPFS runs an AutoRefresh task. If the frequency of triggering the object modification event in the source OSS bucket exceeds the processing capability of the CPFS dataflow, AutoRefresh tasks are accumulated, metadata updates are delayed, and the dataflow status becomes Misconfigured. To resolve these issues, you can increase the dataflow specifications or reduce the frequency of triggering the object modification event.
        
        @param request: ApplyDataFlowAutoRefreshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyDataFlowAutoRefreshResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not UtilClient.is_unset(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not UtilClient.is_unset(request.auto_refreshs):
            query['AutoRefreshs'] = request.auto_refreshs
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyDataFlowAutoRefresh',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ApplyDataFlowAutoRefreshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_data_flow_auto_refresh(
        self,
        request: nas20170626_models.ApplyDataFlowAutoRefreshRequest,
    ) -> nas20170626_models.ApplyDataFlowAutoRefreshResponse:
        """
        @summary Adds AutoRefresh configurations to a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can add AutoRefresh configurations only to the dataflows that are in the `Running` state.
        You can add a maximum of five AutoRefresh configurations to a dataflow.
        It generally takes 2 to 5 minutes to create an AutoRefresh configuration. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the dataflow status.
        AutoRefresh depends on the object modification events collected by EventBridge from the source Object Storage Service (OSS) bucket. You must first [activate EventBridge](https://help.aliyun.com/document_detail/182246.html).
        > The event buses and event rules created for CPFS in the EventBridge console contain the `Create for cpfs auto refresh` description. The event buses and event rules cannot be modified or deleted. Otherwise, AutoRefresh cannot work properly.
        The AutoRefresh configuration applies only to the prefix and is specified by the RefreshPath parameter. When you add an AutoRefresh configuration to the prefix for a CPFS dataflow, an event bus is created at the user side and an event rule is created for the prefix of the source OSS bucket. When an object is modified in the prefix of the source OSS bucket, an OSS event is generated in the EventBridge console. The event is processed by the CPFS dataflow.
        After AutoRefresh is configured, if the data in the source OSS bucket is updated, the updated metadata is automatically synchronized to the CPFS file system. You can load the updated data when you access files, or run a dataflow task to load the updated data.
        AutoRefreshInterval refers to the interval at which CPFS checks whether data is updated in the prefix of the source OSS bucket. If data is updated, CPFS runs an AutoRefresh task. If the frequency of triggering the object modification event in the source OSS bucket exceeds the processing capability of the CPFS dataflow, AutoRefresh tasks are accumulated, metadata updates are delayed, and the dataflow status becomes Misconfigured. To resolve these issues, you can increase the dataflow specifications or reduce the frequency of triggering the object modification event.
        
        @param request: ApplyDataFlowAutoRefreshRequest
        @return: ApplyDataFlowAutoRefreshResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_data_flow_auto_refresh_with_options(request, runtime)

    async def apply_data_flow_auto_refresh_async(
        self,
        request: nas20170626_models.ApplyDataFlowAutoRefreshRequest,
    ) -> nas20170626_models.ApplyDataFlowAutoRefreshResponse:
        """
        @summary Adds AutoRefresh configurations to a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can add AutoRefresh configurations only to the dataflows that are in the `Running` state.
        You can add a maximum of five AutoRefresh configurations to a dataflow.
        It generally takes 2 to 5 minutes to create an AutoRefresh configuration. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the dataflow status.
        AutoRefresh depends on the object modification events collected by EventBridge from the source Object Storage Service (OSS) bucket. You must first [activate EventBridge](https://help.aliyun.com/document_detail/182246.html).
        > The event buses and event rules created for CPFS in the EventBridge console contain the `Create for cpfs auto refresh` description. The event buses and event rules cannot be modified or deleted. Otherwise, AutoRefresh cannot work properly.
        The AutoRefresh configuration applies only to the prefix and is specified by the RefreshPath parameter. When you add an AutoRefresh configuration to the prefix for a CPFS dataflow, an event bus is created at the user side and an event rule is created for the prefix of the source OSS bucket. When an object is modified in the prefix of the source OSS bucket, an OSS event is generated in the EventBridge console. The event is processed by the CPFS dataflow.
        After AutoRefresh is configured, if the data in the source OSS bucket is updated, the updated metadata is automatically synchronized to the CPFS file system. You can load the updated data when you access files, or run a dataflow task to load the updated data.
        AutoRefreshInterval refers to the interval at which CPFS checks whether data is updated in the prefix of the source OSS bucket. If data is updated, CPFS runs an AutoRefresh task. If the frequency of triggering the object modification event in the source OSS bucket exceeds the processing capability of the CPFS dataflow, AutoRefresh tasks are accumulated, metadata updates are delayed, and the dataflow status becomes Misconfigured. To resolve these issues, you can increase the dataflow specifications or reduce the frequency of triggering the object modification event.
        
        @param request: ApplyDataFlowAutoRefreshRequest
        @return: ApplyDataFlowAutoRefreshResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_data_flow_auto_refresh_with_options_async(request, runtime)

    def cancel_auto_snapshot_policy_with_options(
        self,
        request: nas20170626_models.CancelAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelAutoSnapshotPolicyResponse:
        """
        @summary Removes automatic snapshot policies from one or more file systems.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: CancelAutoSnapshotPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.CancelAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelAutoSnapshotPolicyResponse:
        """
        @summary Removes automatic snapshot policies from one or more file systems.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: CancelAutoSnapshotPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_auto_snapshot_policy(
        self,
        request: nas20170626_models.CancelAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.CancelAutoSnapshotPolicyResponse:
        """
        @summary Removes automatic snapshot policies from one or more file systems.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: CancelAutoSnapshotPolicyRequest
        @return: CancelAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_auto_snapshot_policy_with_options(request, runtime)

    async def cancel_auto_snapshot_policy_async(
        self,
        request: nas20170626_models.CancelAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.CancelAutoSnapshotPolicyResponse:
        """
        @summary Removes automatic snapshot policies from one or more file systems.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: CancelAutoSnapshotPolicyRequest
        @return: CancelAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_auto_snapshot_policy_with_options_async(request, runtime)

    def cancel_data_flow_auto_refresh_with_options(
        self,
        request: nas20170626_models.CancelDataFlowAutoRefreshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelDataFlowAutoRefreshResponse:
        """
        @summary Cancels the AutoRefresh configuration for a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can cancel AutoRefresh configurations only for the dataflows that are in the `Running` or `Stopped` state.
        It generally takes 2 to 5 minutes to cancel the AutoRefresh configurations. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the status of the AutoRefresh tasks.
        
        @param request: CancelDataFlowAutoRefreshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelDataFlowAutoRefreshResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.refresh_path):
            query['RefreshPath'] = request.refresh_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDataFlowAutoRefresh',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDataFlowAutoRefreshResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_data_flow_auto_refresh_with_options_async(
        self,
        request: nas20170626_models.CancelDataFlowAutoRefreshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelDataFlowAutoRefreshResponse:
        """
        @summary Cancels the AutoRefresh configuration for a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can cancel AutoRefresh configurations only for the dataflows that are in the `Running` or `Stopped` state.
        It generally takes 2 to 5 minutes to cancel the AutoRefresh configurations. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the status of the AutoRefresh tasks.
        
        @param request: CancelDataFlowAutoRefreshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelDataFlowAutoRefreshResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.refresh_path):
            query['RefreshPath'] = request.refresh_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDataFlowAutoRefresh',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDataFlowAutoRefreshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_data_flow_auto_refresh(
        self,
        request: nas20170626_models.CancelDataFlowAutoRefreshRequest,
    ) -> nas20170626_models.CancelDataFlowAutoRefreshResponse:
        """
        @summary Cancels the AutoRefresh configuration for a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can cancel AutoRefresh configurations only for the dataflows that are in the `Running` or `Stopped` state.
        It generally takes 2 to 5 minutes to cancel the AutoRefresh configurations. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the status of the AutoRefresh tasks.
        
        @param request: CancelDataFlowAutoRefreshRequest
        @return: CancelDataFlowAutoRefreshResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_data_flow_auto_refresh_with_options(request, runtime)

    async def cancel_data_flow_auto_refresh_async(
        self,
        request: nas20170626_models.CancelDataFlowAutoRefreshRequest,
    ) -> nas20170626_models.CancelDataFlowAutoRefreshResponse:
        """
        @summary Cancels the AutoRefresh configuration for a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can cancel AutoRefresh configurations only for the dataflows that are in the `Running` or `Stopped` state.
        It generally takes 2 to 5 minutes to cancel the AutoRefresh configurations. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the status of the AutoRefresh tasks.
        
        @param request: CancelDataFlowAutoRefreshRequest
        @return: CancelDataFlowAutoRefreshResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_data_flow_auto_refresh_with_options_async(request, runtime)

    def cancel_data_flow_sub_task_with_options(
        self,
        request: nas20170626_models.CancelDataFlowSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelDataFlowSubTaskResponse:
        """
        @summary Cancels a data streaming task.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.6.0 and later support this operation. You can view the version information on the file system details page in the console.
        You can cancel a data streaming task only when the task is in the CREATED or RUNNING state.
        Data streaming tasks are executed asynchronously. You can call the DescribeDataFlowSubTasks operation to query the task execution status.
        
        @param request: CancelDataFlowSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelDataFlowSubTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.data_flow_sub_task_id):
            query['DataFlowSubTaskId'] = request.data_flow_sub_task_id
        if not UtilClient.is_unset(request.data_flow_task_id):
            query['DataFlowTaskId'] = request.data_flow_task_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDataFlowSubTask',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDataFlowSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_data_flow_sub_task_with_options_async(
        self,
        request: nas20170626_models.CancelDataFlowSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelDataFlowSubTaskResponse:
        """
        @summary Cancels a data streaming task.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.6.0 and later support this operation. You can view the version information on the file system details page in the console.
        You can cancel a data streaming task only when the task is in the CREATED or RUNNING state.
        Data streaming tasks are executed asynchronously. You can call the DescribeDataFlowSubTasks operation to query the task execution status.
        
        @param request: CancelDataFlowSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelDataFlowSubTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.data_flow_sub_task_id):
            query['DataFlowSubTaskId'] = request.data_flow_sub_task_id
        if not UtilClient.is_unset(request.data_flow_task_id):
            query['DataFlowTaskId'] = request.data_flow_task_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDataFlowSubTask',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDataFlowSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_data_flow_sub_task(
        self,
        request: nas20170626_models.CancelDataFlowSubTaskRequest,
    ) -> nas20170626_models.CancelDataFlowSubTaskResponse:
        """
        @summary Cancels a data streaming task.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.6.0 and later support this operation. You can view the version information on the file system details page in the console.
        You can cancel a data streaming task only when the task is in the CREATED or RUNNING state.
        Data streaming tasks are executed asynchronously. You can call the DescribeDataFlowSubTasks operation to query the task execution status.
        
        @param request: CancelDataFlowSubTaskRequest
        @return: CancelDataFlowSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_data_flow_sub_task_with_options(request, runtime)

    async def cancel_data_flow_sub_task_async(
        self,
        request: nas20170626_models.CancelDataFlowSubTaskRequest,
    ) -> nas20170626_models.CancelDataFlowSubTaskResponse:
        """
        @summary Cancels a data streaming task.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.6.0 and later support this operation. You can view the version information on the file system details page in the console.
        You can cancel a data streaming task only when the task is in the CREATED or RUNNING state.
        Data streaming tasks are executed asynchronously. You can call the DescribeDataFlowSubTasks operation to query the task execution status.
        
        @param request: CancelDataFlowSubTaskRequest
        @return: CancelDataFlowSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_data_flow_sub_task_with_options_async(request, runtime)

    def cancel_data_flow_task_with_options(
        self,
        request: nas20170626_models.CancelDataFlowTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelDataFlowTaskResponse:
        """
        @summary Cancels a dataflow task that is not running.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flow tasks. You can view the version information on the file system details page in the console.
        You can cancel only the data flow tasks that are in the `Pending` and `Executing` states.
        It generally takes 5 to 10 minutes to cancel a data flow task. You can query the task execution status by calling the [DescribeDataFlowTasks](https://help.aliyun.com/document_detail/2838089.html) operation.
        
        @param request: CancelDataFlowTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelDataFlowTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDataFlowTask',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDataFlowTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_data_flow_task_with_options_async(
        self,
        request: nas20170626_models.CancelDataFlowTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelDataFlowTaskResponse:
        """
        @summary Cancels a dataflow task that is not running.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flow tasks. You can view the version information on the file system details page in the console.
        You can cancel only the data flow tasks that are in the `Pending` and `Executing` states.
        It generally takes 5 to 10 minutes to cancel a data flow task. You can query the task execution status by calling the [DescribeDataFlowTasks](https://help.aliyun.com/document_detail/2838089.html) operation.
        
        @param request: CancelDataFlowTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelDataFlowTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDataFlowTask',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDataFlowTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_data_flow_task(
        self,
        request: nas20170626_models.CancelDataFlowTaskRequest,
    ) -> nas20170626_models.CancelDataFlowTaskResponse:
        """
        @summary Cancels a dataflow task that is not running.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flow tasks. You can view the version information on the file system details page in the console.
        You can cancel only the data flow tasks that are in the `Pending` and `Executing` states.
        It generally takes 5 to 10 minutes to cancel a data flow task. You can query the task execution status by calling the [DescribeDataFlowTasks](https://help.aliyun.com/document_detail/2838089.html) operation.
        
        @param request: CancelDataFlowTaskRequest
        @return: CancelDataFlowTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_data_flow_task_with_options(request, runtime)

    async def cancel_data_flow_task_async(
        self,
        request: nas20170626_models.CancelDataFlowTaskRequest,
    ) -> nas20170626_models.CancelDataFlowTaskResponse:
        """
        @summary Cancels a dataflow task that is not running.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flow tasks. You can view the version information on the file system details page in the console.
        You can cancel only the data flow tasks that are in the `Pending` and `Executing` states.
        It generally takes 5 to 10 minutes to cancel a data flow task. You can query the task execution status by calling the [DescribeDataFlowTasks](https://help.aliyun.com/document_detail/2838089.html) operation.
        
        @param request: CancelDataFlowTaskRequest
        @return: CancelDataFlowTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_data_flow_task_with_options_async(request, runtime)

    def cancel_dir_quota_with_options(
        self,
        request: nas20170626_models.CancelDirQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelDirQuotaResponse:
        """
        @summary Cancels the directory quota of a file system.
        
        @description Only General-purpose file systems support the directory quota feature.
        
        @param request: CancelDirQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelDirQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDirQuota',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDirQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_dir_quota_with_options_async(
        self,
        request: nas20170626_models.CancelDirQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelDirQuotaResponse:
        """
        @summary Cancels the directory quota of a file system.
        
        @description Only General-purpose file systems support the directory quota feature.
        
        @param request: CancelDirQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelDirQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelDirQuota',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelDirQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_dir_quota(
        self,
        request: nas20170626_models.CancelDirQuotaRequest,
    ) -> nas20170626_models.CancelDirQuotaResponse:
        """
        @summary Cancels the directory quota of a file system.
        
        @description Only General-purpose file systems support the directory quota feature.
        
        @param request: CancelDirQuotaRequest
        @return: CancelDirQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_dir_quota_with_options(request, runtime)

    async def cancel_dir_quota_async(
        self,
        request: nas20170626_models.CancelDirQuotaRequest,
    ) -> nas20170626_models.CancelDirQuotaResponse:
        """
        @summary Cancels the directory quota of a file system.
        
        @description Only General-purpose file systems support the directory quota feature.
        
        @param request: CancelDirQuotaRequest
        @return: CancelDirQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_dir_quota_with_options_async(request, runtime)

    def cancel_fileset_quota_with_options(
        self,
        request: nas20170626_models.CancelFilesetQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelFilesetQuotaResponse:
        """
        @summary Cancels the quota set for a fileset.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation.
        
        @param request: CancelFilesetQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelFilesetQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelFilesetQuota',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelFilesetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_fileset_quota_with_options_async(
        self,
        request: nas20170626_models.CancelFilesetQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelFilesetQuotaResponse:
        """
        @summary Cancels the quota set for a fileset.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation.
        
        @param request: CancelFilesetQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelFilesetQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelFilesetQuota',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelFilesetQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_fileset_quota(
        self,
        request: nas20170626_models.CancelFilesetQuotaRequest,
    ) -> nas20170626_models.CancelFilesetQuotaResponse:
        """
        @summary Cancels the quota set for a fileset.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation.
        
        @param request: CancelFilesetQuotaRequest
        @return: CancelFilesetQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_fileset_quota_with_options(request, runtime)

    async def cancel_fileset_quota_async(
        self,
        request: nas20170626_models.CancelFilesetQuotaRequest,
    ) -> nas20170626_models.CancelFilesetQuotaResponse:
        """
        @summary Cancels the quota set for a fileset.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation.
        
        @param request: CancelFilesetQuotaRequest
        @return: CancelFilesetQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_fileset_quota_with_options_async(request, runtime)

    def cancel_lifecycle_retrieve_job_with_options(
        self,
        request: nas20170626_models.CancelLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelLifecycleRetrieveJobResponse:
        """
        @summary Cancels a running data retrieval task.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: CancelLifecycleRetrieveJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelLifecycleRetrieveJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelLifecycleRetrieveJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_lifecycle_retrieve_job_with_options_async(
        self,
        request: nas20170626_models.CancelLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelLifecycleRetrieveJobResponse:
        """
        @summary Cancels a running data retrieval task.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: CancelLifecycleRetrieveJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelLifecycleRetrieveJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelLifecycleRetrieveJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_lifecycle_retrieve_job(
        self,
        request: nas20170626_models.CancelLifecycleRetrieveJobRequest,
    ) -> nas20170626_models.CancelLifecycleRetrieveJobResponse:
        """
        @summary Cancels a running data retrieval task.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: CancelLifecycleRetrieveJobRequest
        @return: CancelLifecycleRetrieveJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_lifecycle_retrieve_job_with_options(request, runtime)

    async def cancel_lifecycle_retrieve_job_async(
        self,
        request: nas20170626_models.CancelLifecycleRetrieveJobRequest,
    ) -> nas20170626_models.CancelLifecycleRetrieveJobResponse:
        """
        @summary Cancels a running data retrieval task.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: CancelLifecycleRetrieveJobRequest
        @return: CancelLifecycleRetrieveJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_lifecycle_retrieve_job_with_options_async(request, runtime)

    def cancel_recycle_bin_job_with_options(
        self,
        request: nas20170626_models.CancelRecycleBinJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelRecycleBinJobResponse:
        """
        @summary Cancels a running job of the recycle bin.
        
        @description    Only General-purpose NAS file systems support this operation.
        You can cancel only jobs that are in the Running state. You cannot cancel jobs that are in the PartialSuccess, Success, Fail, or Cancelled state.
        If you cancel a running job that permanently deletes files, you cannot restore the files that are already permanently deleted.
        If you cancel a running job that restores files, you can query the restored files from the file system, and query the unrestored files from the recycle bin.
        
        @param request: CancelRecycleBinJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelRecycleBinJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelRecycleBinJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelRecycleBinJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_recycle_bin_job_with_options_async(
        self,
        request: nas20170626_models.CancelRecycleBinJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CancelRecycleBinJobResponse:
        """
        @summary Cancels a running job of the recycle bin.
        
        @description    Only General-purpose NAS file systems support this operation.
        You can cancel only jobs that are in the Running state. You cannot cancel jobs that are in the PartialSuccess, Success, Fail, or Cancelled state.
        If you cancel a running job that permanently deletes files, you cannot restore the files that are already permanently deleted.
        If you cancel a running job that restores files, you can query the restored files from the file system, and query the unrestored files from the recycle bin.
        
        @param request: CancelRecycleBinJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelRecycleBinJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelRecycleBinJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CancelRecycleBinJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_recycle_bin_job(
        self,
        request: nas20170626_models.CancelRecycleBinJobRequest,
    ) -> nas20170626_models.CancelRecycleBinJobResponse:
        """
        @summary Cancels a running job of the recycle bin.
        
        @description    Only General-purpose NAS file systems support this operation.
        You can cancel only jobs that are in the Running state. You cannot cancel jobs that are in the PartialSuccess, Success, Fail, or Cancelled state.
        If you cancel a running job that permanently deletes files, you cannot restore the files that are already permanently deleted.
        If you cancel a running job that restores files, you can query the restored files from the file system, and query the unrestored files from the recycle bin.
        
        @param request: CancelRecycleBinJobRequest
        @return: CancelRecycleBinJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_recycle_bin_job_with_options(request, runtime)

    async def cancel_recycle_bin_job_async(
        self,
        request: nas20170626_models.CancelRecycleBinJobRequest,
    ) -> nas20170626_models.CancelRecycleBinJobResponse:
        """
        @summary Cancels a running job of the recycle bin.
        
        @description    Only General-purpose NAS file systems support this operation.
        You can cancel only jobs that are in the Running state. You cannot cancel jobs that are in the PartialSuccess, Success, Fail, or Cancelled state.
        If you cancel a running job that permanently deletes files, you cannot restore the files that are already permanently deleted.
        If you cancel a running job that restores files, you can query the restored files from the file system, and query the unrestored files from the recycle bin.
        
        @param request: CancelRecycleBinJobRequest
        @return: CancelRecycleBinJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_recycle_bin_job_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: nas20170626_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a file system belongs.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: nas20170626_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a file system belongs.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: nas20170626_models.ChangeResourceGroupRequest,
    ) -> nas20170626_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a file system belongs.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: nas20170626_models.ChangeResourceGroupRequest,
    ) -> nas20170626_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a file system belongs.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_access_group_with_options(
        self,
        request: nas20170626_models.CreateAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAccessGroupResponse:
        """
        @summary Creates a permission group.
        
        @param request: CreateAccessGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccessGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.access_group_type):
            query['AccessGroupType'] = request.access_group_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_group_with_options_async(
        self,
        request: nas20170626_models.CreateAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAccessGroupResponse:
        """
        @summary Creates a permission group.
        
        @param request: CreateAccessGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccessGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.access_group_type):
            query['AccessGroupType'] = request.access_group_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_group(
        self,
        request: nas20170626_models.CreateAccessGroupRequest,
    ) -> nas20170626_models.CreateAccessGroupResponse:
        """
        @summary Creates a permission group.
        
        @param request: CreateAccessGroupRequest
        @return: CreateAccessGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_access_group_with_options(request, runtime)

    async def create_access_group_async(
        self,
        request: nas20170626_models.CreateAccessGroupRequest,
    ) -> nas20170626_models.CreateAccessGroupResponse:
        """
        @summary Creates a permission group.
        
        @param request: CreateAccessGroupRequest
        @return: CreateAccessGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_access_group_with_options_async(request, runtime)

    def create_access_point_with_options(
        self,
        request: nas20170626_models.CreateAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAccessPointResponse:
        """
        @summary Creates an access point.
        
        @description    After you call the CreateAccessPoint operation, an access point is not immediately created. Therefore, after you call the CreateAccessPoint operation successfully, call the [DescribeAccessPoints](https://help.aliyun.com/document_detail/2712239.html) or [DescribeAccessPoint](https://help.aliyun.com/document_detail/2712240.html) operation to query the status of the access point. If the status is **Active**, mount the file system. Otherwise, the file system may fail to be mounted.
        Only General-purpose Network File System (NFS) file systems support access points.
        If you want to call the EnabledRam operation to enable a Resource Access Management (RAM) policy, you must configure the corresponding RAM permissions. For more information, see [Manage endpoints](https://help.aliyun.com/document_detail/2545998.html).
        
        @param request: CreateAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group):
            query['AccessGroup'] = request.access_group
        if not UtilClient.is_unset(request.access_point_name):
            query['AccessPointName'] = request.access_point_name
        if not UtilClient.is_unset(request.enabled_ram):
            query['EnabledRam'] = request.enabled_ram
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.owner_group_id):
            query['OwnerGroupId'] = request.owner_group_id
        if not UtilClient.is_unset(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.permission):
            query['Permission'] = request.permission
        if not UtilClient.is_unset(request.posix_group_id):
            query['PosixGroupId'] = request.posix_group_id
        if not UtilClient.is_unset(request.posix_secondary_group_ids):
            query['PosixSecondaryGroupIds'] = request.posix_secondary_group_ids
        if not UtilClient.is_unset(request.posix_user_id):
            query['PosixUserId'] = request.posix_user_id
        if not UtilClient.is_unset(request.root_directory):
            query['RootDirectory'] = request.root_directory
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vsw_id):
            query['VswId'] = request.vsw_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessPoint',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_point_with_options_async(
        self,
        request: nas20170626_models.CreateAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAccessPointResponse:
        """
        @summary Creates an access point.
        
        @description    After you call the CreateAccessPoint operation, an access point is not immediately created. Therefore, after you call the CreateAccessPoint operation successfully, call the [DescribeAccessPoints](https://help.aliyun.com/document_detail/2712239.html) or [DescribeAccessPoint](https://help.aliyun.com/document_detail/2712240.html) operation to query the status of the access point. If the status is **Active**, mount the file system. Otherwise, the file system may fail to be mounted.
        Only General-purpose Network File System (NFS) file systems support access points.
        If you want to call the EnabledRam operation to enable a Resource Access Management (RAM) policy, you must configure the corresponding RAM permissions. For more information, see [Manage endpoints](https://help.aliyun.com/document_detail/2545998.html).
        
        @param request: CreateAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group):
            query['AccessGroup'] = request.access_group
        if not UtilClient.is_unset(request.access_point_name):
            query['AccessPointName'] = request.access_point_name
        if not UtilClient.is_unset(request.enabled_ram):
            query['EnabledRam'] = request.enabled_ram
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.owner_group_id):
            query['OwnerGroupId'] = request.owner_group_id
        if not UtilClient.is_unset(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.permission):
            query['Permission'] = request.permission
        if not UtilClient.is_unset(request.posix_group_id):
            query['PosixGroupId'] = request.posix_group_id
        if not UtilClient.is_unset(request.posix_secondary_group_ids):
            query['PosixSecondaryGroupIds'] = request.posix_secondary_group_ids
        if not UtilClient.is_unset(request.posix_user_id):
            query['PosixUserId'] = request.posix_user_id
        if not UtilClient.is_unset(request.root_directory):
            query['RootDirectory'] = request.root_directory
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vsw_id):
            query['VswId'] = request.vsw_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessPoint',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_point(
        self,
        request: nas20170626_models.CreateAccessPointRequest,
    ) -> nas20170626_models.CreateAccessPointResponse:
        """
        @summary Creates an access point.
        
        @description    After you call the CreateAccessPoint operation, an access point is not immediately created. Therefore, after you call the CreateAccessPoint operation successfully, call the [DescribeAccessPoints](https://help.aliyun.com/document_detail/2712239.html) or [DescribeAccessPoint](https://help.aliyun.com/document_detail/2712240.html) operation to query the status of the access point. If the status is **Active**, mount the file system. Otherwise, the file system may fail to be mounted.
        Only General-purpose Network File System (NFS) file systems support access points.
        If you want to call the EnabledRam operation to enable a Resource Access Management (RAM) policy, you must configure the corresponding RAM permissions. For more information, see [Manage endpoints](https://help.aliyun.com/document_detail/2545998.html).
        
        @param request: CreateAccessPointRequest
        @return: CreateAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_access_point_with_options(request, runtime)

    async def create_access_point_async(
        self,
        request: nas20170626_models.CreateAccessPointRequest,
    ) -> nas20170626_models.CreateAccessPointResponse:
        """
        @summary Creates an access point.
        
        @description    After you call the CreateAccessPoint operation, an access point is not immediately created. Therefore, after you call the CreateAccessPoint operation successfully, call the [DescribeAccessPoints](https://help.aliyun.com/document_detail/2712239.html) or [DescribeAccessPoint](https://help.aliyun.com/document_detail/2712240.html) operation to query the status of the access point. If the status is **Active**, mount the file system. Otherwise, the file system may fail to be mounted.
        Only General-purpose Network File System (NFS) file systems support access points.
        If you want to call the EnabledRam operation to enable a Resource Access Management (RAM) policy, you must configure the corresponding RAM permissions. For more information, see [Manage endpoints](https://help.aliyun.com/document_detail/2545998.html).
        
        @param request: CreateAccessPointRequest
        @return: CreateAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_access_point_with_options_async(request, runtime)

    def create_access_rule_with_options(
        self,
        request: nas20170626_models.CreateAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAccessRuleResponse:
        """
        @summary Creates a rule for a permission group.
        
        @param request: CreateAccessRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccessRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.user_access_type):
            query['UserAccessType'] = request.user_access_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_access_rule_with_options_async(
        self,
        request: nas20170626_models.CreateAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAccessRuleResponse:
        """
        @summary Creates a rule for a permission group.
        
        @param request: CreateAccessRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccessRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.user_access_type):
            query['UserAccessType'] = request.user_access_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_access_rule(
        self,
        request: nas20170626_models.CreateAccessRuleRequest,
    ) -> nas20170626_models.CreateAccessRuleResponse:
        """
        @summary Creates a rule for a permission group.
        
        @param request: CreateAccessRuleRequest
        @return: CreateAccessRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_access_rule_with_options(request, runtime)

    async def create_access_rule_async(
        self,
        request: nas20170626_models.CreateAccessRuleRequest,
    ) -> nas20170626_models.CreateAccessRuleResponse:
        """
        @summary Creates a rule for a permission group.
        
        @param request: CreateAccessRuleRequest
        @return: CreateAccessRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_access_rule_with_options_async(request, runtime)

    def create_auto_snapshot_policy_with_options(
        self,
        request: nas20170626_models.CreateAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAutoSnapshotPolicyResponse:
        """
        @summary Creates an automatic snapshot policy.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        You can create a maximum of 100 automatic snapshot policies in each region for an Alibaba Cloud account.
        If an auto snapshot is being created when the scheduled time for a new auto snapshot arrives, the creation of the new snapshot is skipped. This occurs if the file system stores a large volume of data. For example, you have scheduled auto snapshots to be created at 09:00:00, 10:00:00, 11:00:00, and 12:00:00 for a file system. The system starts to create an auto snapshot at 09:00:00 and does not complete the process until 10:20:00. The process takes 80 minutes because the file system has a large volume of data. In this case, the system does not create an auto snapshot at 10:00:00, but creates an auto snapshot at 11:00:00.
        A maximum of 128 auto snapshots can be created for a file system. If the upper limit is reached, the earliest auto snapshot is deleted. This rule does not apply to manual snapshots.
        If you modify the retention period of an automatic snapshot policy, the modification applies only to subsequent snapshots, but not to the existing snapshots.
        If an auto snapshot is being created for a file system, you cannot create a manual snapshot for the file system. You must wait after the auto snapshot is created.
        You can only apply automatic snapshot policies to a file system that is in the Running state.
        All auto snapshots are named in the `auto_yyyyMMdd_X` format, where: `auto` indicates that the snapshot is created based on an automatic snapshot policy. `yyyyMMdd` indicates the date on which the snapshot is created. `y` indicates the year. `M` indicates the month. `d` indicates the day. `X` indicates the ordinal number of the snapshot on the current day. For example, `auto_20201018_1` indicates the first auto snapshot that was created on October 18, 2020.
        After an automatic snapshot policy is created, you can call the ApplyAutoSnapshotPolicy operation to apply the policy to a file system and call the ModifyAutoSnapshotPolicy operation to modify the policy.
        
        @param request: CreateAutoSnapshotPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_name):
            query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.repeat_weekdays):
            query['RepeatWeekdays'] = request.repeat_weekdays
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.time_points):
            query['TimePoints'] = request.time_points
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.CreateAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateAutoSnapshotPolicyResponse:
        """
        @summary Creates an automatic snapshot policy.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        You can create a maximum of 100 automatic snapshot policies in each region for an Alibaba Cloud account.
        If an auto snapshot is being created when the scheduled time for a new auto snapshot arrives, the creation of the new snapshot is skipped. This occurs if the file system stores a large volume of data. For example, you have scheduled auto snapshots to be created at 09:00:00, 10:00:00, 11:00:00, and 12:00:00 for a file system. The system starts to create an auto snapshot at 09:00:00 and does not complete the process until 10:20:00. The process takes 80 minutes because the file system has a large volume of data. In this case, the system does not create an auto snapshot at 10:00:00, but creates an auto snapshot at 11:00:00.
        A maximum of 128 auto snapshots can be created for a file system. If the upper limit is reached, the earliest auto snapshot is deleted. This rule does not apply to manual snapshots.
        If you modify the retention period of an automatic snapshot policy, the modification applies only to subsequent snapshots, but not to the existing snapshots.
        If an auto snapshot is being created for a file system, you cannot create a manual snapshot for the file system. You must wait after the auto snapshot is created.
        You can only apply automatic snapshot policies to a file system that is in the Running state.
        All auto snapshots are named in the `auto_yyyyMMdd_X` format, where: `auto` indicates that the snapshot is created based on an automatic snapshot policy. `yyyyMMdd` indicates the date on which the snapshot is created. `y` indicates the year. `M` indicates the month. `d` indicates the day. `X` indicates the ordinal number of the snapshot on the current day. For example, `auto_20201018_1` indicates the first auto snapshot that was created on October 18, 2020.
        After an automatic snapshot policy is created, you can call the ApplyAutoSnapshotPolicy operation to apply the policy to a file system and call the ModifyAutoSnapshotPolicy operation to modify the policy.
        
        @param request: CreateAutoSnapshotPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_name):
            query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.repeat_weekdays):
            query['RepeatWeekdays'] = request.repeat_weekdays
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.time_points):
            query['TimePoints'] = request.time_points
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_auto_snapshot_policy(
        self,
        request: nas20170626_models.CreateAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.CreateAutoSnapshotPolicyResponse:
        """
        @summary Creates an automatic snapshot policy.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        You can create a maximum of 100 automatic snapshot policies in each region for an Alibaba Cloud account.
        If an auto snapshot is being created when the scheduled time for a new auto snapshot arrives, the creation of the new snapshot is skipped. This occurs if the file system stores a large volume of data. For example, you have scheduled auto snapshots to be created at 09:00:00, 10:00:00, 11:00:00, and 12:00:00 for a file system. The system starts to create an auto snapshot at 09:00:00 and does not complete the process until 10:20:00. The process takes 80 minutes because the file system has a large volume of data. In this case, the system does not create an auto snapshot at 10:00:00, but creates an auto snapshot at 11:00:00.
        A maximum of 128 auto snapshots can be created for a file system. If the upper limit is reached, the earliest auto snapshot is deleted. This rule does not apply to manual snapshots.
        If you modify the retention period of an automatic snapshot policy, the modification applies only to subsequent snapshots, but not to the existing snapshots.
        If an auto snapshot is being created for a file system, you cannot create a manual snapshot for the file system. You must wait after the auto snapshot is created.
        You can only apply automatic snapshot policies to a file system that is in the Running state.
        All auto snapshots are named in the `auto_yyyyMMdd_X` format, where: `auto` indicates that the snapshot is created based on an automatic snapshot policy. `yyyyMMdd` indicates the date on which the snapshot is created. `y` indicates the year. `M` indicates the month. `d` indicates the day. `X` indicates the ordinal number of the snapshot on the current day. For example, `auto_20201018_1` indicates the first auto snapshot that was created on October 18, 2020.
        After an automatic snapshot policy is created, you can call the ApplyAutoSnapshotPolicy operation to apply the policy to a file system and call the ModifyAutoSnapshotPolicy operation to modify the policy.
        
        @param request: CreateAutoSnapshotPolicyRequest
        @return: CreateAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_auto_snapshot_policy_with_options(request, runtime)

    async def create_auto_snapshot_policy_async(
        self,
        request: nas20170626_models.CreateAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.CreateAutoSnapshotPolicyResponse:
        """
        @summary Creates an automatic snapshot policy.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        You can create a maximum of 100 automatic snapshot policies in each region for an Alibaba Cloud account.
        If an auto snapshot is being created when the scheduled time for a new auto snapshot arrives, the creation of the new snapshot is skipped. This occurs if the file system stores a large volume of data. For example, you have scheduled auto snapshots to be created at 09:00:00, 10:00:00, 11:00:00, and 12:00:00 for a file system. The system starts to create an auto snapshot at 09:00:00 and does not complete the process until 10:20:00. The process takes 80 minutes because the file system has a large volume of data. In this case, the system does not create an auto snapshot at 10:00:00, but creates an auto snapshot at 11:00:00.
        A maximum of 128 auto snapshots can be created for a file system. If the upper limit is reached, the earliest auto snapshot is deleted. This rule does not apply to manual snapshots.
        If you modify the retention period of an automatic snapshot policy, the modification applies only to subsequent snapshots, but not to the existing snapshots.
        If an auto snapshot is being created for a file system, you cannot create a manual snapshot for the file system. You must wait after the auto snapshot is created.
        You can only apply automatic snapshot policies to a file system that is in the Running state.
        All auto snapshots are named in the `auto_yyyyMMdd_X` format, where: `auto` indicates that the snapshot is created based on an automatic snapshot policy. `yyyyMMdd` indicates the date on which the snapshot is created. `y` indicates the year. `M` indicates the month. `d` indicates the day. `X` indicates the ordinal number of the snapshot on the current day. For example, `auto_20201018_1` indicates the first auto snapshot that was created on October 18, 2020.
        After an automatic snapshot policy is created, you can call the ApplyAutoSnapshotPolicy operation to apply the policy to a file system and call the ModifyAutoSnapshotPolicy operation to modify the policy.
        
        @param request: CreateAutoSnapshotPolicyRequest
        @return: CreateAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_auto_snapshot_policy_with_options_async(request, runtime)

    def create_data_flow_with_options(
        self,
        request: nas20170626_models.CreateDataFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateDataFlowResponse:
        """
        @summary Creates a dataflow for a Cloud Parallel File Storage (CPFS) file system and source storage.
        
        @description    Basic operations
        Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flows.
        You can create a data flow only when a CPFS for LINGJUN file system is in the Running state.
        A maximum of 10 data flows can be created for a CPFS for LINGJUN file system.
        It generally takes 2 to 5 minutes to create a data flow. You can call the DescribeDataFlows operation to check whether the data flow has been created.
        Permissions
        When you create a data flow, CPFS for LINGJUN obtains the following two service-linked roles: `AliyunServiceRoleForNasOssDataflow` and `AliyunServiceRoleForNasEventNotification`. For more information, see [CPFS service-linked roles](https://help.aliyun.com/document_detail/2837688.html).
        CPFS for LINGJUN usage notes
        Source storage
        The source storage is an Object Storage Service (OSS) bucket. SourceStorage for a data flow must be an OSS bucket.
        CPFS for LINGJUN data flows support both encrypted and unencrypted access to OSS. If you select SSL-encrypted access to OSS, make sure that encryption in transit for OSS buckets supports encrypted access.
        If data flows for multiple CPFS for LINGJUN file systems or multiple data flows for the same CPFS for LINGJUN file system are stored in the same OSS bucket, you must enable versioning for the OSS bucket to prevent data conflicts caused by data export from multiple CPFS for LINGJUN file systems to one OSS bucket.
        Data flows are not supported for OSS buckets across regions. The OSS bucket must reside in the same region as the CPFS file system.
        CPFS for LINGJUN V2.6.0 and later allow you to create data flows for OSS buckets across accounts.
        The account id parameter is required only when you use OSS buckets across accounts.
        To use OSS buckets across accounts, you must first grant permissions to the related accounts. For more information, see [Cross-account authorization on data flows](https://help.aliyun.com/document_detail/2713462.html).
        >  Before you create a data flow, you must configure a tag (key: cpfs-dataflow, value: true) for the source OSS bucket. This way, the created data flow can access the data in the OSS bucket. When a data flow is being used, do not delete or modify the tag. Otherwise, the data flow for CPFS for LINGJUN cannot access the data in the OSS bucket.
        Limits of data flows on file systems
        You cannot rename a non-empty directory in a path that is associated with a data flow. Otherwise, the Permission Denied error message or an error message indicating that the directory is not empty is returned.
        Proceed with caution when you use special characters in the names of directories and files. The following characters are supported: letters, digits, exclamation points (!), hyphens (-), underscores (_), periods (.), asterisks (\\*), and parentheses (()).
        The path can be up to 1,023 characters in length.
        Limits of data flows on import
        After a symbolic link is imported to CPFS for LINGJUN, the symbolic link is converted into a common data file that contains no symbolic link information.
        If an OSS bucket has multiple versions, only data of the latest version is used.
        The name of a file or a subdirectory can be up to 255 bytes in length.
        Limits of data flows on export
        After a symbolic link is synchronized to OSS, the file that the symbolic link points to is not synchronized to OSS. In this case, the symbolic link is converted into a common object that contains no data.
        Hard links can be synchronized to OSS only as common files that contain no link information.
        After a file of the Socket, Device, or Pipe type is exported to an OSS bucket, the file is converted into a common object that contains no data.
        The directory path can be up to 1,023 characters in length.
        
        @param request: CreateDataFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not UtilClient.is_unset(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not UtilClient.is_unset(request.auto_refreshs):
            query['AutoRefreshs'] = request.auto_refreshs
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_path):
            query['FileSystemPath'] = request.file_system_path
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        if not UtilClient.is_unset(request.source_security_type):
            query['SourceSecurityType'] = request.source_security_type
        if not UtilClient.is_unset(request.source_storage):
            query['SourceStorage'] = request.source_storage
        if not UtilClient.is_unset(request.source_storage_path):
            query['SourceStoragePath'] = request.source_storage_path
        if not UtilClient.is_unset(request.throughput):
            query['Throughput'] = request.throughput
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_flow_with_options_async(
        self,
        request: nas20170626_models.CreateDataFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateDataFlowResponse:
        """
        @summary Creates a dataflow for a Cloud Parallel File Storage (CPFS) file system and source storage.
        
        @description    Basic operations
        Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flows.
        You can create a data flow only when a CPFS for LINGJUN file system is in the Running state.
        A maximum of 10 data flows can be created for a CPFS for LINGJUN file system.
        It generally takes 2 to 5 minutes to create a data flow. You can call the DescribeDataFlows operation to check whether the data flow has been created.
        Permissions
        When you create a data flow, CPFS for LINGJUN obtains the following two service-linked roles: `AliyunServiceRoleForNasOssDataflow` and `AliyunServiceRoleForNasEventNotification`. For more information, see [CPFS service-linked roles](https://help.aliyun.com/document_detail/2837688.html).
        CPFS for LINGJUN usage notes
        Source storage
        The source storage is an Object Storage Service (OSS) bucket. SourceStorage for a data flow must be an OSS bucket.
        CPFS for LINGJUN data flows support both encrypted and unencrypted access to OSS. If you select SSL-encrypted access to OSS, make sure that encryption in transit for OSS buckets supports encrypted access.
        If data flows for multiple CPFS for LINGJUN file systems or multiple data flows for the same CPFS for LINGJUN file system are stored in the same OSS bucket, you must enable versioning for the OSS bucket to prevent data conflicts caused by data export from multiple CPFS for LINGJUN file systems to one OSS bucket.
        Data flows are not supported for OSS buckets across regions. The OSS bucket must reside in the same region as the CPFS file system.
        CPFS for LINGJUN V2.6.0 and later allow you to create data flows for OSS buckets across accounts.
        The account id parameter is required only when you use OSS buckets across accounts.
        To use OSS buckets across accounts, you must first grant permissions to the related accounts. For more information, see [Cross-account authorization on data flows](https://help.aliyun.com/document_detail/2713462.html).
        >  Before you create a data flow, you must configure a tag (key: cpfs-dataflow, value: true) for the source OSS bucket. This way, the created data flow can access the data in the OSS bucket. When a data flow is being used, do not delete or modify the tag. Otherwise, the data flow for CPFS for LINGJUN cannot access the data in the OSS bucket.
        Limits of data flows on file systems
        You cannot rename a non-empty directory in a path that is associated with a data flow. Otherwise, the Permission Denied error message or an error message indicating that the directory is not empty is returned.
        Proceed with caution when you use special characters in the names of directories and files. The following characters are supported: letters, digits, exclamation points (!), hyphens (-), underscores (_), periods (.), asterisks (\\*), and parentheses (()).
        The path can be up to 1,023 characters in length.
        Limits of data flows on import
        After a symbolic link is imported to CPFS for LINGJUN, the symbolic link is converted into a common data file that contains no symbolic link information.
        If an OSS bucket has multiple versions, only data of the latest version is used.
        The name of a file or a subdirectory can be up to 255 bytes in length.
        Limits of data flows on export
        After a symbolic link is synchronized to OSS, the file that the symbolic link points to is not synchronized to OSS. In this case, the symbolic link is converted into a common object that contains no data.
        Hard links can be synchronized to OSS only as common files that contain no link information.
        After a file of the Socket, Device, or Pipe type is exported to an OSS bucket, the file is converted into a common object that contains no data.
        The directory path can be up to 1,023 characters in length.
        
        @param request: CreateDataFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not UtilClient.is_unset(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not UtilClient.is_unset(request.auto_refreshs):
            query['AutoRefreshs'] = request.auto_refreshs
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_path):
            query['FileSystemPath'] = request.file_system_path
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        if not UtilClient.is_unset(request.source_security_type):
            query['SourceSecurityType'] = request.source_security_type
        if not UtilClient.is_unset(request.source_storage):
            query['SourceStorage'] = request.source_storage
        if not UtilClient.is_unset(request.source_storage_path):
            query['SourceStoragePath'] = request.source_storage_path
        if not UtilClient.is_unset(request.throughput):
            query['Throughput'] = request.throughput
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateDataFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_flow(
        self,
        request: nas20170626_models.CreateDataFlowRequest,
    ) -> nas20170626_models.CreateDataFlowResponse:
        """
        @summary Creates a dataflow for a Cloud Parallel File Storage (CPFS) file system and source storage.
        
        @description    Basic operations
        Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flows.
        You can create a data flow only when a CPFS for LINGJUN file system is in the Running state.
        A maximum of 10 data flows can be created for a CPFS for LINGJUN file system.
        It generally takes 2 to 5 minutes to create a data flow. You can call the DescribeDataFlows operation to check whether the data flow has been created.
        Permissions
        When you create a data flow, CPFS for LINGJUN obtains the following two service-linked roles: `AliyunServiceRoleForNasOssDataflow` and `AliyunServiceRoleForNasEventNotification`. For more information, see [CPFS service-linked roles](https://help.aliyun.com/document_detail/2837688.html).
        CPFS for LINGJUN usage notes
        Source storage
        The source storage is an Object Storage Service (OSS) bucket. SourceStorage for a data flow must be an OSS bucket.
        CPFS for LINGJUN data flows support both encrypted and unencrypted access to OSS. If you select SSL-encrypted access to OSS, make sure that encryption in transit for OSS buckets supports encrypted access.
        If data flows for multiple CPFS for LINGJUN file systems or multiple data flows for the same CPFS for LINGJUN file system are stored in the same OSS bucket, you must enable versioning for the OSS bucket to prevent data conflicts caused by data export from multiple CPFS for LINGJUN file systems to one OSS bucket.
        Data flows are not supported for OSS buckets across regions. The OSS bucket must reside in the same region as the CPFS file system.
        CPFS for LINGJUN V2.6.0 and later allow you to create data flows for OSS buckets across accounts.
        The account id parameter is required only when you use OSS buckets across accounts.
        To use OSS buckets across accounts, you must first grant permissions to the related accounts. For more information, see [Cross-account authorization on data flows](https://help.aliyun.com/document_detail/2713462.html).
        >  Before you create a data flow, you must configure a tag (key: cpfs-dataflow, value: true) for the source OSS bucket. This way, the created data flow can access the data in the OSS bucket. When a data flow is being used, do not delete or modify the tag. Otherwise, the data flow for CPFS for LINGJUN cannot access the data in the OSS bucket.
        Limits of data flows on file systems
        You cannot rename a non-empty directory in a path that is associated with a data flow. Otherwise, the Permission Denied error message or an error message indicating that the directory is not empty is returned.
        Proceed with caution when you use special characters in the names of directories and files. The following characters are supported: letters, digits, exclamation points (!), hyphens (-), underscores (_), periods (.), asterisks (\\*), and parentheses (()).
        The path can be up to 1,023 characters in length.
        Limits of data flows on import
        After a symbolic link is imported to CPFS for LINGJUN, the symbolic link is converted into a common data file that contains no symbolic link information.
        If an OSS bucket has multiple versions, only data of the latest version is used.
        The name of a file or a subdirectory can be up to 255 bytes in length.
        Limits of data flows on export
        After a symbolic link is synchronized to OSS, the file that the symbolic link points to is not synchronized to OSS. In this case, the symbolic link is converted into a common object that contains no data.
        Hard links can be synchronized to OSS only as common files that contain no link information.
        After a file of the Socket, Device, or Pipe type is exported to an OSS bucket, the file is converted into a common object that contains no data.
        The directory path can be up to 1,023 characters in length.
        
        @param request: CreateDataFlowRequest
        @return: CreateDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_flow_with_options(request, runtime)

    async def create_data_flow_async(
        self,
        request: nas20170626_models.CreateDataFlowRequest,
    ) -> nas20170626_models.CreateDataFlowResponse:
        """
        @summary Creates a dataflow for a Cloud Parallel File Storage (CPFS) file system and source storage.
        
        @description    Basic operations
        Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flows.
        You can create a data flow only when a CPFS for LINGJUN file system is in the Running state.
        A maximum of 10 data flows can be created for a CPFS for LINGJUN file system.
        It generally takes 2 to 5 minutes to create a data flow. You can call the DescribeDataFlows operation to check whether the data flow has been created.
        Permissions
        When you create a data flow, CPFS for LINGJUN obtains the following two service-linked roles: `AliyunServiceRoleForNasOssDataflow` and `AliyunServiceRoleForNasEventNotification`. For more information, see [CPFS service-linked roles](https://help.aliyun.com/document_detail/2837688.html).
        CPFS for LINGJUN usage notes
        Source storage
        The source storage is an Object Storage Service (OSS) bucket. SourceStorage for a data flow must be an OSS bucket.
        CPFS for LINGJUN data flows support both encrypted and unencrypted access to OSS. If you select SSL-encrypted access to OSS, make sure that encryption in transit for OSS buckets supports encrypted access.
        If data flows for multiple CPFS for LINGJUN file systems or multiple data flows for the same CPFS for LINGJUN file system are stored in the same OSS bucket, you must enable versioning for the OSS bucket to prevent data conflicts caused by data export from multiple CPFS for LINGJUN file systems to one OSS bucket.
        Data flows are not supported for OSS buckets across regions. The OSS bucket must reside in the same region as the CPFS file system.
        CPFS for LINGJUN V2.6.0 and later allow you to create data flows for OSS buckets across accounts.
        The account id parameter is required only when you use OSS buckets across accounts.
        To use OSS buckets across accounts, you must first grant permissions to the related accounts. For more information, see [Cross-account authorization on data flows](https://help.aliyun.com/document_detail/2713462.html).
        >  Before you create a data flow, you must configure a tag (key: cpfs-dataflow, value: true) for the source OSS bucket. This way, the created data flow can access the data in the OSS bucket. When a data flow is being used, do not delete or modify the tag. Otherwise, the data flow for CPFS for LINGJUN cannot access the data in the OSS bucket.
        Limits of data flows on file systems
        You cannot rename a non-empty directory in a path that is associated with a data flow. Otherwise, the Permission Denied error message or an error message indicating that the directory is not empty is returned.
        Proceed with caution when you use special characters in the names of directories and files. The following characters are supported: letters, digits, exclamation points (!), hyphens (-), underscores (_), periods (.), asterisks (\\*), and parentheses (()).
        The path can be up to 1,023 characters in length.
        Limits of data flows on import
        After a symbolic link is imported to CPFS for LINGJUN, the symbolic link is converted into a common data file that contains no symbolic link information.
        If an OSS bucket has multiple versions, only data of the latest version is used.
        The name of a file or a subdirectory can be up to 255 bytes in length.
        Limits of data flows on export
        After a symbolic link is synchronized to OSS, the file that the symbolic link points to is not synchronized to OSS. In this case, the symbolic link is converted into a common object that contains no data.
        Hard links can be synchronized to OSS only as common files that contain no link information.
        After a file of the Socket, Device, or Pipe type is exported to an OSS bucket, the file is converted into a common object that contains no data.
        The directory path can be up to 1,023 characters in length.
        
        @param request: CreateDataFlowRequest
        @return: CreateDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_flow_with_options_async(request, runtime)

    def create_data_flow_sub_task_with_options(
        self,
        request: nas20170626_models.CreateDataFlowSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateDataFlowSubTaskResponse:
        """
        @summary Creates a data streaming subtask.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.6.0 and later support this operation. You can view the version information on the file system details page in the console.
        You can create subtasks only for a data streaming subtask in the Executing state.
        Data streaming tasks are executed asynchronously. You can call the DescribeDataFlowSubTasks operation to query the task execution status.
        When the type of data flow task is streaming, the running status only indicates that a streaming import or export task can be created. It does not indicate that the import or export task is running.
        
        @param request: CreateDataFlowSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataFlowSubTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.condition):
            query['Condition'] = request.condition
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.data_flow_task_id):
            query['DataFlowTaskId'] = request.data_flow_task_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.dst_file_path):
            query['DstFilePath'] = request.dst_file_path
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.src_file_path):
            query['SrcFilePath'] = request.src_file_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataFlowSubTask',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateDataFlowSubTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_flow_sub_task_with_options_async(
        self,
        request: nas20170626_models.CreateDataFlowSubTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateDataFlowSubTaskResponse:
        """
        @summary Creates a data streaming subtask.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.6.0 and later support this operation. You can view the version information on the file system details page in the console.
        You can create subtasks only for a data streaming subtask in the Executing state.
        Data streaming tasks are executed asynchronously. You can call the DescribeDataFlowSubTasks operation to query the task execution status.
        When the type of data flow task is streaming, the running status only indicates that a streaming import or export task can be created. It does not indicate that the import or export task is running.
        
        @param request: CreateDataFlowSubTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataFlowSubTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.condition):
            query['Condition'] = request.condition
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.data_flow_task_id):
            query['DataFlowTaskId'] = request.data_flow_task_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.dst_file_path):
            query['DstFilePath'] = request.dst_file_path
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.src_file_path):
            query['SrcFilePath'] = request.src_file_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataFlowSubTask',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateDataFlowSubTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_flow_sub_task(
        self,
        request: nas20170626_models.CreateDataFlowSubTaskRequest,
    ) -> nas20170626_models.CreateDataFlowSubTaskResponse:
        """
        @summary Creates a data streaming subtask.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.6.0 and later support this operation. You can view the version information on the file system details page in the console.
        You can create subtasks only for a data streaming subtask in the Executing state.
        Data streaming tasks are executed asynchronously. You can call the DescribeDataFlowSubTasks operation to query the task execution status.
        When the type of data flow task is streaming, the running status only indicates that a streaming import or export task can be created. It does not indicate that the import or export task is running.
        
        @param request: CreateDataFlowSubTaskRequest
        @return: CreateDataFlowSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_flow_sub_task_with_options(request, runtime)

    async def create_data_flow_sub_task_async(
        self,
        request: nas20170626_models.CreateDataFlowSubTaskRequest,
    ) -> nas20170626_models.CreateDataFlowSubTaskResponse:
        """
        @summary Creates a data streaming subtask.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.6.0 and later support this operation. You can view the version information on the file system details page in the console.
        You can create subtasks only for a data streaming subtask in the Executing state.
        Data streaming tasks are executed asynchronously. You can call the DescribeDataFlowSubTasks operation to query the task execution status.
        When the type of data flow task is streaming, the running status only indicates that a streaming import or export task can be created. It does not indicate that the import or export task is running.
        
        @param request: CreateDataFlowSubTaskRequest
        @return: CreateDataFlowSubTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_flow_sub_task_with_options_async(request, runtime)

    def create_data_flow_task_with_options(
        self,
        request: nas20170626_models.CreateDataFlowTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateDataFlowTaskResponse:
        """
        @summary Creates a dataflow task.
        
        @description    Only Cloud Parallel File Storage CPFS for LINGJUN V2.4.0 and later support data flows. You can view the version information on the file system details page in the console.
        You can create a data flow task only for a data flow that is in the Running state.
        Data flow tasks are executed asynchronously. You can call the [DescribeDataFlowTasks](https://help.aliyun.com/document_detail/2838089.html) operation to query the task execution status. The task duration depends on the amount of data to be imported and exported. If a large amount of data exists, we recommend that you create multiple tasks.
        When you manually run a data flow task, the automatic data update task for the data flow is interrupted and enters the pending state.
        When you create an export task, make sure that the total length of the absolute path of the files to be exported from a CPFS or CPFS for LINGJUN file system does not exceed 1,023 characters.
        CPFS for LINGJUN supports two types of tasks: batch tasks and streaming tasks. For more information, see [Task types](https://help.aliyun.com/document_detail/2845429.html).
        
        @param request: CreateDataFlowTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataFlowTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.conflict_policy):
            query['ConflictPolicy'] = request.conflict_policy
        if not UtilClient.is_unset(request.create_dir_if_not_exist):
            query['CreateDirIfNotExist'] = request.create_dir_if_not_exist
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.directory):
            query['Directory'] = request.directory
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.dst_directory):
            query['DstDirectory'] = request.dst_directory
        if not UtilClient.is_unset(request.entry_list):
            query['EntryList'] = request.entry_list
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.includes):
            query['Includes'] = request.includes
        if not UtilClient.is_unset(request.src_task_id):
            query['SrcTaskId'] = request.src_task_id
        if not UtilClient.is_unset(request.task_action):
            query['TaskAction'] = request.task_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataFlowTask',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateDataFlowTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_flow_task_with_options_async(
        self,
        request: nas20170626_models.CreateDataFlowTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateDataFlowTaskResponse:
        """
        @summary Creates a dataflow task.
        
        @description    Only Cloud Parallel File Storage CPFS for LINGJUN V2.4.0 and later support data flows. You can view the version information on the file system details page in the console.
        You can create a data flow task only for a data flow that is in the Running state.
        Data flow tasks are executed asynchronously. You can call the [DescribeDataFlowTasks](https://help.aliyun.com/document_detail/2838089.html) operation to query the task execution status. The task duration depends on the amount of data to be imported and exported. If a large amount of data exists, we recommend that you create multiple tasks.
        When you manually run a data flow task, the automatic data update task for the data flow is interrupted and enters the pending state.
        When you create an export task, make sure that the total length of the absolute path of the files to be exported from a CPFS or CPFS for LINGJUN file system does not exceed 1,023 characters.
        CPFS for LINGJUN supports two types of tasks: batch tasks and streaming tasks. For more information, see [Task types](https://help.aliyun.com/document_detail/2845429.html).
        
        @param request: CreateDataFlowTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDataFlowTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.conflict_policy):
            query['ConflictPolicy'] = request.conflict_policy
        if not UtilClient.is_unset(request.create_dir_if_not_exist):
            query['CreateDirIfNotExist'] = request.create_dir_if_not_exist
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.directory):
            query['Directory'] = request.directory
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.dst_directory):
            query['DstDirectory'] = request.dst_directory
        if not UtilClient.is_unset(request.entry_list):
            query['EntryList'] = request.entry_list
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.includes):
            query['Includes'] = request.includes
        if not UtilClient.is_unset(request.src_task_id):
            query['SrcTaskId'] = request.src_task_id
        if not UtilClient.is_unset(request.task_action):
            query['TaskAction'] = request.task_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataFlowTask',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateDataFlowTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_data_flow_task(
        self,
        request: nas20170626_models.CreateDataFlowTaskRequest,
    ) -> nas20170626_models.CreateDataFlowTaskResponse:
        """
        @summary Creates a dataflow task.
        
        @description    Only Cloud Parallel File Storage CPFS for LINGJUN V2.4.0 and later support data flows. You can view the version information on the file system details page in the console.
        You can create a data flow task only for a data flow that is in the Running state.
        Data flow tasks are executed asynchronously. You can call the [DescribeDataFlowTasks](https://help.aliyun.com/document_detail/2838089.html) operation to query the task execution status. The task duration depends on the amount of data to be imported and exported. If a large amount of data exists, we recommend that you create multiple tasks.
        When you manually run a data flow task, the automatic data update task for the data flow is interrupted and enters the pending state.
        When you create an export task, make sure that the total length of the absolute path of the files to be exported from a CPFS or CPFS for LINGJUN file system does not exceed 1,023 characters.
        CPFS for LINGJUN supports two types of tasks: batch tasks and streaming tasks. For more information, see [Task types](https://help.aliyun.com/document_detail/2845429.html).
        
        @param request: CreateDataFlowTaskRequest
        @return: CreateDataFlowTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_data_flow_task_with_options(request, runtime)

    async def create_data_flow_task_async(
        self,
        request: nas20170626_models.CreateDataFlowTaskRequest,
    ) -> nas20170626_models.CreateDataFlowTaskResponse:
        """
        @summary Creates a dataflow task.
        
        @description    Only Cloud Parallel File Storage CPFS for LINGJUN V2.4.0 and later support data flows. You can view the version information on the file system details page in the console.
        You can create a data flow task only for a data flow that is in the Running state.
        Data flow tasks are executed asynchronously. You can call the [DescribeDataFlowTasks](https://help.aliyun.com/document_detail/2838089.html) operation to query the task execution status. The task duration depends on the amount of data to be imported and exported. If a large amount of data exists, we recommend that you create multiple tasks.
        When you manually run a data flow task, the automatic data update task for the data flow is interrupted and enters the pending state.
        When you create an export task, make sure that the total length of the absolute path of the files to be exported from a CPFS or CPFS for LINGJUN file system does not exceed 1,023 characters.
        CPFS for LINGJUN supports two types of tasks: batch tasks and streaming tasks. For more information, see [Task types](https://help.aliyun.com/document_detail/2845429.html).
        
        @param request: CreateDataFlowTaskRequest
        @return: CreateDataFlowTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_data_flow_task_with_options_async(request, runtime)

    def create_dir_with_options(
        self,
        request: nas20170626_models.CreateDirRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateDirResponse:
        """
        @summary Creates a directory in a file system.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: CreateDirRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDirResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.owner_group_id):
            query['OwnerGroupId'] = request.owner_group_id
        if not UtilClient.is_unset(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.permission):
            query['Permission'] = request.permission
        if not UtilClient.is_unset(request.recursion):
            query['Recursion'] = request.recursion
        if not UtilClient.is_unset(request.root_directory):
            query['RootDirectory'] = request.root_directory
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDir',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateDirResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dir_with_options_async(
        self,
        request: nas20170626_models.CreateDirRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateDirResponse:
        """
        @summary Creates a directory in a file system.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: CreateDirRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDirResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.owner_group_id):
            query['OwnerGroupId'] = request.owner_group_id
        if not UtilClient.is_unset(request.owner_user_id):
            query['OwnerUserId'] = request.owner_user_id
        if not UtilClient.is_unset(request.permission):
            query['Permission'] = request.permission
        if not UtilClient.is_unset(request.recursion):
            query['Recursion'] = request.recursion
        if not UtilClient.is_unset(request.root_directory):
            query['RootDirectory'] = request.root_directory
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDir',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateDirResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dir(
        self,
        request: nas20170626_models.CreateDirRequest,
    ) -> nas20170626_models.CreateDirResponse:
        """
        @summary Creates a directory in a file system.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: CreateDirRequest
        @return: CreateDirResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dir_with_options(request, runtime)

    async def create_dir_async(
        self,
        request: nas20170626_models.CreateDirRequest,
    ) -> nas20170626_models.CreateDirResponse:
        """
        @summary Creates a directory in a file system.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: CreateDirRequest
        @return: CreateDirResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dir_with_options_async(request, runtime)

    def create_file_with_options(
        self,
        request: nas20170626_models.CreateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateFileResponse:
        """
        @summary Creates a directory or file.
        
        @description    This operation is only available to some users.
        This operation supports only General-purpose NAS file systems that use the Server Message Block (SMB) protocol and have Resource Access Management (RAM) enabled.
        
        @param request: CreateFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.owner_access_inheritable):
            query['OwnerAccessInheritable'] = request.owner_access_inheritable
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_with_options_async(
        self,
        request: nas20170626_models.CreateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateFileResponse:
        """
        @summary Creates a directory or file.
        
        @description    This operation is only available to some users.
        This operation supports only General-purpose NAS file systems that use the Server Message Block (SMB) protocol and have Resource Access Management (RAM) enabled.
        
        @param request: CreateFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.owner):
            query['Owner'] = request.owner
        if not UtilClient.is_unset(request.owner_access_inheritable):
            query['OwnerAccessInheritable'] = request.owner_access_inheritable
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFile',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file(
        self,
        request: nas20170626_models.CreateFileRequest,
    ) -> nas20170626_models.CreateFileResponse:
        """
        @summary Creates a directory or file.
        
        @description    This operation is only available to some users.
        This operation supports only General-purpose NAS file systems that use the Server Message Block (SMB) protocol and have Resource Access Management (RAM) enabled.
        
        @param request: CreateFileRequest
        @return: CreateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_file_with_options(request, runtime)

    async def create_file_async(
        self,
        request: nas20170626_models.CreateFileRequest,
    ) -> nas20170626_models.CreateFileResponse:
        """
        @summary Creates a directory or file.
        
        @description    This operation is only available to some users.
        This operation supports only General-purpose NAS file systems that use the Server Message Block (SMB) protocol and have Resource Access Management (RAM) enabled.
        
        @param request: CreateFileRequest
        @return: CreateFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_file_with_options_async(request, runtime)

    def create_file_system_with_options(
        self,
        request: nas20170626_models.CreateFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateFileSystemResponse:
        """
        @summary Creates a file system.
        
        @description    Before you call this operation, you must understand the billing and pricing of File Storage NAS. For more information, see [Billing](https://help.aliyun.com/document_detail/178365.html) and [Pricing](https://www.alibabacloud.com/product/nas/pricing).
        Before you create a file system, you must complete real-name verification.
        When you call this operation, a service-linked role of NAS is automatically created. For more information, see [Manage the service-linked roles of NAS](https://help.aliyun.com/document_detail/208530.html).
        
        @param request: CreateFileSystemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_system_with_options_async(
        self,
        request: nas20170626_models.CreateFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateFileSystemResponse:
        """
        @summary Creates a file system.
        
        @description    Before you call this operation, you must understand the billing and pricing of File Storage NAS. For more information, see [Billing](https://help.aliyun.com/document_detail/178365.html) and [Pricing](https://www.alibabacloud.com/product/nas/pricing).
        Before you create a file system, you must complete real-name verification.
        When you call this operation, a service-linked role of NAS is automatically created. For more information, see [Manage the service-linked roles of NAS](https://help.aliyun.com/document_detail/208530.html).
        
        @param request: CreateFileSystemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.kms_key_id):
            query['KmsKeyId'] = request.kms_key_id
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file_system(
        self,
        request: nas20170626_models.CreateFileSystemRequest,
    ) -> nas20170626_models.CreateFileSystemResponse:
        """
        @summary Creates a file system.
        
        @description    Before you call this operation, you must understand the billing and pricing of File Storage NAS. For more information, see [Billing](https://help.aliyun.com/document_detail/178365.html) and [Pricing](https://www.alibabacloud.com/product/nas/pricing).
        Before you create a file system, you must complete real-name verification.
        When you call this operation, a service-linked role of NAS is automatically created. For more information, see [Manage the service-linked roles of NAS](https://help.aliyun.com/document_detail/208530.html).
        
        @param request: CreateFileSystemRequest
        @return: CreateFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_file_system_with_options(request, runtime)

    async def create_file_system_async(
        self,
        request: nas20170626_models.CreateFileSystemRequest,
    ) -> nas20170626_models.CreateFileSystemResponse:
        """
        @summary Creates a file system.
        
        @description    Before you call this operation, you must understand the billing and pricing of File Storage NAS. For more information, see [Billing](https://help.aliyun.com/document_detail/178365.html) and [Pricing](https://www.alibabacloud.com/product/nas/pricing).
        Before you create a file system, you must complete real-name verification.
        When you call this operation, a service-linked role of NAS is automatically created. For more information, see [Manage the service-linked roles of NAS](https://help.aliyun.com/document_detail/208530.html).
        
        @param request: CreateFileSystemRequest
        @return: CreateFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_file_system_with_options_async(request, runtime)

    def create_fileset_with_options(
        self,
        request: nas20170626_models.CreateFilesetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateFilesetResponse:
        """
        @summary Creates a fileset.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation. You can view the version information on the file system details page in the console.
        A maximum of 500 filesets can be created for a CPFS file system.
        The fileset path must be a new path and cannot be an existing path. Fileset paths cannot be renamed and cannot be symbolic links.
        The maximum depth supported by a fileset path is eight levels. The depth of the root directory / is 0 levels. For example, the fileset path /test/aaa/ccc/ has three levels.
        If the fileset path is a multi-level path, the parent directory must be an existing directory.
        Nested filesets are not supported. If a fileset is specified as a parent directory, its subdirectory cannot be a fileset. A fileset path supports only one quota.
        The minimum capacity quota of a fileset is 10 GiB. The scaling step size is 1 GiB. The maximum capacity quota is 1,000 TiB. The capacity quota cannot exceed the total capacity of the file system.
        A fileset supports a minimum of 10,000 files or directories and a maximum of 10 billion files or directories. The scaling step size is 1.
        When you modify a directory quota, you must set the quota capacity or the number of files to be greater than the capacity or file quantity that has been used.
        The quota statistics have a 5-minute latency. The actual usage takes effect after 5 minutes.
        
        @param request: CreateFilesetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFilesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_path):
            query['FileSystemPath'] = request.file_system_path
        if not UtilClient.is_unset(request.quota):
            query['Quota'] = request.quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileset',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateFilesetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fileset_with_options_async(
        self,
        request: nas20170626_models.CreateFilesetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateFilesetResponse:
        """
        @summary Creates a fileset.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation. You can view the version information on the file system details page in the console.
        A maximum of 500 filesets can be created for a CPFS file system.
        The fileset path must be a new path and cannot be an existing path. Fileset paths cannot be renamed and cannot be symbolic links.
        The maximum depth supported by a fileset path is eight levels. The depth of the root directory / is 0 levels. For example, the fileset path /test/aaa/ccc/ has three levels.
        If the fileset path is a multi-level path, the parent directory must be an existing directory.
        Nested filesets are not supported. If a fileset is specified as a parent directory, its subdirectory cannot be a fileset. A fileset path supports only one quota.
        The minimum capacity quota of a fileset is 10 GiB. The scaling step size is 1 GiB. The maximum capacity quota is 1,000 TiB. The capacity quota cannot exceed the total capacity of the file system.
        A fileset supports a minimum of 10,000 files or directories and a maximum of 10 billion files or directories. The scaling step size is 1.
        When you modify a directory quota, you must set the quota capacity or the number of files to be greater than the capacity or file quantity that has been used.
        The quota statistics have a 5-minute latency. The actual usage takes effect after 5 minutes.
        
        @param request: CreateFilesetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFilesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_path):
            query['FileSystemPath'] = request.file_system_path
        if not UtilClient.is_unset(request.quota):
            query['Quota'] = request.quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileset',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateFilesetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fileset(
        self,
        request: nas20170626_models.CreateFilesetRequest,
    ) -> nas20170626_models.CreateFilesetResponse:
        """
        @summary Creates a fileset.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation. You can view the version information on the file system details page in the console.
        A maximum of 500 filesets can be created for a CPFS file system.
        The fileset path must be a new path and cannot be an existing path. Fileset paths cannot be renamed and cannot be symbolic links.
        The maximum depth supported by a fileset path is eight levels. The depth of the root directory / is 0 levels. For example, the fileset path /test/aaa/ccc/ has three levels.
        If the fileset path is a multi-level path, the parent directory must be an existing directory.
        Nested filesets are not supported. If a fileset is specified as a parent directory, its subdirectory cannot be a fileset. A fileset path supports only one quota.
        The minimum capacity quota of a fileset is 10 GiB. The scaling step size is 1 GiB. The maximum capacity quota is 1,000 TiB. The capacity quota cannot exceed the total capacity of the file system.
        A fileset supports a minimum of 10,000 files or directories and a maximum of 10 billion files or directories. The scaling step size is 1.
        When you modify a directory quota, you must set the quota capacity or the number of files to be greater than the capacity or file quantity that has been used.
        The quota statistics have a 5-minute latency. The actual usage takes effect after 5 minutes.
        
        @param request: CreateFilesetRequest
        @return: CreateFilesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_fileset_with_options(request, runtime)

    async def create_fileset_async(
        self,
        request: nas20170626_models.CreateFilesetRequest,
    ) -> nas20170626_models.CreateFilesetResponse:
        """
        @summary Creates a fileset.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation. You can view the version information on the file system details page in the console.
        A maximum of 500 filesets can be created for a CPFS file system.
        The fileset path must be a new path and cannot be an existing path. Fileset paths cannot be renamed and cannot be symbolic links.
        The maximum depth supported by a fileset path is eight levels. The depth of the root directory / is 0 levels. For example, the fileset path /test/aaa/ccc/ has three levels.
        If the fileset path is a multi-level path, the parent directory must be an existing directory.
        Nested filesets are not supported. If a fileset is specified as a parent directory, its subdirectory cannot be a fileset. A fileset path supports only one quota.
        The minimum capacity quota of a fileset is 10 GiB. The scaling step size is 1 GiB. The maximum capacity quota is 1,000 TiB. The capacity quota cannot exceed the total capacity of the file system.
        A fileset supports a minimum of 10,000 files or directories and a maximum of 10 billion files or directories. The scaling step size is 1.
        When you modify a directory quota, you must set the quota capacity or the number of files to be greater than the capacity or file quantity that has been used.
        The quota statistics have a 5-minute latency. The actual usage takes effect after 5 minutes.
        
        @param request: CreateFilesetRequest
        @return: CreateFilesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_fileset_with_options_async(request, runtime)

    def create_ldapconfig_with_options(
        self,
        request: nas20170626_models.CreateLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLDAPConfigResponse:
        """
        @deprecated OpenAPI CreateLDAPConfig is deprecated
        
        @summary Creates LDAP configurations.
        
        @param request: CreateLDAPConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLDAPConfigResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_dn):
            query['BindDN'] = request.bind_dn
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.search_base):
            query['SearchBase'] = request.search_base
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLDAPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ldapconfig_with_options_async(
        self,
        request: nas20170626_models.CreateLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLDAPConfigResponse:
        """
        @deprecated OpenAPI CreateLDAPConfig is deprecated
        
        @summary Creates LDAP configurations.
        
        @param request: CreateLDAPConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLDAPConfigResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_dn):
            query['BindDN'] = request.bind_dn
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.search_base):
            query['SearchBase'] = request.search_base
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLDAPConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ldapconfig(
        self,
        request: nas20170626_models.CreateLDAPConfigRequest,
    ) -> nas20170626_models.CreateLDAPConfigResponse:
        """
        @deprecated OpenAPI CreateLDAPConfig is deprecated
        
        @summary Creates LDAP configurations.
        
        @param request: CreateLDAPConfigRequest
        @return: CreateLDAPConfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ldapconfig_with_options(request, runtime)

    async def create_ldapconfig_async(
        self,
        request: nas20170626_models.CreateLDAPConfigRequest,
    ) -> nas20170626_models.CreateLDAPConfigResponse:
        """
        @deprecated OpenAPI CreateLDAPConfig is deprecated
        
        @summary Creates LDAP configurations.
        
        @param request: CreateLDAPConfigRequest
        @return: CreateLDAPConfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_ldapconfig_with_options_async(request, runtime)

    def create_lifecycle_policy_with_options(
        self,
        request: nas20170626_models.CreateLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLifecyclePolicyResponse:
        """
        @summary Creates a lifecycle policy.
        
        @description    You can create lifecycle policies only for General-purpose NAS file systems.
        You can create up to 20 lifecycle policies in each region within an Alibaba Cloud account.
        
        @param request: CreateLifecyclePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLifecyclePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        if not UtilClient.is_unset(request.lifecycle_rule_name):
            query['LifecycleRuleName'] = request.lifecycle_rule_name
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.paths):
            query['Paths'] = request.paths
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLifecyclePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lifecycle_policy_with_options_async(
        self,
        request: nas20170626_models.CreateLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLifecyclePolicyResponse:
        """
        @summary Creates a lifecycle policy.
        
        @description    You can create lifecycle policies only for General-purpose NAS file systems.
        You can create up to 20 lifecycle policies in each region within an Alibaba Cloud account.
        
        @param request: CreateLifecyclePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLifecyclePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        if not UtilClient.is_unset(request.lifecycle_rule_name):
            query['LifecycleRuleName'] = request.lifecycle_rule_name
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.paths):
            query['Paths'] = request.paths
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLifecyclePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lifecycle_policy(
        self,
        request: nas20170626_models.CreateLifecyclePolicyRequest,
    ) -> nas20170626_models.CreateLifecyclePolicyResponse:
        """
        @summary Creates a lifecycle policy.
        
        @description    You can create lifecycle policies only for General-purpose NAS file systems.
        You can create up to 20 lifecycle policies in each region within an Alibaba Cloud account.
        
        @param request: CreateLifecyclePolicyRequest
        @return: CreateLifecyclePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_lifecycle_policy_with_options(request, runtime)

    async def create_lifecycle_policy_async(
        self,
        request: nas20170626_models.CreateLifecyclePolicyRequest,
    ) -> nas20170626_models.CreateLifecyclePolicyResponse:
        """
        @summary Creates a lifecycle policy.
        
        @description    You can create lifecycle policies only for General-purpose NAS file systems.
        You can create up to 20 lifecycle policies in each region within an Alibaba Cloud account.
        
        @param request: CreateLifecyclePolicyRequest
        @return: CreateLifecyclePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_lifecycle_policy_with_options_async(request, runtime)

    def create_lifecycle_retrieve_job_with_options(
        self,
        request: nas20170626_models.CreateLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLifecycleRetrieveJobResponse:
        """
        @summary Creates a data retrieval task.
        
        @description    Only General-purpose NAS file systems support this operation.
        You can run a maximum of 20 data retrieval tasks in each region within an Alibaba Cloud account.
        
        @param request: CreateLifecycleRetrieveJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLifecycleRetrieveJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.paths):
            query['Paths'] = request.paths
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLifecycleRetrieveJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lifecycle_retrieve_job_with_options_async(
        self,
        request: nas20170626_models.CreateLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLifecycleRetrieveJobResponse:
        """
        @summary Creates a data retrieval task.
        
        @description    Only General-purpose NAS file systems support this operation.
        You can run a maximum of 20 data retrieval tasks in each region within an Alibaba Cloud account.
        
        @param request: CreateLifecycleRetrieveJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLifecycleRetrieveJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.paths):
            query['Paths'] = request.paths
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLifecycleRetrieveJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lifecycle_retrieve_job(
        self,
        request: nas20170626_models.CreateLifecycleRetrieveJobRequest,
    ) -> nas20170626_models.CreateLifecycleRetrieveJobResponse:
        """
        @summary Creates a data retrieval task.
        
        @description    Only General-purpose NAS file systems support this operation.
        You can run a maximum of 20 data retrieval tasks in each region within an Alibaba Cloud account.
        
        @param request: CreateLifecycleRetrieveJobRequest
        @return: CreateLifecycleRetrieveJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_lifecycle_retrieve_job_with_options(request, runtime)

    async def create_lifecycle_retrieve_job_async(
        self,
        request: nas20170626_models.CreateLifecycleRetrieveJobRequest,
    ) -> nas20170626_models.CreateLifecycleRetrieveJobResponse:
        """
        @summary Creates a data retrieval task.
        
        @description    Only General-purpose NAS file systems support this operation.
        You can run a maximum of 20 data retrieval tasks in each region within an Alibaba Cloud account.
        
        @param request: CreateLifecycleRetrieveJobRequest
        @return: CreateLifecycleRetrieveJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_lifecycle_retrieve_job_with_options_async(request, runtime)

    def create_log_analysis_with_options(
        self,
        request: nas20170626_models.CreateLogAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLogAnalysisResponse:
        """
        @summary Dumps the logs of a General-purpose NAS file system to Simple Log Service.
        
        @param request: CreateLogAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLogAnalysisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogAnalysis',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLogAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_log_analysis_with_options_async(
        self,
        request: nas20170626_models.CreateLogAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateLogAnalysisResponse:
        """
        @summary Dumps the logs of a General-purpose NAS file system to Simple Log Service.
        
        @param request: CreateLogAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLogAnalysisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLogAnalysis',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateLogAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_log_analysis(
        self,
        request: nas20170626_models.CreateLogAnalysisRequest,
    ) -> nas20170626_models.CreateLogAnalysisResponse:
        """
        @summary Dumps the logs of a General-purpose NAS file system to Simple Log Service.
        
        @param request: CreateLogAnalysisRequest
        @return: CreateLogAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_log_analysis_with_options(request, runtime)

    async def create_log_analysis_async(
        self,
        request: nas20170626_models.CreateLogAnalysisRequest,
    ) -> nas20170626_models.CreateLogAnalysisResponse:
        """
        @summary Dumps the logs of a General-purpose NAS file system to Simple Log Service.
        
        @param request: CreateLogAnalysisRequest
        @return: CreateLogAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_log_analysis_with_options_async(request, runtime)

    def create_mount_target_with_options(
        self,
        request: nas20170626_models.CreateMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateMountTargetResponse:
        """
        @summary Creates a mount target.
        
        @description    After you call the CreateMountTarget operation, a mount target is not immediately created. Therefore, we recommend that you call the DescribeMountTargets operation to query the status of the mount target. If the mount target is in the **Active** state, you can then mount the file system. Otherwise, the file system may fail to be mounted.
        When you call this operation, a service-linked role of NAS is automatically created. For more information, see [Manage the service-linked roles of NAS](https://help.aliyun.com/document_detail/208530.html).
        
        @param request: CreateMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.enable_ipv_6):
            query['EnableIpv6'] = request.enable_ipv_6
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mount_target_with_options_async(
        self,
        request: nas20170626_models.CreateMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateMountTargetResponse:
        """
        @summary Creates a mount target.
        
        @description    After you call the CreateMountTarget operation, a mount target is not immediately created. Therefore, we recommend that you call the DescribeMountTargets operation to query the status of the mount target. If the mount target is in the **Active** state, you can then mount the file system. Otherwise, the file system may fail to be mounted.
        When you call this operation, a service-linked role of NAS is automatically created. For more information, see [Manage the service-linked roles of NAS](https://help.aliyun.com/document_detail/208530.html).
        
        @param request: CreateMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.enable_ipv_6):
            query['EnableIpv6'] = request.enable_ipv_6
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mount_target(
        self,
        request: nas20170626_models.CreateMountTargetRequest,
    ) -> nas20170626_models.CreateMountTargetResponse:
        """
        @summary Creates a mount target.
        
        @description    After you call the CreateMountTarget operation, a mount target is not immediately created. Therefore, we recommend that you call the DescribeMountTargets operation to query the status of the mount target. If the mount target is in the **Active** state, you can then mount the file system. Otherwise, the file system may fail to be mounted.
        When you call this operation, a service-linked role of NAS is automatically created. For more information, see [Manage the service-linked roles of NAS](https://help.aliyun.com/document_detail/208530.html).
        
        @param request: CreateMountTargetRequest
        @return: CreateMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_mount_target_with_options(request, runtime)

    async def create_mount_target_async(
        self,
        request: nas20170626_models.CreateMountTargetRequest,
    ) -> nas20170626_models.CreateMountTargetResponse:
        """
        @summary Creates a mount target.
        
        @description    After you call the CreateMountTarget operation, a mount target is not immediately created. Therefore, we recommend that you call the DescribeMountTargets operation to query the status of the mount target. If the mount target is in the **Active** state, you can then mount the file system. Otherwise, the file system may fail to be mounted.
        When you call this operation, a service-linked role of NAS is automatically created. For more information, see [Manage the service-linked roles of NAS](https://help.aliyun.com/document_detail/208530.html).
        
        @param request: CreateMountTargetRequest
        @return: CreateMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_mount_target_with_options_async(request, runtime)

    def create_protocol_mount_target_with_options(
        self,
        request: nas20170626_models.CreateProtocolMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateProtocolMountTargetResponse:
        """
        @summary Creates an export directory for a protocol service.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Prerequisites
        A protocol service is created.
        Others
        The virtual private cloud (VPC) CIDR block of the export directory for the protocol service cannot overlap with the VPC CIDR block of the file system.
        The VPC CIDR blocks of multiple export directories of a protocol service cannot overlap.
        You can create a maximum of 10 export directories for a protocol service.
        When you create export directories for a protocol service, a maximum of 32 IP addresses that are allocated by the specified vSwitch are used. Make sure that the vSwitch can provide sufficient IP addresses.
        
        @param request: CreateProtocolMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProtocolMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProtocolMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateProtocolMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_protocol_mount_target_with_options_async(
        self,
        request: nas20170626_models.CreateProtocolMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateProtocolMountTargetResponse:
        """
        @summary Creates an export directory for a protocol service.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Prerequisites
        A protocol service is created.
        Others
        The virtual private cloud (VPC) CIDR block of the export directory for the protocol service cannot overlap with the VPC CIDR block of the file system.
        The VPC CIDR blocks of multiple export directories of a protocol service cannot overlap.
        You can create a maximum of 10 export directories for a protocol service.
        When you create export directories for a protocol service, a maximum of 32 IP addresses that are allocated by the specified vSwitch are used. Make sure that the vSwitch can provide sufficient IP addresses.
        
        @param request: CreateProtocolMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProtocolMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProtocolMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateProtocolMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_protocol_mount_target(
        self,
        request: nas20170626_models.CreateProtocolMountTargetRequest,
    ) -> nas20170626_models.CreateProtocolMountTargetResponse:
        """
        @summary Creates an export directory for a protocol service.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Prerequisites
        A protocol service is created.
        Others
        The virtual private cloud (VPC) CIDR block of the export directory for the protocol service cannot overlap with the VPC CIDR block of the file system.
        The VPC CIDR blocks of multiple export directories of a protocol service cannot overlap.
        You can create a maximum of 10 export directories for a protocol service.
        When you create export directories for a protocol service, a maximum of 32 IP addresses that are allocated by the specified vSwitch are used. Make sure that the vSwitch can provide sufficient IP addresses.
        
        @param request: CreateProtocolMountTargetRequest
        @return: CreateProtocolMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_protocol_mount_target_with_options(request, runtime)

    async def create_protocol_mount_target_async(
        self,
        request: nas20170626_models.CreateProtocolMountTargetRequest,
    ) -> nas20170626_models.CreateProtocolMountTargetResponse:
        """
        @summary Creates an export directory for a protocol service.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Prerequisites
        A protocol service is created.
        Others
        The virtual private cloud (VPC) CIDR block of the export directory for the protocol service cannot overlap with the VPC CIDR block of the file system.
        The VPC CIDR blocks of multiple export directories of a protocol service cannot overlap.
        You can create a maximum of 10 export directories for a protocol service.
        When you create export directories for a protocol service, a maximum of 32 IP addresses that are allocated by the specified vSwitch are used. Make sure that the vSwitch can provide sufficient IP addresses.
        
        @param request: CreateProtocolMountTargetRequest
        @return: CreateProtocolMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_protocol_mount_target_with_options_async(request, runtime)

    def create_protocol_service_with_options(
        self,
        request: nas20170626_models.CreateProtocolServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateProtocolServiceResponse:
        """
        @summary Creates a protocol service for a Cloud Parallel File Storage (CPFS) file system. The creation takes about 5 to 10 minutes.
        
        @description    This operation is available only to CPFS file systems on the China site (aliyun.com).
        Only CPFS V2.3.0 and later support protocol services. You can query the version information of the file system by calling the [DescribeFileSystems](~~2402188.~~) operation.
        Protocol service types
        Protocol services are classified into general-purpose protocol services and cache protocol services. Different from general-purpose protocol services, cache protocol services can cache hot data. If data exists in the cache, the bandwidth of the cache protocol service may exceed the bandwidth of the CPFS file system, reaching the maximum bandwidth specified for the protocol service.
        General-purpose protocol services: provide NFS access and [directory-level mount targets](https://help.aliyun.com/document_detail/427175.html) for CPFS file systems. You do not need to configure a POSIX client to manage clusters. General-purpose protocol services are provided free of charge.
        Cache protocol services: provide the server memory cache based on the least recently used (LRU) policy. When data is cached in the memory, CPFS provides higher internal bandwidth. Cache protocol services are divided into Cache L1 and Cache L2 specifications. The differences are the internal bandwidth size and memory cache size.
        >   Note You are charged for using cache protocol services, which are in invitational preview. For more information about the billing method of cache protocol services, see [Billable items](https://help.aliyun.com/document_detail/111858.html). If you have any feedback or questions, you can join the DingTalk group (group number: 31045006299).
        Protocol type
        Only NFSv3 is supported.
        Others
        Only one protocol service can be created for a CPFS file system.
        A protocol service can use a maximum of 32 IP addresses that are allocated by a specified vSwitch. Make sure that the vSwitch can provide sufficient IP addresses.
        
        @param request: CreateProtocolServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProtocolServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_spec):
            query['ProtocolSpec'] = request.protocol_spec
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.throughput):
            query['Throughput'] = request.throughput
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProtocolService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateProtocolServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_protocol_service_with_options_async(
        self,
        request: nas20170626_models.CreateProtocolServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateProtocolServiceResponse:
        """
        @summary Creates a protocol service for a Cloud Parallel File Storage (CPFS) file system. The creation takes about 5 to 10 minutes.
        
        @description    This operation is available only to CPFS file systems on the China site (aliyun.com).
        Only CPFS V2.3.0 and later support protocol services. You can query the version information of the file system by calling the [DescribeFileSystems](~~2402188.~~) operation.
        Protocol service types
        Protocol services are classified into general-purpose protocol services and cache protocol services. Different from general-purpose protocol services, cache protocol services can cache hot data. If data exists in the cache, the bandwidth of the cache protocol service may exceed the bandwidth of the CPFS file system, reaching the maximum bandwidth specified for the protocol service.
        General-purpose protocol services: provide NFS access and [directory-level mount targets](https://help.aliyun.com/document_detail/427175.html) for CPFS file systems. You do not need to configure a POSIX client to manage clusters. General-purpose protocol services are provided free of charge.
        Cache protocol services: provide the server memory cache based on the least recently used (LRU) policy. When data is cached in the memory, CPFS provides higher internal bandwidth. Cache protocol services are divided into Cache L1 and Cache L2 specifications. The differences are the internal bandwidth size and memory cache size.
        >   Note You are charged for using cache protocol services, which are in invitational preview. For more information about the billing method of cache protocol services, see [Billable items](https://help.aliyun.com/document_detail/111858.html). If you have any feedback or questions, you can join the DingTalk group (group number: 31045006299).
        Protocol type
        Only NFSv3 is supported.
        Others
        Only one protocol service can be created for a CPFS file system.
        A protocol service can use a maximum of 32 IP addresses that are allocated by a specified vSwitch. Make sure that the vSwitch can provide sufficient IP addresses.
        
        @param request: CreateProtocolServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProtocolServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_spec):
            query['ProtocolSpec'] = request.protocol_spec
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.throughput):
            query['Throughput'] = request.throughput
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProtocolService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateProtocolServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_protocol_service(
        self,
        request: nas20170626_models.CreateProtocolServiceRequest,
    ) -> nas20170626_models.CreateProtocolServiceResponse:
        """
        @summary Creates a protocol service for a Cloud Parallel File Storage (CPFS) file system. The creation takes about 5 to 10 minutes.
        
        @description    This operation is available only to CPFS file systems on the China site (aliyun.com).
        Only CPFS V2.3.0 and later support protocol services. You can query the version information of the file system by calling the [DescribeFileSystems](~~2402188.~~) operation.
        Protocol service types
        Protocol services are classified into general-purpose protocol services and cache protocol services. Different from general-purpose protocol services, cache protocol services can cache hot data. If data exists in the cache, the bandwidth of the cache protocol service may exceed the bandwidth of the CPFS file system, reaching the maximum bandwidth specified for the protocol service.
        General-purpose protocol services: provide NFS access and [directory-level mount targets](https://help.aliyun.com/document_detail/427175.html) for CPFS file systems. You do not need to configure a POSIX client to manage clusters. General-purpose protocol services are provided free of charge.
        Cache protocol services: provide the server memory cache based on the least recently used (LRU) policy. When data is cached in the memory, CPFS provides higher internal bandwidth. Cache protocol services are divided into Cache L1 and Cache L2 specifications. The differences are the internal bandwidth size and memory cache size.
        >   Note You are charged for using cache protocol services, which are in invitational preview. For more information about the billing method of cache protocol services, see [Billable items](https://help.aliyun.com/document_detail/111858.html). If you have any feedback or questions, you can join the DingTalk group (group number: 31045006299).
        Protocol type
        Only NFSv3 is supported.
        Others
        Only one protocol service can be created for a CPFS file system.
        A protocol service can use a maximum of 32 IP addresses that are allocated by a specified vSwitch. Make sure that the vSwitch can provide sufficient IP addresses.
        
        @param request: CreateProtocolServiceRequest
        @return: CreateProtocolServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_protocol_service_with_options(request, runtime)

    async def create_protocol_service_async(
        self,
        request: nas20170626_models.CreateProtocolServiceRequest,
    ) -> nas20170626_models.CreateProtocolServiceResponse:
        """
        @summary Creates a protocol service for a Cloud Parallel File Storage (CPFS) file system. The creation takes about 5 to 10 minutes.
        
        @description    This operation is available only to CPFS file systems on the China site (aliyun.com).
        Only CPFS V2.3.0 and later support protocol services. You can query the version information of the file system by calling the [DescribeFileSystems](~~2402188.~~) operation.
        Protocol service types
        Protocol services are classified into general-purpose protocol services and cache protocol services. Different from general-purpose protocol services, cache protocol services can cache hot data. If data exists in the cache, the bandwidth of the cache protocol service may exceed the bandwidth of the CPFS file system, reaching the maximum bandwidth specified for the protocol service.
        General-purpose protocol services: provide NFS access and [directory-level mount targets](https://help.aliyun.com/document_detail/427175.html) for CPFS file systems. You do not need to configure a POSIX client to manage clusters. General-purpose protocol services are provided free of charge.
        Cache protocol services: provide the server memory cache based on the least recently used (LRU) policy. When data is cached in the memory, CPFS provides higher internal bandwidth. Cache protocol services are divided into Cache L1 and Cache L2 specifications. The differences are the internal bandwidth size and memory cache size.
        >   Note You are charged for using cache protocol services, which are in invitational preview. For more information about the billing method of cache protocol services, see [Billable items](https://help.aliyun.com/document_detail/111858.html). If you have any feedback or questions, you can join the DingTalk group (group number: 31045006299).
        Protocol type
        Only NFSv3 is supported.
        Others
        Only one protocol service can be created for a CPFS file system.
        A protocol service can use a maximum of 32 IP addresses that are allocated by a specified vSwitch. Make sure that the vSwitch can provide sufficient IP addresses.
        
        @param request: CreateProtocolServiceRequest
        @return: CreateProtocolServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_protocol_service_with_options_async(request, runtime)

    def create_recycle_bin_delete_job_with_options(
        self,
        request: nas20170626_models.CreateRecycleBinDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateRecycleBinDeleteJobResponse:
        """
        @summary Creates a job to permanently delete a file or directory from the recycle bin.
        
        @description    Only General-purpose NAS file systems support this operation.
        If you permanently delete a directory, the files in the directory are recursively cleared.
        You can run only one job at a time for a single file system to permanently delete the files from the file system. You cannot create a restoration or deletion job when a file or directory is being deleted.
        
        @param request: CreateRecycleBinDeleteJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRecycleBinDeleteJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecycleBinDeleteJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateRecycleBinDeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_recycle_bin_delete_job_with_options_async(
        self,
        request: nas20170626_models.CreateRecycleBinDeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateRecycleBinDeleteJobResponse:
        """
        @summary Creates a job to permanently delete a file or directory from the recycle bin.
        
        @description    Only General-purpose NAS file systems support this operation.
        If you permanently delete a directory, the files in the directory are recursively cleared.
        You can run only one job at a time for a single file system to permanently delete the files from the file system. You cannot create a restoration or deletion job when a file or directory is being deleted.
        
        @param request: CreateRecycleBinDeleteJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRecycleBinDeleteJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecycleBinDeleteJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateRecycleBinDeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_recycle_bin_delete_job(
        self,
        request: nas20170626_models.CreateRecycleBinDeleteJobRequest,
    ) -> nas20170626_models.CreateRecycleBinDeleteJobResponse:
        """
        @summary Creates a job to permanently delete a file or directory from the recycle bin.
        
        @description    Only General-purpose NAS file systems support this operation.
        If you permanently delete a directory, the files in the directory are recursively cleared.
        You can run only one job at a time for a single file system to permanently delete the files from the file system. You cannot create a restoration or deletion job when a file or directory is being deleted.
        
        @param request: CreateRecycleBinDeleteJobRequest
        @return: CreateRecycleBinDeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_recycle_bin_delete_job_with_options(request, runtime)

    async def create_recycle_bin_delete_job_async(
        self,
        request: nas20170626_models.CreateRecycleBinDeleteJobRequest,
    ) -> nas20170626_models.CreateRecycleBinDeleteJobResponse:
        """
        @summary Creates a job to permanently delete a file or directory from the recycle bin.
        
        @description    Only General-purpose NAS file systems support this operation.
        If you permanently delete a directory, the files in the directory are recursively cleared.
        You can run only one job at a time for a single file system to permanently delete the files from the file system. You cannot create a restoration or deletion job when a file or directory is being deleted.
        
        @param request: CreateRecycleBinDeleteJobRequest
        @return: CreateRecycleBinDeleteJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_recycle_bin_delete_job_with_options_async(request, runtime)

    def create_recycle_bin_restore_job_with_options(
        self,
        request: nas20170626_models.CreateRecycleBinRestoreJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateRecycleBinRestoreJobResponse:
        """
        @summary Restores a file or directory from the recycle bin.
        
        @description ### Usage notes
        Only General-purpose NAS file systems support this operation.
        You can run only one job at a time for a single file system to restore files to or clear files from the file system. You cannot create a restore or cleanup job when files are being restored from the recycle bin.
        You can restore only one file or directory in a single restore job. If you restore a specified directory, all files in the directory are recursively restored.
        After files are restored, the data of the files is defragmented. When the data is being defragmented, the read performance is slightly degraded.
        
        @param request: CreateRecycleBinRestoreJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRecycleBinRestoreJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecycleBinRestoreJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateRecycleBinRestoreJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_recycle_bin_restore_job_with_options_async(
        self,
        request: nas20170626_models.CreateRecycleBinRestoreJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateRecycleBinRestoreJobResponse:
        """
        @summary Restores a file or directory from the recycle bin.
        
        @description ### Usage notes
        Only General-purpose NAS file systems support this operation.
        You can run only one job at a time for a single file system to restore files to or clear files from the file system. You cannot create a restore or cleanup job when files are being restored from the recycle bin.
        You can restore only one file or directory in a single restore job. If you restore a specified directory, all files in the directory are recursively restored.
        After files are restored, the data of the files is defragmented. When the data is being defragmented, the read performance is slightly degraded.
        
        @param request: CreateRecycleBinRestoreJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRecycleBinRestoreJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecycleBinRestoreJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateRecycleBinRestoreJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_recycle_bin_restore_job(
        self,
        request: nas20170626_models.CreateRecycleBinRestoreJobRequest,
    ) -> nas20170626_models.CreateRecycleBinRestoreJobResponse:
        """
        @summary Restores a file or directory from the recycle bin.
        
        @description ### Usage notes
        Only General-purpose NAS file systems support this operation.
        You can run only one job at a time for a single file system to restore files to or clear files from the file system. You cannot create a restore or cleanup job when files are being restored from the recycle bin.
        You can restore only one file or directory in a single restore job. If you restore a specified directory, all files in the directory are recursively restored.
        After files are restored, the data of the files is defragmented. When the data is being defragmented, the read performance is slightly degraded.
        
        @param request: CreateRecycleBinRestoreJobRequest
        @return: CreateRecycleBinRestoreJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_recycle_bin_restore_job_with_options(request, runtime)

    async def create_recycle_bin_restore_job_async(
        self,
        request: nas20170626_models.CreateRecycleBinRestoreJobRequest,
    ) -> nas20170626_models.CreateRecycleBinRestoreJobResponse:
        """
        @summary Restores a file or directory from the recycle bin.
        
        @description ### Usage notes
        Only General-purpose NAS file systems support this operation.
        You can run only one job at a time for a single file system to restore files to or clear files from the file system. You cannot create a restore or cleanup job when files are being restored from the recycle bin.
        You can restore only one file or directory in a single restore job. If you restore a specified directory, all files in the directory are recursively restored.
        After files are restored, the data of the files is defragmented. When the data is being defragmented, the read performance is slightly degraded.
        
        @param request: CreateRecycleBinRestoreJobRequest
        @return: CreateRecycleBinRestoreJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_recycle_bin_restore_job_with_options_async(request, runtime)

    def create_snapshot_with_options(
        self,
        request: nas20170626_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateSnapshotResponse:
        """
        @summary Creates a snapshot.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        You can create a maximum of 128 snapshots for a file system.
        The compute node on which a file system is mounted must function as expected. Otherwise, you cannot create a snapshot for the file system.
        You can create only one snapshot for a file system at a time.
        If the file system expires when a snapshot is being created, the file system is released and the snapshot is deleted.
        When you create a snapshot for a file system, the I/O performance of the file system may be degraded for a short period of time. We recommend that you create snapshots during off-peak hours.
        A snapshot is a backup of a file system at a specific point in time. After you create a snapshot, incremental data that is generated in the file system will not be synchronized to the snapshot.
        Manually created snapshots will not be deleted until 15 days after the service is suspended due to overdue payments. We recommend that you delete unnecessary snapshots at regular intervals to prevent extra fees incurred by the snapshots.
        
        @param request: CreateSnapshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: nas20170626_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.CreateSnapshotResponse:
        """
        @summary Creates a snapshot.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        You can create a maximum of 128 snapshots for a file system.
        The compute node on which a file system is mounted must function as expected. Otherwise, you cannot create a snapshot for the file system.
        You can create only one snapshot for a file system at a time.
        If the file system expires when a snapshot is being created, the file system is released and the snapshot is deleted.
        When you create a snapshot for a file system, the I/O performance of the file system may be degraded for a short period of time. We recommend that you create snapshots during off-peak hours.
        A snapshot is a backup of a file system at a specific point in time. After you create a snapshot, incremental data that is generated in the file system will not be synchronized to the snapshot.
        Manually created snapshots will not be deleted until 15 days after the service is suspended due to overdue payments. We recommend that you delete unnecessary snapshots at regular intervals to prevent extra fees incurred by the snapshots.
        
        @param request: CreateSnapshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSnapshot',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.CreateSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_snapshot(
        self,
        request: nas20170626_models.CreateSnapshotRequest,
    ) -> nas20170626_models.CreateSnapshotResponse:
        """
        @summary Creates a snapshot.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        You can create a maximum of 128 snapshots for a file system.
        The compute node on which a file system is mounted must function as expected. Otherwise, you cannot create a snapshot for the file system.
        You can create only one snapshot for a file system at a time.
        If the file system expires when a snapshot is being created, the file system is released and the snapshot is deleted.
        When you create a snapshot for a file system, the I/O performance of the file system may be degraded for a short period of time. We recommend that you create snapshots during off-peak hours.
        A snapshot is a backup of a file system at a specific point in time. After you create a snapshot, incremental data that is generated in the file system will not be synchronized to the snapshot.
        Manually created snapshots will not be deleted until 15 days after the service is suspended due to overdue payments. We recommend that you delete unnecessary snapshots at regular intervals to prevent extra fees incurred by the snapshots.
        
        @param request: CreateSnapshotRequest
        @return: CreateSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    async def create_snapshot_async(
        self,
        request: nas20170626_models.CreateSnapshotRequest,
    ) -> nas20170626_models.CreateSnapshotResponse:
        """
        @summary Creates a snapshot.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        You can create a maximum of 128 snapshots for a file system.
        The compute node on which a file system is mounted must function as expected. Otherwise, you cannot create a snapshot for the file system.
        You can create only one snapshot for a file system at a time.
        If the file system expires when a snapshot is being created, the file system is released and the snapshot is deleted.
        When you create a snapshot for a file system, the I/O performance of the file system may be degraded for a short period of time. We recommend that you create snapshots during off-peak hours.
        A snapshot is a backup of a file system at a specific point in time. After you create a snapshot, incremental data that is generated in the file system will not be synchronized to the snapshot.
        Manually created snapshots will not be deleted until 15 days after the service is suspended due to overdue payments. We recommend that you delete unnecessary snapshots at regular intervals to prevent extra fees incurred by the snapshots.
        
        @param request: CreateSnapshotRequest
        @return: CreateSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_snapshot_with_options_async(request, runtime)

    def delete_access_group_with_options(
        self,
        request: nas20170626_models.DeleteAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAccessGroupResponse:
        """
        @summary Deletes a permission group.
        
        @description The default permission group (DEFAULT_VPC_GROUP_NAME) cannot be deleted.
        
        @param request: DeleteAccessGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccessGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_group_with_options_async(
        self,
        request: nas20170626_models.DeleteAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAccessGroupResponse:
        """
        @summary Deletes a permission group.
        
        @description The default permission group (DEFAULT_VPC_GROUP_NAME) cannot be deleted.
        
        @param request: DeleteAccessGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccessGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_group(
        self,
        request: nas20170626_models.DeleteAccessGroupRequest,
    ) -> nas20170626_models.DeleteAccessGroupResponse:
        """
        @summary Deletes a permission group.
        
        @description The default permission group (DEFAULT_VPC_GROUP_NAME) cannot be deleted.
        
        @param request: DeleteAccessGroupRequest
        @return: DeleteAccessGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_access_group_with_options(request, runtime)

    async def delete_access_group_async(
        self,
        request: nas20170626_models.DeleteAccessGroupRequest,
    ) -> nas20170626_models.DeleteAccessGroupResponse:
        """
        @summary Deletes a permission group.
        
        @description The default permission group (DEFAULT_VPC_GROUP_NAME) cannot be deleted.
        
        @param request: DeleteAccessGroupRequest
        @return: DeleteAccessGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_group_with_options_async(request, runtime)

    def delete_access_point_with_options(
        self,
        request: nas20170626_models.DeleteAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAccessPointResponse:
        """
        @summary Deletes an access point.
        
        @description    Only General-purpose Network File System (NFS) file systems support access points.
        After an access point is deleted, all I/O operations that are being performed on the directory accessed over the access point are interrupted immediately. Exercise caution when you perform this operation.
        
        @param request: DeleteAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessPoint',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_point_with_options_async(
        self,
        request: nas20170626_models.DeleteAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAccessPointResponse:
        """
        @summary Deletes an access point.
        
        @description    Only General-purpose Network File System (NFS) file systems support access points.
        After an access point is deleted, all I/O operations that are being performed on the directory accessed over the access point are interrupted immediately. Exercise caution when you perform this operation.
        
        @param request: DeleteAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessPoint',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_point(
        self,
        request: nas20170626_models.DeleteAccessPointRequest,
    ) -> nas20170626_models.DeleteAccessPointResponse:
        """
        @summary Deletes an access point.
        
        @description    Only General-purpose Network File System (NFS) file systems support access points.
        After an access point is deleted, all I/O operations that are being performed on the directory accessed over the access point are interrupted immediately. Exercise caution when you perform this operation.
        
        @param request: DeleteAccessPointRequest
        @return: DeleteAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_access_point_with_options(request, runtime)

    async def delete_access_point_async(
        self,
        request: nas20170626_models.DeleteAccessPointRequest,
    ) -> nas20170626_models.DeleteAccessPointResponse:
        """
        @summary Deletes an access point.
        
        @description    Only General-purpose Network File System (NFS) file systems support access points.
        After an access point is deleted, all I/O operations that are being performed on the directory accessed over the access point are interrupted immediately. Exercise caution when you perform this operation.
        
        @param request: DeleteAccessPointRequest
        @return: DeleteAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_point_with_options_async(request, runtime)

    def delete_access_rule_with_options(
        self,
        request: nas20170626_models.DeleteAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAccessRuleResponse:
        """
        @summary Deletes a rule from a permission group.
        
        @description Rules in the default permission group (DEFAULT_VPC_GROUP_NAME) cannot be deleted.
        
        @param request: DeleteAccessRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccessRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_access_rule_with_options_async(
        self,
        request: nas20170626_models.DeleteAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAccessRuleResponse:
        """
        @summary Deletes a rule from a permission group.
        
        @description Rules in the default permission group (DEFAULT_VPC_GROUP_NAME) cannot be deleted.
        
        @param request: DeleteAccessRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccessRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_access_rule(
        self,
        request: nas20170626_models.DeleteAccessRuleRequest,
    ) -> nas20170626_models.DeleteAccessRuleResponse:
        """
        @summary Deletes a rule from a permission group.
        
        @description Rules in the default permission group (DEFAULT_VPC_GROUP_NAME) cannot be deleted.
        
        @param request: DeleteAccessRuleRequest
        @return: DeleteAccessRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_access_rule_with_options(request, runtime)

    async def delete_access_rule_async(
        self,
        request: nas20170626_models.DeleteAccessRuleRequest,
    ) -> nas20170626_models.DeleteAccessRuleResponse:
        """
        @summary Deletes a rule from a permission group.
        
        @description Rules in the default permission group (DEFAULT_VPC_GROUP_NAME) cannot be deleted.
        
        @param request: DeleteAccessRuleRequest
        @return: DeleteAccessRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_access_rule_with_options_async(request, runtime)

    def delete_auto_snapshot_policy_with_options(
        self,
        request: nas20170626_models.DeleteAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAutoSnapshotPolicyResponse:
        """
        @summary Deletes an automatic snapshot policy.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        If you delete an automatic snapshot policy that is applied to a file system, snapshots for the file system are no longer created based on the policy.
        
        @param request: DeleteAutoSnapshotPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.DeleteAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteAutoSnapshotPolicyResponse:
        """
        @summary Deletes an automatic snapshot policy.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        If you delete an automatic snapshot policy that is applied to a file system, snapshots for the file system are no longer created based on the policy.
        
        @param request: DeleteAutoSnapshotPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_auto_snapshot_policy(
        self,
        request: nas20170626_models.DeleteAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.DeleteAutoSnapshotPolicyResponse:
        """
        @summary Deletes an automatic snapshot policy.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        If you delete an automatic snapshot policy that is applied to a file system, snapshots for the file system are no longer created based on the policy.
        
        @param request: DeleteAutoSnapshotPolicyRequest
        @return: DeleteAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_snapshot_policy_with_options(request, runtime)

    async def delete_auto_snapshot_policy_async(
        self,
        request: nas20170626_models.DeleteAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.DeleteAutoSnapshotPolicyResponse:
        """
        @summary Deletes an automatic snapshot policy.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        If you delete an automatic snapshot policy that is applied to a file system, snapshots for the file system are no longer created based on the policy.
        
        @param request: DeleteAutoSnapshotPolicyRequest
        @return: DeleteAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_snapshot_policy_with_options_async(request, runtime)

    def delete_data_flow_with_options(
        self,
        request: nas20170626_models.DeleteDataFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteDataFlowResponse:
        """
        @summary Deletes a dataflow.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flows. You can view the version information on the file system details page in the console.
        You can delete the data flows that are only in the `Running` or `Stopped` state.
        After a data flow is deleted, the resources related to the data flow are released and cannot be restored. You must create a data flow again if required.
        
        @param request: DeleteDataFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_flow_with_options_async(
        self,
        request: nas20170626_models.DeleteDataFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteDataFlowResponse:
        """
        @summary Deletes a dataflow.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flows. You can view the version information on the file system details page in the console.
        You can delete the data flows that are only in the `Running` or `Stopped` state.
        After a data flow is deleted, the resources related to the data flow are released and cannot be restored. You must create a data flow again if required.
        
        @param request: DeleteDataFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteDataFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_flow(
        self,
        request: nas20170626_models.DeleteDataFlowRequest,
    ) -> nas20170626_models.DeleteDataFlowResponse:
        """
        @summary Deletes a dataflow.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flows. You can view the version information on the file system details page in the console.
        You can delete the data flows that are only in the `Running` or `Stopped` state.
        After a data flow is deleted, the resources related to the data flow are released and cannot be restored. You must create a data flow again if required.
        
        @param request: DeleteDataFlowRequest
        @return: DeleteDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_flow_with_options(request, runtime)

    async def delete_data_flow_async(
        self,
        request: nas20170626_models.DeleteDataFlowRequest,
    ) -> nas20170626_models.DeleteDataFlowResponse:
        """
        @summary Deletes a dataflow.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flows. You can view the version information on the file system details page in the console.
        You can delete the data flows that are only in the `Running` or `Stopped` state.
        After a data flow is deleted, the resources related to the data flow are released and cannot be restored. You must create a data flow again if required.
        
        @param request: DeleteDataFlowRequest
        @return: DeleteDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_flow_with_options_async(request, runtime)

    def delete_file_system_with_options(
        self,
        request: nas20170626_models.DeleteFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteFileSystemResponse:
        """
        @summary Deletes a file system.
        
        @description    Before you delete a file system, you must delete all mount targets of the file system.
        Before you delete a file system, you must make sure that no lifecycle policy is created for the file system.
        After a file system is deleted, the data on the file system cannot be restored. Proceed with caution.
        
        @param request: DeleteFileSystemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_system_with_options_async(
        self,
        request: nas20170626_models.DeleteFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteFileSystemResponse:
        """
        @summary Deletes a file system.
        
        @description    Before you delete a file system, you must delete all mount targets of the file system.
        Before you delete a file system, you must make sure that no lifecycle policy is created for the file system.
        After a file system is deleted, the data on the file system cannot be restored. Proceed with caution.
        
        @param request: DeleteFileSystemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file_system(
        self,
        request: nas20170626_models.DeleteFileSystemRequest,
    ) -> nas20170626_models.DeleteFileSystemResponse:
        """
        @summary Deletes a file system.
        
        @description    Before you delete a file system, you must delete all mount targets of the file system.
        Before you delete a file system, you must make sure that no lifecycle policy is created for the file system.
        After a file system is deleted, the data on the file system cannot be restored. Proceed with caution.
        
        @param request: DeleteFileSystemRequest
        @return: DeleteFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_file_system_with_options(request, runtime)

    async def delete_file_system_async(
        self,
        request: nas20170626_models.DeleteFileSystemRequest,
    ) -> nas20170626_models.DeleteFileSystemResponse:
        """
        @summary Deletes a file system.
        
        @description    Before you delete a file system, you must delete all mount targets of the file system.
        Before you delete a file system, you must make sure that no lifecycle policy is created for the file system.
        After a file system is deleted, the data on the file system cannot be restored. Proceed with caution.
        
        @param request: DeleteFileSystemRequest
        @return: DeleteFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_file_system_with_options_async(request, runtime)

    def delete_fileset_with_options(
        self,
        request: nas20170626_models.DeleteFilesetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteFilesetResponse:
        """
        @summary Deletes a fileset.
        
        @description    Only Cloud Parallel File Storage (CPFS) for Lingjun V2.7.0 and later support this operation. After you delete a fileset, all data in the fileset is deleted and cannot be restored. Proceed with caution.
        If deletion protection is enabled for the fileset, you must disable deletion protection before you delete the fileset.
        After you delete a fileset of CPFS for Lingjun, the storage space is not immediately released and will be recycled within 24 hours. If you want to release storage space immediately, you can clear the data in the fileset and then delete the fileset. Deleted data cannot be restored. Proceed with caution.
        
        @param request: DeleteFilesetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFilesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileset',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteFilesetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_fileset_with_options_async(
        self,
        request: nas20170626_models.DeleteFilesetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteFilesetResponse:
        """
        @summary Deletes a fileset.
        
        @description    Only Cloud Parallel File Storage (CPFS) for Lingjun V2.7.0 and later support this operation. After you delete a fileset, all data in the fileset is deleted and cannot be restored. Proceed with caution.
        If deletion protection is enabled for the fileset, you must disable deletion protection before you delete the fileset.
        After you delete a fileset of CPFS for Lingjun, the storage space is not immediately released and will be recycled within 24 hours. If you want to release storage space immediately, you can clear the data in the fileset and then delete the fileset. Deleted data cannot be restored. Proceed with caution.
        
        @param request: DeleteFilesetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFilesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileset',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteFilesetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_fileset(
        self,
        request: nas20170626_models.DeleteFilesetRequest,
    ) -> nas20170626_models.DeleteFilesetResponse:
        """
        @summary Deletes a fileset.
        
        @description    Only Cloud Parallel File Storage (CPFS) for Lingjun V2.7.0 and later support this operation. After you delete a fileset, all data in the fileset is deleted and cannot be restored. Proceed with caution.
        If deletion protection is enabled for the fileset, you must disable deletion protection before you delete the fileset.
        After you delete a fileset of CPFS for Lingjun, the storage space is not immediately released and will be recycled within 24 hours. If you want to release storage space immediately, you can clear the data in the fileset and then delete the fileset. Deleted data cannot be restored. Proceed with caution.
        
        @param request: DeleteFilesetRequest
        @return: DeleteFilesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_fileset_with_options(request, runtime)

    async def delete_fileset_async(
        self,
        request: nas20170626_models.DeleteFilesetRequest,
    ) -> nas20170626_models.DeleteFilesetResponse:
        """
        @summary Deletes a fileset.
        
        @description    Only Cloud Parallel File Storage (CPFS) for Lingjun V2.7.0 and later support this operation. After you delete a fileset, all data in the fileset is deleted and cannot be restored. Proceed with caution.
        If deletion protection is enabled for the fileset, you must disable deletion protection before you delete the fileset.
        After you delete a fileset of CPFS for Lingjun, the storage space is not immediately released and will be recycled within 24 hours. If you want to release storage space immediately, you can clear the data in the fileset and then delete the fileset. Deleted data cannot be restored. Proceed with caution.
        
        @param request: DeleteFilesetRequest
        @return: DeleteFilesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_fileset_with_options_async(request, runtime)

    def delete_ldapconfig_with_options(
        self,
        request: nas20170626_models.DeleteLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteLDAPConfigResponse:
        """
        @deprecated OpenAPI DeleteLDAPConfig is deprecated
        
        @summary 删除LDAP配置
        
        @param request: DeleteLDAPConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLDAPConfigResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLDAPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ldapconfig_with_options_async(
        self,
        request: nas20170626_models.DeleteLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteLDAPConfigResponse:
        """
        @deprecated OpenAPI DeleteLDAPConfig is deprecated
        
        @summary 删除LDAP配置
        
        @param request: DeleteLDAPConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLDAPConfigResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLDAPConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ldapconfig(
        self,
        request: nas20170626_models.DeleteLDAPConfigRequest,
    ) -> nas20170626_models.DeleteLDAPConfigResponse:
        """
        @deprecated OpenAPI DeleteLDAPConfig is deprecated
        
        @summary 删除LDAP配置
        
        @param request: DeleteLDAPConfigRequest
        @return: DeleteLDAPConfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_ldapconfig_with_options(request, runtime)

    async def delete_ldapconfig_async(
        self,
        request: nas20170626_models.DeleteLDAPConfigRequest,
    ) -> nas20170626_models.DeleteLDAPConfigResponse:
        """
        @deprecated OpenAPI DeleteLDAPConfig is deprecated
        
        @summary 删除LDAP配置
        
        @param request: DeleteLDAPConfigRequest
        @return: DeleteLDAPConfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_ldapconfig_with_options_async(request, runtime)

    def delete_lifecycle_policy_with_options(
        self,
        request: nas20170626_models.DeleteLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteLifecyclePolicyResponse:
        """
        @summary Deletes a lifecycle policy.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: DeleteLifecyclePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLifecyclePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLifecyclePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_lifecycle_policy_with_options_async(
        self,
        request: nas20170626_models.DeleteLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteLifecyclePolicyResponse:
        """
        @summary Deletes a lifecycle policy.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: DeleteLifecyclePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLifecyclePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLifecyclePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_lifecycle_policy(
        self,
        request: nas20170626_models.DeleteLifecyclePolicyRequest,
    ) -> nas20170626_models.DeleteLifecyclePolicyResponse:
        """
        @summary Deletes a lifecycle policy.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: DeleteLifecyclePolicyRequest
        @return: DeleteLifecyclePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_lifecycle_policy_with_options(request, runtime)

    async def delete_lifecycle_policy_async(
        self,
        request: nas20170626_models.DeleteLifecyclePolicyRequest,
    ) -> nas20170626_models.DeleteLifecyclePolicyResponse:
        """
        @summary Deletes a lifecycle policy.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: DeleteLifecyclePolicyRequest
        @return: DeleteLifecyclePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_lifecycle_policy_with_options_async(request, runtime)

    def delete_log_analysis_with_options(
        self,
        request: nas20170626_models.DeleteLogAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteLogAnalysisResponse:
        """
        @summary Disables log dumping for a General-purpose NAS file system.
        
        @param request: DeleteLogAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLogAnalysisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogAnalysis',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLogAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_log_analysis_with_options_async(
        self,
        request: nas20170626_models.DeleteLogAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteLogAnalysisResponse:
        """
        @summary Disables log dumping for a General-purpose NAS file system.
        
        @param request: DeleteLogAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLogAnalysisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLogAnalysis',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteLogAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_log_analysis(
        self,
        request: nas20170626_models.DeleteLogAnalysisRequest,
    ) -> nas20170626_models.DeleteLogAnalysisResponse:
        """
        @summary Disables log dumping for a General-purpose NAS file system.
        
        @param request: DeleteLogAnalysisRequest
        @return: DeleteLogAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_log_analysis_with_options(request, runtime)

    async def delete_log_analysis_async(
        self,
        request: nas20170626_models.DeleteLogAnalysisRequest,
    ) -> nas20170626_models.DeleteLogAnalysisResponse:
        """
        @summary Disables log dumping for a General-purpose NAS file system.
        
        @param request: DeleteLogAnalysisRequest
        @return: DeleteLogAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_log_analysis_with_options_async(request, runtime)

    def delete_mount_target_with_options(
        self,
        request: nas20170626_models.DeleteMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteMountTargetResponse:
        """
        @summary Deletes a mount target.
        
        @description After you delete a mount target, the mount target cannot be restored. Proceed with caution.
        
        @param request: DeleteMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mount_target_with_options_async(
        self,
        request: nas20170626_models.DeleteMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteMountTargetResponse:
        """
        @summary Deletes a mount target.
        
        @description After you delete a mount target, the mount target cannot be restored. Proceed with caution.
        
        @param request: DeleteMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mount_target(
        self,
        request: nas20170626_models.DeleteMountTargetRequest,
    ) -> nas20170626_models.DeleteMountTargetResponse:
        """
        @summary Deletes a mount target.
        
        @description After you delete a mount target, the mount target cannot be restored. Proceed with caution.
        
        @param request: DeleteMountTargetRequest
        @return: DeleteMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_mount_target_with_options(request, runtime)

    async def delete_mount_target_async(
        self,
        request: nas20170626_models.DeleteMountTargetRequest,
    ) -> nas20170626_models.DeleteMountTargetResponse:
        """
        @summary Deletes a mount target.
        
        @description After you delete a mount target, the mount target cannot be restored. Proceed with caution.
        
        @param request: DeleteMountTargetRequest
        @return: DeleteMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_mount_target_with_options_async(request, runtime)

    def delete_protocol_mount_target_with_options(
        self,
        request: nas20170626_models.DeleteProtocolMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteProtocolMountTargetResponse:
        """
        @summary Deletes an export directory of a protocol service.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: DeleteProtocolMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProtocolMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProtocolMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteProtocolMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_protocol_mount_target_with_options_async(
        self,
        request: nas20170626_models.DeleteProtocolMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteProtocolMountTargetResponse:
        """
        @summary Deletes an export directory of a protocol service.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: DeleteProtocolMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProtocolMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProtocolMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteProtocolMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_protocol_mount_target(
        self,
        request: nas20170626_models.DeleteProtocolMountTargetRequest,
    ) -> nas20170626_models.DeleteProtocolMountTargetResponse:
        """
        @summary Deletes an export directory of a protocol service.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: DeleteProtocolMountTargetRequest
        @return: DeleteProtocolMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_protocol_mount_target_with_options(request, runtime)

    async def delete_protocol_mount_target_async(
        self,
        request: nas20170626_models.DeleteProtocolMountTargetRequest,
    ) -> nas20170626_models.DeleteProtocolMountTargetResponse:
        """
        @summary Deletes an export directory of a protocol service.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: DeleteProtocolMountTargetRequest
        @return: DeleteProtocolMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_protocol_mount_target_with_options_async(request, runtime)

    def delete_protocol_service_with_options(
        self,
        request: nas20170626_models.DeleteProtocolServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteProtocolServiceResponse:
        """
        @summary Deletes a protocol service of a Cloud Parallel File Storage (CPFS) file system.
        
        @description    This operation is available only to CPFS file systems on the China site (aliyun.com).
        When you delete a protocol service, the export directories in the protocol service are also deleted.
        
        @param request: DeleteProtocolServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProtocolServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProtocolService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteProtocolServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_protocol_service_with_options_async(
        self,
        request: nas20170626_models.DeleteProtocolServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteProtocolServiceResponse:
        """
        @summary Deletes a protocol service of a Cloud Parallel File Storage (CPFS) file system.
        
        @description    This operation is available only to CPFS file systems on the China site (aliyun.com).
        When you delete a protocol service, the export directories in the protocol service are also deleted.
        
        @param request: DeleteProtocolServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProtocolServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProtocolService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteProtocolServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_protocol_service(
        self,
        request: nas20170626_models.DeleteProtocolServiceRequest,
    ) -> nas20170626_models.DeleteProtocolServiceResponse:
        """
        @summary Deletes a protocol service of a Cloud Parallel File Storage (CPFS) file system.
        
        @description    This operation is available only to CPFS file systems on the China site (aliyun.com).
        When you delete a protocol service, the export directories in the protocol service are also deleted.
        
        @param request: DeleteProtocolServiceRequest
        @return: DeleteProtocolServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_protocol_service_with_options(request, runtime)

    async def delete_protocol_service_async(
        self,
        request: nas20170626_models.DeleteProtocolServiceRequest,
    ) -> nas20170626_models.DeleteProtocolServiceResponse:
        """
        @summary Deletes a protocol service of a Cloud Parallel File Storage (CPFS) file system.
        
        @description    This operation is available only to CPFS file systems on the China site (aliyun.com).
        When you delete a protocol service, the export directories in the protocol service are also deleted.
        
        @param request: DeleteProtocolServiceRequest
        @return: DeleteProtocolServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_protocol_service_with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: nas20170626_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteSnapshotResponse:
        """
        @summary Deletes a snapshot or cancels a snapshot that is being created.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: DeleteSnapshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: nas20170626_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DeleteSnapshotResponse:
        """
        @summary Deletes a snapshot or cancels a snapshot that is being created.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: DeleteSnapshotRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSnapshotResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshot',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DeleteSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_snapshot(
        self,
        request: nas20170626_models.DeleteSnapshotRequest,
    ) -> nas20170626_models.DeleteSnapshotResponse:
        """
        @summary Deletes a snapshot or cancels a snapshot that is being created.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: DeleteSnapshotRequest
        @return: DeleteSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    async def delete_snapshot_async(
        self,
        request: nas20170626_models.DeleteSnapshotRequest,
    ) -> nas20170626_models.DeleteSnapshotResponse:
        """
        @summary Deletes a snapshot or cancels a snapshot that is being created.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: DeleteSnapshotRequest
        @return: DeleteSnapshotResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_with_options_async(request, runtime)

    def describe_access_groups_with_options(
        self,
        request: nas20170626_models.DescribeAccessGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAccessGroupsResponse:
        """
        @summary Queries permission groups.
        
        @param request: DescribeAccessGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccessGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.use_utcdate_time):
            query['UseUTCDateTime'] = request.use_utcdate_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessGroups',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_groups_with_options_async(
        self,
        request: nas20170626_models.DescribeAccessGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAccessGroupsResponse:
        """
        @summary Queries permission groups.
        
        @param request: DescribeAccessGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccessGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.use_utcdate_time):
            query['UseUTCDateTime'] = request.use_utcdate_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessGroups',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_groups(
        self,
        request: nas20170626_models.DescribeAccessGroupsRequest,
    ) -> nas20170626_models.DescribeAccessGroupsResponse:
        """
        @summary Queries permission groups.
        
        @param request: DescribeAccessGroupsRequest
        @return: DescribeAccessGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_access_groups_with_options(request, runtime)

    async def describe_access_groups_async(
        self,
        request: nas20170626_models.DescribeAccessGroupsRequest,
    ) -> nas20170626_models.DescribeAccessGroupsResponse:
        """
        @summary Queries permission groups.
        
        @param request: DescribeAccessGroupsRequest
        @return: DescribeAccessGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_groups_with_options_async(request, runtime)

    def describe_access_point_with_options(
        self,
        request: nas20170626_models.DescribeAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAccessPointResponse:
        """
        @summary Queries the details of an access point.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: DescribeAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessPoint',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_point_with_options_async(
        self,
        request: nas20170626_models.DescribeAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAccessPointResponse:
        """
        @summary Queries the details of an access point.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: DescribeAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessPoint',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_point(
        self,
        request: nas20170626_models.DescribeAccessPointRequest,
    ) -> nas20170626_models.DescribeAccessPointResponse:
        """
        @summary Queries the details of an access point.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: DescribeAccessPointRequest
        @return: DescribeAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_access_point_with_options(request, runtime)

    async def describe_access_point_async(
        self,
        request: nas20170626_models.DescribeAccessPointRequest,
    ) -> nas20170626_models.DescribeAccessPointResponse:
        """
        @summary Queries the details of an access point.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: DescribeAccessPointRequest
        @return: DescribeAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_point_with_options_async(request, runtime)

    def describe_access_points_with_options(
        self,
        request: nas20170626_models.DescribeAccessPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAccessPointsResponse:
        """
        @summary Queries the information about an access point.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: DescribeAccessPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccessPointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group):
            query['AccessGroup'] = request.access_group
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessPoints',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessPointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_points_with_options_async(
        self,
        request: nas20170626_models.DescribeAccessPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAccessPointsResponse:
        """
        @summary Queries the information about an access point.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: DescribeAccessPointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccessPointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group):
            query['AccessGroup'] = request.access_group
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessPoints',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessPointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_points(
        self,
        request: nas20170626_models.DescribeAccessPointsRequest,
    ) -> nas20170626_models.DescribeAccessPointsResponse:
        """
        @summary Queries the information about an access point.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: DescribeAccessPointsRequest
        @return: DescribeAccessPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_access_points_with_options(request, runtime)

    async def describe_access_points_async(
        self,
        request: nas20170626_models.DescribeAccessPointsRequest,
    ) -> nas20170626_models.DescribeAccessPointsResponse:
        """
        @summary Queries the information about an access point.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: DescribeAccessPointsRequest
        @return: DescribeAccessPointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_points_with_options_async(request, runtime)

    def describe_access_rules_with_options(
        self,
        request: nas20170626_models.DescribeAccessRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAccessRulesResponse:
        """
        @summary Queries the information about rules in a permission group.
        
        @param request: DescribeAccessRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccessRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessRules',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_rules_with_options_async(
        self,
        request: nas20170626_models.DescribeAccessRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAccessRulesResponse:
        """
        @summary Queries the information about rules in a permission group.
        
        @param request: DescribeAccessRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccessRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessRules',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAccessRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_rules(
        self,
        request: nas20170626_models.DescribeAccessRulesRequest,
    ) -> nas20170626_models.DescribeAccessRulesResponse:
        """
        @summary Queries the information about rules in a permission group.
        
        @param request: DescribeAccessRulesRequest
        @return: DescribeAccessRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_access_rules_with_options(request, runtime)

    async def describe_access_rules_async(
        self,
        request: nas20170626_models.DescribeAccessRulesRequest,
    ) -> nas20170626_models.DescribeAccessRulesResponse:
        """
        @summary Queries the information about rules in a permission group.
        
        @param request: DescribeAccessRulesRequest
        @return: DescribeAccessRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_rules_with_options_async(request, runtime)

    def describe_auto_snapshot_policies_with_options(
        self,
        request: nas20170626_models.DescribeAutoSnapshotPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAutoSnapshotPoliciesResponse:
        """
        @summary Queries automatic snapshot policies.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: DescribeAutoSnapshotPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoSnapshotPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoSnapshotPolicies',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAutoSnapshotPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_snapshot_policies_with_options_async(
        self,
        request: nas20170626_models.DescribeAutoSnapshotPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAutoSnapshotPoliciesResponse:
        """
        @summary Queries automatic snapshot policies.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: DescribeAutoSnapshotPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoSnapshotPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoSnapshotPolicies',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAutoSnapshotPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_snapshot_policies(
        self,
        request: nas20170626_models.DescribeAutoSnapshotPoliciesRequest,
    ) -> nas20170626_models.DescribeAutoSnapshotPoliciesResponse:
        """
        @summary Queries automatic snapshot policies.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: DescribeAutoSnapshotPoliciesRequest
        @return: DescribeAutoSnapshotPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_snapshot_policies_with_options(request, runtime)

    async def describe_auto_snapshot_policies_async(
        self,
        request: nas20170626_models.DescribeAutoSnapshotPoliciesRequest,
    ) -> nas20170626_models.DescribeAutoSnapshotPoliciesResponse:
        """
        @summary Queries automatic snapshot policies.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: DescribeAutoSnapshotPoliciesRequest
        @return: DescribeAutoSnapshotPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_snapshot_policies_with_options_async(request, runtime)

    def describe_auto_snapshot_tasks_with_options(
        self,
        request: nas20170626_models.DescribeAutoSnapshotTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAutoSnapshotTasksResponse:
        """
        @summary Queries automatic snapshot tasks.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        
        @param request: DescribeAutoSnapshotTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoSnapshotTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_ids):
            query['AutoSnapshotPolicyIds'] = request.auto_snapshot_policy_ids
        if not UtilClient.is_unset(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoSnapshotTasks',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAutoSnapshotTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_auto_snapshot_tasks_with_options_async(
        self,
        request: nas20170626_models.DescribeAutoSnapshotTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeAutoSnapshotTasksResponse:
        """
        @summary Queries automatic snapshot tasks.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        
        @param request: DescribeAutoSnapshotTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAutoSnapshotTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_ids):
            query['AutoSnapshotPolicyIds'] = request.auto_snapshot_policy_ids
        if not UtilClient.is_unset(request.file_system_ids):
            query['FileSystemIds'] = request.file_system_ids
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoSnapshotTasks',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeAutoSnapshotTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_auto_snapshot_tasks(
        self,
        request: nas20170626_models.DescribeAutoSnapshotTasksRequest,
    ) -> nas20170626_models.DescribeAutoSnapshotTasksResponse:
        """
        @summary Queries automatic snapshot tasks.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        
        @param request: DescribeAutoSnapshotTasksRequest
        @return: DescribeAutoSnapshotTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_snapshot_tasks_with_options(request, runtime)

    async def describe_auto_snapshot_tasks_async(
        self,
        request: nas20170626_models.DescribeAutoSnapshotTasksRequest,
    ) -> nas20170626_models.DescribeAutoSnapshotTasksResponse:
        """
        @summary Queries automatic snapshot tasks.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support the snapshot feature.
        
        @param request: DescribeAutoSnapshotTasksRequest
        @return: DescribeAutoSnapshotTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_snapshot_tasks_with_options_async(request, runtime)

    def describe_black_list_clients_with_options(
        self,
        request: nas20170626_models.DescribeBlackListClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeBlackListClientsResponse:
        """
        @deprecated OpenAPI DescribeBlackListClients is deprecated
        
        @summary Queries the status of clients in the blacklist of a Cloud Parallel File Storage (CPFS) file system.
        
        @description The API operation is available only for CPFS file systems.
        
        @param request: DescribeBlackListClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBlackListClientsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlackListClients',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeBlackListClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_black_list_clients_with_options_async(
        self,
        request: nas20170626_models.DescribeBlackListClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeBlackListClientsResponse:
        """
        @deprecated OpenAPI DescribeBlackListClients is deprecated
        
        @summary Queries the status of clients in the blacklist of a Cloud Parallel File Storage (CPFS) file system.
        
        @description The API operation is available only for CPFS file systems.
        
        @param request: DescribeBlackListClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBlackListClientsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBlackListClients',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeBlackListClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_black_list_clients(
        self,
        request: nas20170626_models.DescribeBlackListClientsRequest,
    ) -> nas20170626_models.DescribeBlackListClientsResponse:
        """
        @deprecated OpenAPI DescribeBlackListClients is deprecated
        
        @summary Queries the status of clients in the blacklist of a Cloud Parallel File Storage (CPFS) file system.
        
        @description The API operation is available only for CPFS file systems.
        
        @param request: DescribeBlackListClientsRequest
        @return: DescribeBlackListClientsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_black_list_clients_with_options(request, runtime)

    async def describe_black_list_clients_async(
        self,
        request: nas20170626_models.DescribeBlackListClientsRequest,
    ) -> nas20170626_models.DescribeBlackListClientsResponse:
        """
        @deprecated OpenAPI DescribeBlackListClients is deprecated
        
        @summary Queries the status of clients in the blacklist of a Cloud Parallel File Storage (CPFS) file system.
        
        @description The API operation is available only for CPFS file systems.
        
        @param request: DescribeBlackListClientsRequest
        @return: DescribeBlackListClientsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_black_list_clients_with_options_async(request, runtime)

    def describe_data_flow_sub_tasks_with_options(
        self,
        request: nas20170626_models.DescribeDataFlowSubTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeDataFlowSubTasksResponse:
        """
        @summary Queries data flow subtasks in batches.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.6.0 and later support this operation. You can view the version information on the file system details page in the console.
        
        @param request: DescribeDataFlowSubTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataFlowSubTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataFlowSubTasks',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDataFlowSubTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_flow_sub_tasks_with_options_async(
        self,
        request: nas20170626_models.DescribeDataFlowSubTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeDataFlowSubTasksResponse:
        """
        @summary Queries data flow subtasks in batches.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.6.0 and later support this operation. You can view the version information on the file system details page in the console.
        
        @param request: DescribeDataFlowSubTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataFlowSubTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataFlowSubTasks',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDataFlowSubTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_flow_sub_tasks(
        self,
        request: nas20170626_models.DescribeDataFlowSubTasksRequest,
    ) -> nas20170626_models.DescribeDataFlowSubTasksResponse:
        """
        @summary Queries data flow subtasks in batches.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.6.0 and later support this operation. You can view the version information on the file system details page in the console.
        
        @param request: DescribeDataFlowSubTasksRequest
        @return: DescribeDataFlowSubTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_flow_sub_tasks_with_options(request, runtime)

    async def describe_data_flow_sub_tasks_async(
        self,
        request: nas20170626_models.DescribeDataFlowSubTasksRequest,
    ) -> nas20170626_models.DescribeDataFlowSubTasksResponse:
        """
        @summary Queries data flow subtasks in batches.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.6.0 and later support this operation. You can view the version information on the file system details page in the console.
        
        @param request: DescribeDataFlowSubTasksRequest
        @return: DescribeDataFlowSubTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_flow_sub_tasks_with_options_async(request, runtime)

    def describe_data_flow_tasks_with_options(
        self,
        request: nas20170626_models.DescribeDataFlowTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeDataFlowTasksResponse:
        """
        @summary Queries the details of data flow tasks.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support query of data flow tasks. You can view the version information on the file system details page in the console.
        
        @param request: DescribeDataFlowTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataFlowTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataFlowTasks',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDataFlowTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_flow_tasks_with_options_async(
        self,
        request: nas20170626_models.DescribeDataFlowTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeDataFlowTasksResponse:
        """
        @summary Queries the details of data flow tasks.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support query of data flow tasks. You can view the version information on the file system details page in the console.
        
        @param request: DescribeDataFlowTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataFlowTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataFlowTasks',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDataFlowTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_flow_tasks(
        self,
        request: nas20170626_models.DescribeDataFlowTasksRequest,
    ) -> nas20170626_models.DescribeDataFlowTasksResponse:
        """
        @summary Queries the details of data flow tasks.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support query of data flow tasks. You can view the version information on the file system details page in the console.
        
        @param request: DescribeDataFlowTasksRequest
        @return: DescribeDataFlowTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_flow_tasks_with_options(request, runtime)

    async def describe_data_flow_tasks_async(
        self,
        request: nas20170626_models.DescribeDataFlowTasksRequest,
    ) -> nas20170626_models.DescribeDataFlowTasksResponse:
        """
        @summary Queries the details of data flow tasks.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support query of data flow tasks. You can view the version information on the file system details page in the console.
        
        @param request: DescribeDataFlowTasksRequest
        @return: DescribeDataFlowTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_flow_tasks_with_options_async(request, runtime)

    def describe_data_flows_with_options(
        self,
        request: nas20170626_models.DescribeDataFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeDataFlowsResponse:
        """
        @summary Queries the dataflows of a CPFS file system.
        
        @description    Only CPFS for LINGJUN V2.4.0 and later support data flows. You can view the version information on the file system details page in the console.
        In Filters, FsetIds, DataFlowlds, SourceStorage, ThroughputList, and Status support exact match only. FileSystemPath, Description, and SourceStoragePath support fuzzy match.
        Combined query is supported.
        
        @param request: DescribeDataFlowsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataFlowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataFlows',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDataFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_flows_with_options_async(
        self,
        request: nas20170626_models.DescribeDataFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeDataFlowsResponse:
        """
        @summary Queries the dataflows of a CPFS file system.
        
        @description    Only CPFS for LINGJUN V2.4.0 and later support data flows. You can view the version information on the file system details page in the console.
        In Filters, FsetIds, DataFlowlds, SourceStorage, ThroughputList, and Status support exact match only. FileSystemPath, Description, and SourceStoragePath support fuzzy match.
        Combined query is supported.
        
        @param request: DescribeDataFlowsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDataFlowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDataFlows',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDataFlowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_data_flows(
        self,
        request: nas20170626_models.DescribeDataFlowsRequest,
    ) -> nas20170626_models.DescribeDataFlowsResponse:
        """
        @summary Queries the dataflows of a CPFS file system.
        
        @description    Only CPFS for LINGJUN V2.4.0 and later support data flows. You can view the version information on the file system details page in the console.
        In Filters, FsetIds, DataFlowlds, SourceStorage, ThroughputList, and Status support exact match only. FileSystemPath, Description, and SourceStoragePath support fuzzy match.
        Combined query is supported.
        
        @param request: DescribeDataFlowsRequest
        @return: DescribeDataFlowsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_data_flows_with_options(request, runtime)

    async def describe_data_flows_async(
        self,
        request: nas20170626_models.DescribeDataFlowsRequest,
    ) -> nas20170626_models.DescribeDataFlowsResponse:
        """
        @summary Queries the dataflows of a CPFS file system.
        
        @description    Only CPFS for LINGJUN V2.4.0 and later support data flows. You can view the version information on the file system details page in the console.
        In Filters, FsetIds, DataFlowlds, SourceStorage, ThroughputList, and Status support exact match only. FileSystemPath, Description, and SourceStoragePath support fuzzy match.
        Combined query is supported.
        
        @param request: DescribeDataFlowsRequest
        @return: DescribeDataFlowsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_flows_with_options_async(request, runtime)

    def describe_dir_quotas_with_options(
        self,
        request: nas20170626_models.DescribeDirQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeDirQuotasResponse:
        """
        @summary Queries the directory quotas of a file system.
        
        @description Only General-purpose NAS file systems support the directory quota feature.
        
        @param request: DescribeDirQuotasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDirQuotasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirQuotas',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDirQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dir_quotas_with_options_async(
        self,
        request: nas20170626_models.DescribeDirQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeDirQuotasResponse:
        """
        @summary Queries the directory quotas of a file system.
        
        @description Only General-purpose NAS file systems support the directory quota feature.
        
        @param request: DescribeDirQuotasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDirQuotasResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirQuotas',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeDirQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dir_quotas(
        self,
        request: nas20170626_models.DescribeDirQuotasRequest,
    ) -> nas20170626_models.DescribeDirQuotasResponse:
        """
        @summary Queries the directory quotas of a file system.
        
        @description Only General-purpose NAS file systems support the directory quota feature.
        
        @param request: DescribeDirQuotasRequest
        @return: DescribeDirQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dir_quotas_with_options(request, runtime)

    async def describe_dir_quotas_async(
        self,
        request: nas20170626_models.DescribeDirQuotasRequest,
    ) -> nas20170626_models.DescribeDirQuotasResponse:
        """
        @summary Queries the directory quotas of a file system.
        
        @description Only General-purpose NAS file systems support the directory quota feature.
        
        @param request: DescribeDirQuotasRequest
        @return: DescribeDirQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dir_quotas_with_options_async(request, runtime)

    def describe_file_system_statistics_with_options(
        self,
        request: nas20170626_models.DescribeFileSystemStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeFileSystemStatisticsResponse:
        """
        @deprecated OpenAPI DescribeFileSystemStatistics is deprecated, please use NAS::2017-06-26::DescribeResourceStatistics instead.
        
        @summary Queries the statistics of file systems that are owned by the current account.
        
        @param request: DescribeFileSystemStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFileSystemStatisticsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFileSystemStatistics',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFileSystemStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_file_system_statistics_with_options_async(
        self,
        request: nas20170626_models.DescribeFileSystemStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeFileSystemStatisticsResponse:
        """
        @deprecated OpenAPI DescribeFileSystemStatistics is deprecated, please use NAS::2017-06-26::DescribeResourceStatistics instead.
        
        @summary Queries the statistics of file systems that are owned by the current account.
        
        @param request: DescribeFileSystemStatisticsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFileSystemStatisticsResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFileSystemStatistics',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFileSystemStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_file_system_statistics(
        self,
        request: nas20170626_models.DescribeFileSystemStatisticsRequest,
    ) -> nas20170626_models.DescribeFileSystemStatisticsResponse:
        """
        @deprecated OpenAPI DescribeFileSystemStatistics is deprecated, please use NAS::2017-06-26::DescribeResourceStatistics instead.
        
        @summary Queries the statistics of file systems that are owned by the current account.
        
        @param request: DescribeFileSystemStatisticsRequest
        @return: DescribeFileSystemStatisticsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_file_system_statistics_with_options(request, runtime)

    async def describe_file_system_statistics_async(
        self,
        request: nas20170626_models.DescribeFileSystemStatisticsRequest,
    ) -> nas20170626_models.DescribeFileSystemStatisticsResponse:
        """
        @deprecated OpenAPI DescribeFileSystemStatistics is deprecated, please use NAS::2017-06-26::DescribeResourceStatistics instead.
        
        @summary Queries the statistics of file systems that are owned by the current account.
        
        @param request: DescribeFileSystemStatisticsRequest
        @return: DescribeFileSystemStatisticsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_file_system_statistics_with_options_async(request, runtime)

    def describe_file_systems_with_options(
        self,
        request: nas20170626_models.DescribeFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeFileSystemsResponse:
        """
        @summary Queries file systems.
        
        @param request: DescribeFileSystemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFileSystemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFileSystems',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFileSystemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_file_systems_with_options_async(
        self,
        request: nas20170626_models.DescribeFileSystemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeFileSystemsResponse:
        """
        @summary Queries file systems.
        
        @param request: DescribeFileSystemsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFileSystemsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFileSystems',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFileSystemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_file_systems(
        self,
        request: nas20170626_models.DescribeFileSystemsRequest,
    ) -> nas20170626_models.DescribeFileSystemsResponse:
        """
        @summary Queries file systems.
        
        @param request: DescribeFileSystemsRequest
        @return: DescribeFileSystemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_file_systems_with_options(request, runtime)

    async def describe_file_systems_async(
        self,
        request: nas20170626_models.DescribeFileSystemsRequest,
    ) -> nas20170626_models.DescribeFileSystemsResponse:
        """
        @summary Queries file systems.
        
        @param request: DescribeFileSystemsRequest
        @return: DescribeFileSystemsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_file_systems_with_options_async(request, runtime)

    def describe_filesets_with_options(
        self,
        request: nas20170626_models.DescribeFilesetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeFilesetsResponse:
        """
        @summary Queries the information about created filesets.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation. You can view the version information on the file system details page in the console.
        In Filters, FsetIds supports exact match only. FileSystemPath and Description support fuzzy match.
        Combined query is supported.
        
        @param request: DescribeFilesetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFilesetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by_field):
            query['OrderByField'] = request.order_by_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFilesets',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFilesetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_filesets_with_options_async(
        self,
        request: nas20170626_models.DescribeFilesetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeFilesetsResponse:
        """
        @summary Queries the information about created filesets.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation. You can view the version information on the file system details page in the console.
        In Filters, FsetIds supports exact match only. FileSystemPath and Description support fuzzy match.
        Combined query is supported.
        
        @param request: DescribeFilesetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFilesetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by_field):
            query['OrderByField'] = request.order_by_field
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFilesets',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeFilesetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_filesets(
        self,
        request: nas20170626_models.DescribeFilesetsRequest,
    ) -> nas20170626_models.DescribeFilesetsResponse:
        """
        @summary Queries the information about created filesets.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation. You can view the version information on the file system details page in the console.
        In Filters, FsetIds supports exact match only. FileSystemPath and Description support fuzzy match.
        Combined query is supported.
        
        @param request: DescribeFilesetsRequest
        @return: DescribeFilesetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_filesets_with_options(request, runtime)

    async def describe_filesets_async(
        self,
        request: nas20170626_models.DescribeFilesetsRequest,
    ) -> nas20170626_models.DescribeFilesetsResponse:
        """
        @summary Queries the information about created filesets.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation. You can view the version information on the file system details page in the console.
        In Filters, FsetIds supports exact match only. FileSystemPath and Description support fuzzy match.
        Combined query is supported.
        
        @param request: DescribeFilesetsRequest
        @return: DescribeFilesetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_filesets_with_options_async(request, runtime)

    def describe_lifecycle_policies_with_options(
        self,
        request: nas20170626_models.DescribeLifecyclePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeLifecyclePoliciesResponse:
        """
        @summary Queries lifecycle policies.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: DescribeLifecyclePoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLifecyclePoliciesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecyclePolicies',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLifecyclePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lifecycle_policies_with_options_async(
        self,
        request: nas20170626_models.DescribeLifecyclePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeLifecyclePoliciesResponse:
        """
        @summary Queries lifecycle policies.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: DescribeLifecyclePoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLifecyclePoliciesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecyclePolicies',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLifecyclePoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lifecycle_policies(
        self,
        request: nas20170626_models.DescribeLifecyclePoliciesRequest,
    ) -> nas20170626_models.DescribeLifecyclePoliciesResponse:
        """
        @summary Queries lifecycle policies.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: DescribeLifecyclePoliciesRequest
        @return: DescribeLifecyclePoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_lifecycle_policies_with_options(request, runtime)

    async def describe_lifecycle_policies_async(
        self,
        request: nas20170626_models.DescribeLifecyclePoliciesRequest,
    ) -> nas20170626_models.DescribeLifecyclePoliciesResponse:
        """
        @summary Queries lifecycle policies.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: DescribeLifecyclePoliciesRequest
        @return: DescribeLifecyclePoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_lifecycle_policies_with_options_async(request, runtime)

    def describe_log_analysis_with_options(
        self,
        request: nas20170626_models.DescribeLogAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeLogAnalysisResponse:
        """
        @summary Queries the log dump information configured in log analysis.
        
        @param request: DescribeLogAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogAnalysisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogAnalysis',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLogAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_analysis_with_options_async(
        self,
        request: nas20170626_models.DescribeLogAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeLogAnalysisResponse:
        """
        @summary Queries the log dump information configured in log analysis.
        
        @param request: DescribeLogAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogAnalysisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogAnalysis',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeLogAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_analysis(
        self,
        request: nas20170626_models.DescribeLogAnalysisRequest,
    ) -> nas20170626_models.DescribeLogAnalysisResponse:
        """
        @summary Queries the log dump information configured in log analysis.
        
        @param request: DescribeLogAnalysisRequest
        @return: DescribeLogAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_log_analysis_with_options(request, runtime)

    async def describe_log_analysis_async(
        self,
        request: nas20170626_models.DescribeLogAnalysisRequest,
    ) -> nas20170626_models.DescribeLogAnalysisResponse:
        """
        @summary Queries the log dump information configured in log analysis.
        
        @param request: DescribeLogAnalysisRequest
        @return: DescribeLogAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_analysis_with_options_async(request, runtime)

    def describe_mount_targets_with_options(
        self,
        request: nas20170626_models.DescribeMountTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeMountTargetsResponse:
        """
        @summary Queries mount targets.
        
        @param request: DescribeMountTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMountTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dual_stack_mount_target_domain):
            query['DualStackMountTargetDomain'] = request.dual_stack_mount_target_domain
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMountTargets',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeMountTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mount_targets_with_options_async(
        self,
        request: nas20170626_models.DescribeMountTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeMountTargetsResponse:
        """
        @summary Queries mount targets.
        
        @param request: DescribeMountTargetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMountTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dual_stack_mount_target_domain):
            query['DualStackMountTargetDomain'] = request.dual_stack_mount_target_domain
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMountTargets',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeMountTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mount_targets(
        self,
        request: nas20170626_models.DescribeMountTargetsRequest,
    ) -> nas20170626_models.DescribeMountTargetsResponse:
        """
        @summary Queries mount targets.
        
        @param request: DescribeMountTargetsRequest
        @return: DescribeMountTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_mount_targets_with_options(request, runtime)

    async def describe_mount_targets_async(
        self,
        request: nas20170626_models.DescribeMountTargetsRequest,
    ) -> nas20170626_models.DescribeMountTargetsResponse:
        """
        @summary Queries mount targets.
        
        @param request: DescribeMountTargetsRequest
        @return: DescribeMountTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_mount_targets_with_options_async(request, runtime)

    def describe_mounted_clients_with_options(
        self,
        request: nas20170626_models.DescribeMountedClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeMountedClientsResponse:
        """
        @summary Queries the clients on which a file system is mounted.
        
        @description    Only General-purpose NAS file systems support this operation.
        This operation returns the clients that have accessed the specified file system within the last minute. If the file system is mounted on a client but the client did not access the file system within the last minute, the client is not included in the returned information.
        
        @param request: DescribeMountedClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMountedClientsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMountedClients',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeMountedClientsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_mounted_clients_with_options_async(
        self,
        request: nas20170626_models.DescribeMountedClientsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeMountedClientsResponse:
        """
        @summary Queries the clients on which a file system is mounted.
        
        @description    Only General-purpose NAS file systems support this operation.
        This operation returns the clients that have accessed the specified file system within the last minute. If the file system is mounted on a client but the client did not access the file system within the last minute, the client is not included in the returned information.
        
        @param request: DescribeMountedClientsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeMountedClientsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMountedClients',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeMountedClientsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_mounted_clients(
        self,
        request: nas20170626_models.DescribeMountedClientsRequest,
    ) -> nas20170626_models.DescribeMountedClientsResponse:
        """
        @summary Queries the clients on which a file system is mounted.
        
        @description    Only General-purpose NAS file systems support this operation.
        This operation returns the clients that have accessed the specified file system within the last minute. If the file system is mounted on a client but the client did not access the file system within the last minute, the client is not included in the returned information.
        
        @param request: DescribeMountedClientsRequest
        @return: DescribeMountedClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_mounted_clients_with_options(request, runtime)

    async def describe_mounted_clients_async(
        self,
        request: nas20170626_models.DescribeMountedClientsRequest,
    ) -> nas20170626_models.DescribeMountedClientsResponse:
        """
        @summary Queries the clients on which a file system is mounted.
        
        @description    Only General-purpose NAS file systems support this operation.
        This operation returns the clients that have accessed the specified file system within the last minute. If the file system is mounted on a client but the client did not access the file system within the last minute, the client is not included in the returned information.
        
        @param request: DescribeMountedClientsRequest
        @return: DescribeMountedClientsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_mounted_clients_with_options_async(request, runtime)

    def describe_nfs_acl_with_options(
        self,
        request: nas20170626_models.DescribeNfsAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeNfsAclResponse:
        """
        @summary Queries whether the NFS ACL feature is enabled for a file system.
        
        @param request: DescribeNfsAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNfsAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNfsAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeNfsAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_nfs_acl_with_options_async(
        self,
        request: nas20170626_models.DescribeNfsAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeNfsAclResponse:
        """
        @summary Queries whether the NFS ACL feature is enabled for a file system.
        
        @param request: DescribeNfsAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNfsAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNfsAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeNfsAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_nfs_acl(
        self,
        request: nas20170626_models.DescribeNfsAclRequest,
    ) -> nas20170626_models.DescribeNfsAclResponse:
        """
        @summary Queries whether the NFS ACL feature is enabled for a file system.
        
        @param request: DescribeNfsAclRequest
        @return: DescribeNfsAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_nfs_acl_with_options(request, runtime)

    async def describe_nfs_acl_async(
        self,
        request: nas20170626_models.DescribeNfsAclRequest,
    ) -> nas20170626_models.DescribeNfsAclResponse:
        """
        @summary Queries whether the NFS ACL feature is enabled for a file system.
        
        @param request: DescribeNfsAclRequest
        @return: DescribeNfsAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_nfs_acl_with_options_async(request, runtime)

    def describe_protocol_mount_target_with_options(
        self,
        request: nas20170626_models.DescribeProtocolMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeProtocolMountTargetResponse:
        """
        @summary Queries the export directories of a protocol service.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: DescribeProtocolMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProtocolMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProtocolMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeProtocolMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_protocol_mount_target_with_options_async(
        self,
        request: nas20170626_models.DescribeProtocolMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeProtocolMountTargetResponse:
        """
        @summary Queries the export directories of a protocol service.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: DescribeProtocolMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProtocolMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProtocolMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeProtocolMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_protocol_mount_target(
        self,
        request: nas20170626_models.DescribeProtocolMountTargetRequest,
    ) -> nas20170626_models.DescribeProtocolMountTargetResponse:
        """
        @summary Queries the export directories of a protocol service.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: DescribeProtocolMountTargetRequest
        @return: DescribeProtocolMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_protocol_mount_target_with_options(request, runtime)

    async def describe_protocol_mount_target_async(
        self,
        request: nas20170626_models.DescribeProtocolMountTargetRequest,
    ) -> nas20170626_models.DescribeProtocolMountTargetResponse:
        """
        @summary Queries the export directories of a protocol service.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: DescribeProtocolMountTargetRequest
        @return: DescribeProtocolMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_protocol_mount_target_with_options_async(request, runtime)

    def describe_protocol_service_with_options(
        self,
        request: nas20170626_models.DescribeProtocolServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeProtocolServiceResponse:
        """
        @summary Queries the information about protocol services.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: DescribeProtocolServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProtocolServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.protocol_service_ids):
            query['ProtocolServiceIds'] = request.protocol_service_ids
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProtocolService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeProtocolServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_protocol_service_with_options_async(
        self,
        request: nas20170626_models.DescribeProtocolServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeProtocolServiceResponse:
        """
        @summary Queries the information about protocol services.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: DescribeProtocolServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProtocolServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.protocol_service_ids):
            query['ProtocolServiceIds'] = request.protocol_service_ids
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProtocolService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeProtocolServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_protocol_service(
        self,
        request: nas20170626_models.DescribeProtocolServiceRequest,
    ) -> nas20170626_models.DescribeProtocolServiceResponse:
        """
        @summary Queries the information about protocol services.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: DescribeProtocolServiceRequest
        @return: DescribeProtocolServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_protocol_service_with_options(request, runtime)

    async def describe_protocol_service_async(
        self,
        request: nas20170626_models.DescribeProtocolServiceRequest,
    ) -> nas20170626_models.DescribeProtocolServiceResponse:
        """
        @summary Queries the information about protocol services.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: DescribeProtocolServiceRequest
        @return: DescribeProtocolServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_protocol_service_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: nas20170626_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which File Storage NAS is available.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: nas20170626_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which File Storage NAS is available.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: nas20170626_models.DescribeRegionsRequest,
    ) -> nas20170626_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which File Storage NAS is available.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: nas20170626_models.DescribeRegionsRequest,
    ) -> nas20170626_models.DescribeRegionsResponse:
        """
        @summary Queries the regions in which File Storage NAS is available.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_smb_acl_with_options(
        self,
        request: nas20170626_models.DescribeSmbAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeSmbAclResponse:
        """
        @summary Queries the information about the access control list (ACL) feature of a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: DescribeSmbAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSmbAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmbAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeSmbAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_smb_acl_with_options_async(
        self,
        request: nas20170626_models.DescribeSmbAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeSmbAclResponse:
        """
        @summary Queries the information about the access control list (ACL) feature of a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: DescribeSmbAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSmbAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSmbAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeSmbAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_smb_acl(
        self,
        request: nas20170626_models.DescribeSmbAclRequest,
    ) -> nas20170626_models.DescribeSmbAclResponse:
        """
        @summary Queries the information about the access control list (ACL) feature of a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: DescribeSmbAclRequest
        @return: DescribeSmbAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_smb_acl_with_options(request, runtime)

    async def describe_smb_acl_async(
        self,
        request: nas20170626_models.DescribeSmbAclRequest,
    ) -> nas20170626_models.DescribeSmbAclResponse:
        """
        @summary Queries the information about the access control list (ACL) feature of a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: DescribeSmbAclRequest
        @return: DescribeSmbAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_smb_acl_with_options_async(request, runtime)

    def describe_snapshots_with_options(
        self,
        request: nas20170626_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeSnapshotsResponse:
        """
        @summary Queries the information about one or more snapshots of a file system.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: DescribeSnapshotsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSnapshotsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not UtilClient.is_unset(request.snapshot_type):
            query['SnapshotType'] = request.snapshot_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshots',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_snapshots_with_options_async(
        self,
        request: nas20170626_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeSnapshotsResponse:
        """
        @summary Queries the information about one or more snapshots of a file system.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: DescribeSnapshotsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSnapshotsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.snapshot_ids):
            query['SnapshotIds'] = request.snapshot_ids
        if not UtilClient.is_unset(request.snapshot_name):
            query['SnapshotName'] = request.snapshot_name
        if not UtilClient.is_unset(request.snapshot_type):
            query['SnapshotType'] = request.snapshot_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSnapshots',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_snapshots(
        self,
        request: nas20170626_models.DescribeSnapshotsRequest,
    ) -> nas20170626_models.DescribeSnapshotsResponse:
        """
        @summary Queries the information about one or more snapshots of a file system.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: DescribeSnapshotsRequest
        @return: DescribeSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    async def describe_snapshots_async(
        self,
        request: nas20170626_models.DescribeSnapshotsRequest,
    ) -> nas20170626_models.DescribeSnapshotsResponse:
        """
        @summary Queries the information about one or more snapshots of a file system.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: DescribeSnapshotsRequest
        @return: DescribeSnapshotsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_snapshots_with_options_async(request, runtime)

    def describe_storage_packages_with_options(
        self,
        request: nas20170626_models.DescribeStoragePackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeStoragePackagesResponse:
        """
        @summary You can call the DescribeStoragePackages operation to query the list of storage plans.
        
        @param request: DescribeStoragePackagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStoragePackagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.use_utcdate_time):
            query['UseUTCDateTime'] = request.use_utcdate_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStoragePackages',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeStoragePackagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_storage_packages_with_options_async(
        self,
        request: nas20170626_models.DescribeStoragePackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeStoragePackagesResponse:
        """
        @summary You can call the DescribeStoragePackages operation to query the list of storage plans.
        
        @param request: DescribeStoragePackagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeStoragePackagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.use_utcdate_time):
            query['UseUTCDateTime'] = request.use_utcdate_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStoragePackages',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeStoragePackagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_storage_packages(
        self,
        request: nas20170626_models.DescribeStoragePackagesRequest,
    ) -> nas20170626_models.DescribeStoragePackagesResponse:
        """
        @summary You can call the DescribeStoragePackages operation to query the list of storage plans.
        
        @param request: DescribeStoragePackagesRequest
        @return: DescribeStoragePackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_packages_with_options(request, runtime)

    async def describe_storage_packages_async(
        self,
        request: nas20170626_models.DescribeStoragePackagesRequest,
    ) -> nas20170626_models.DescribeStoragePackagesResponse:
        """
        @summary You can call the DescribeStoragePackages operation to query the list of storage plans.
        
        @param request: DescribeStoragePackagesRequest
        @return: DescribeStoragePackagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_packages_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: nas20170626_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeZonesResponse:
        """
        @summary Queries all zones in a region and the file system types that are supported in each zone.
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: nas20170626_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DescribeZonesResponse:
        """
        @summary Queries all zones in a region and the file system types that are supported in each zone.
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: nas20170626_models.DescribeZonesRequest,
    ) -> nas20170626_models.DescribeZonesResponse:
        """
        @summary Queries all zones in a region and the file system types that are supported in each zone.
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: nas20170626_models.DescribeZonesRequest,
    ) -> nas20170626_models.DescribeZonesResponse:
        """
        @summary Queries all zones in a region and the file system types that are supported in each zone.
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def disable_and_clean_recycle_bin_with_options(
        self,
        request: nas20170626_models.DisableAndCleanRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DisableAndCleanRecycleBinResponse:
        """
        @summary Disables and empties the recycle bin of a General-purpose NAS file system.
        
        @description    Only General-purpose NAS file systems support this operation.
        If you disable the recycle bin, all files in the recycle bin are permanently deleted.
        If you disable and then enable the recycle bin, the recycle bin is empty. You cannot retrieve the deleted files.
        
        @param request: DisableAndCleanRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAndCleanRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAndCleanRecycleBin',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DisableAndCleanRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_and_clean_recycle_bin_with_options_async(
        self,
        request: nas20170626_models.DisableAndCleanRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DisableAndCleanRecycleBinResponse:
        """
        @summary Disables and empties the recycle bin of a General-purpose NAS file system.
        
        @description    Only General-purpose NAS file systems support this operation.
        If you disable the recycle bin, all files in the recycle bin are permanently deleted.
        If you disable and then enable the recycle bin, the recycle bin is empty. You cannot retrieve the deleted files.
        
        @param request: DisableAndCleanRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAndCleanRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAndCleanRecycleBin',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DisableAndCleanRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_and_clean_recycle_bin(
        self,
        request: nas20170626_models.DisableAndCleanRecycleBinRequest,
    ) -> nas20170626_models.DisableAndCleanRecycleBinResponse:
        """
        @summary Disables and empties the recycle bin of a General-purpose NAS file system.
        
        @description    Only General-purpose NAS file systems support this operation.
        If you disable the recycle bin, all files in the recycle bin are permanently deleted.
        If you disable and then enable the recycle bin, the recycle bin is empty. You cannot retrieve the deleted files.
        
        @param request: DisableAndCleanRecycleBinRequest
        @return: DisableAndCleanRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_and_clean_recycle_bin_with_options(request, runtime)

    async def disable_and_clean_recycle_bin_async(
        self,
        request: nas20170626_models.DisableAndCleanRecycleBinRequest,
    ) -> nas20170626_models.DisableAndCleanRecycleBinResponse:
        """
        @summary Disables and empties the recycle bin of a General-purpose NAS file system.
        
        @description    Only General-purpose NAS file systems support this operation.
        If you disable the recycle bin, all files in the recycle bin are permanently deleted.
        If you disable and then enable the recycle bin, the recycle bin is empty. You cannot retrieve the deleted files.
        
        @param request: DisableAndCleanRecycleBinRequest
        @return: DisableAndCleanRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_and_clean_recycle_bin_with_options_async(request, runtime)

    def disable_nfs_acl_with_options(
        self,
        request: nas20170626_models.DisableNfsAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DisableNfsAclResponse:
        """
        @summary Disables the NFS ACL feature for a file system.
        
        @param request: DisableNfsAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableNfsAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableNfsAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DisableNfsAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_nfs_acl_with_options_async(
        self,
        request: nas20170626_models.DisableNfsAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DisableNfsAclResponse:
        """
        @summary Disables the NFS ACL feature for a file system.
        
        @param request: DisableNfsAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableNfsAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableNfsAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DisableNfsAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_nfs_acl(
        self,
        request: nas20170626_models.DisableNfsAclRequest,
    ) -> nas20170626_models.DisableNfsAclResponse:
        """
        @summary Disables the NFS ACL feature for a file system.
        
        @param request: DisableNfsAclRequest
        @return: DisableNfsAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_nfs_acl_with_options(request, runtime)

    async def disable_nfs_acl_async(
        self,
        request: nas20170626_models.DisableNfsAclRequest,
    ) -> nas20170626_models.DisableNfsAclResponse:
        """
        @summary Disables the NFS ACL feature for a file system.
        
        @param request: DisableNfsAclRequest
        @return: DisableNfsAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_nfs_acl_with_options_async(request, runtime)

    def disable_smb_acl_with_options(
        self,
        request: nas20170626_models.DisableSmbAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DisableSmbAclResponse:
        """
        @summary Disables the access control list (ACL) feature for a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: DisableSmbAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableSmbAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSmbAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DisableSmbAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_smb_acl_with_options_async(
        self,
        request: nas20170626_models.DisableSmbAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.DisableSmbAclResponse:
        """
        @summary Disables the access control list (ACL) feature for a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: DisableSmbAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableSmbAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSmbAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.DisableSmbAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_smb_acl(
        self,
        request: nas20170626_models.DisableSmbAclRequest,
    ) -> nas20170626_models.DisableSmbAclResponse:
        """
        @summary Disables the access control list (ACL) feature for a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: DisableSmbAclRequest
        @return: DisableSmbAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_smb_acl_with_options(request, runtime)

    async def disable_smb_acl_async(
        self,
        request: nas20170626_models.DisableSmbAclRequest,
    ) -> nas20170626_models.DisableSmbAclResponse:
        """
        @summary Disables the access control list (ACL) feature for a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: DisableSmbAclRequest
        @return: DisableSmbAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_smb_acl_with_options_async(request, runtime)

    def enable_nfs_acl_with_options(
        self,
        request: nas20170626_models.EnableNfsAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.EnableNfsAclResponse:
        """
        @summary Enables the NFS ACL feature for a file system.
        
        @param request: EnableNfsAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableNfsAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableNfsAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.EnableNfsAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_nfs_acl_with_options_async(
        self,
        request: nas20170626_models.EnableNfsAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.EnableNfsAclResponse:
        """
        @summary Enables the NFS ACL feature for a file system.
        
        @param request: EnableNfsAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableNfsAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableNfsAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.EnableNfsAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_nfs_acl(
        self,
        request: nas20170626_models.EnableNfsAclRequest,
    ) -> nas20170626_models.EnableNfsAclResponse:
        """
        @summary Enables the NFS ACL feature for a file system.
        
        @param request: EnableNfsAclRequest
        @return: EnableNfsAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_nfs_acl_with_options(request, runtime)

    async def enable_nfs_acl_async(
        self,
        request: nas20170626_models.EnableNfsAclRequest,
    ) -> nas20170626_models.EnableNfsAclResponse:
        """
        @summary Enables the NFS ACL feature for a file system.
        
        @param request: EnableNfsAclRequest
        @return: EnableNfsAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_nfs_acl_with_options_async(request, runtime)

    def enable_recycle_bin_with_options(
        self,
        request: nas20170626_models.EnableRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.EnableRecycleBinResponse:
        """
        @summary Enables the recycle bin feature for a file system.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: EnableRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.reserved_days):
            query['ReservedDays'] = request.reserved_days
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableRecycleBin',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.EnableRecycleBinResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_recycle_bin_with_options_async(
        self,
        request: nas20170626_models.EnableRecycleBinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.EnableRecycleBinResponse:
        """
        @summary Enables the recycle bin feature for a file system.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: EnableRecycleBinRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableRecycleBinResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.reserved_days):
            query['ReservedDays'] = request.reserved_days
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableRecycleBin',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.EnableRecycleBinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_recycle_bin(
        self,
        request: nas20170626_models.EnableRecycleBinRequest,
    ) -> nas20170626_models.EnableRecycleBinResponse:
        """
        @summary Enables the recycle bin feature for a file system.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: EnableRecycleBinRequest
        @return: EnableRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_recycle_bin_with_options(request, runtime)

    async def enable_recycle_bin_async(
        self,
        request: nas20170626_models.EnableRecycleBinRequest,
    ) -> nas20170626_models.EnableRecycleBinResponse:
        """
        @summary Enables the recycle bin feature for a file system.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: EnableRecycleBinRequest
        @return: EnableRecycleBinResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_recycle_bin_with_options_async(request, runtime)

    def enable_smb_acl_with_options(
        self,
        request: nas20170626_models.EnableSmbAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.EnableSmbAclResponse:
        """
        @summary Enables the access control list (ACL) feature for a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: EnableSmbAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableSmbAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.keytab):
            query['Keytab'] = request.keytab
        if not UtilClient.is_unset(request.keytab_md_5):
            query['KeytabMd5'] = request.keytab_md_5
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSmbAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.EnableSmbAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_smb_acl_with_options_async(
        self,
        request: nas20170626_models.EnableSmbAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.EnableSmbAclResponse:
        """
        @summary Enables the access control list (ACL) feature for a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: EnableSmbAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableSmbAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.keytab):
            query['Keytab'] = request.keytab
        if not UtilClient.is_unset(request.keytab_md_5):
            query['KeytabMd5'] = request.keytab_md_5
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSmbAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.EnableSmbAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_smb_acl(
        self,
        request: nas20170626_models.EnableSmbAclRequest,
    ) -> nas20170626_models.EnableSmbAclResponse:
        """
        @summary Enables the access control list (ACL) feature for a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: EnableSmbAclRequest
        @return: EnableSmbAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_smb_acl_with_options(request, runtime)

    async def enable_smb_acl_async(
        self,
        request: nas20170626_models.EnableSmbAclRequest,
    ) -> nas20170626_models.EnableSmbAclResponse:
        """
        @summary Enables the access control list (ACL) feature for a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: EnableSmbAclRequest
        @return: EnableSmbAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_smb_acl_with_options_async(request, runtime)

    def get_directory_or_file_properties_with_options(
        self,
        request: nas20170626_models.GetDirectoryOrFilePropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.GetDirectoryOrFilePropertiesResponse:
        """
        @summary Queries whether a directory contains files that are stored in the Infrequent Access (IA) or Archive storage class, or whether a file is stored in the IA or Archive storage class.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: GetDirectoryOrFilePropertiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDirectoryOrFilePropertiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDirectoryOrFileProperties',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.GetDirectoryOrFilePropertiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_directory_or_file_properties_with_options_async(
        self,
        request: nas20170626_models.GetDirectoryOrFilePropertiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.GetDirectoryOrFilePropertiesResponse:
        """
        @summary Queries whether a directory contains files that are stored in the Infrequent Access (IA) or Archive storage class, or whether a file is stored in the IA or Archive storage class.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: GetDirectoryOrFilePropertiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDirectoryOrFilePropertiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDirectoryOrFileProperties',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.GetDirectoryOrFilePropertiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_directory_or_file_properties(
        self,
        request: nas20170626_models.GetDirectoryOrFilePropertiesRequest,
    ) -> nas20170626_models.GetDirectoryOrFilePropertiesResponse:
        """
        @summary Queries whether a directory contains files that are stored in the Infrequent Access (IA) or Archive storage class, or whether a file is stored in the IA or Archive storage class.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: GetDirectoryOrFilePropertiesRequest
        @return: GetDirectoryOrFilePropertiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_directory_or_file_properties_with_options(request, runtime)

    async def get_directory_or_file_properties_async(
        self,
        request: nas20170626_models.GetDirectoryOrFilePropertiesRequest,
    ) -> nas20170626_models.GetDirectoryOrFilePropertiesResponse:
        """
        @summary Queries whether a directory contains files that are stored in the Infrequent Access (IA) or Archive storage class, or whether a file is stored in the IA or Archive storage class.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: GetDirectoryOrFilePropertiesRequest
        @return: GetDirectoryOrFilePropertiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_directory_or_file_properties_with_options_async(request, runtime)

    def get_recycle_bin_attribute_with_options(
        self,
        request: nas20170626_models.GetRecycleBinAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.GetRecycleBinAttributeResponse:
        """
        @summary Queries the recycle bin configurations of a General-purpose NAS file system.
        
        @description Only General-purpose File Storage NAS (NAS) file systems support this operation.
        
        @param request: GetRecycleBinAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRecycleBinAttributeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecycleBinAttribute',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.GetRecycleBinAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_recycle_bin_attribute_with_options_async(
        self,
        request: nas20170626_models.GetRecycleBinAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.GetRecycleBinAttributeResponse:
        """
        @summary Queries the recycle bin configurations of a General-purpose NAS file system.
        
        @description Only General-purpose File Storage NAS (NAS) file systems support this operation.
        
        @param request: GetRecycleBinAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRecycleBinAttributeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecycleBinAttribute',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.GetRecycleBinAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_recycle_bin_attribute(
        self,
        request: nas20170626_models.GetRecycleBinAttributeRequest,
    ) -> nas20170626_models.GetRecycleBinAttributeResponse:
        """
        @summary Queries the recycle bin configurations of a General-purpose NAS file system.
        
        @description Only General-purpose File Storage NAS (NAS) file systems support this operation.
        
        @param request: GetRecycleBinAttributeRequest
        @return: GetRecycleBinAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_recycle_bin_attribute_with_options(request, runtime)

    async def get_recycle_bin_attribute_async(
        self,
        request: nas20170626_models.GetRecycleBinAttributeRequest,
    ) -> nas20170626_models.GetRecycleBinAttributeResponse:
        """
        @summary Queries the recycle bin configurations of a General-purpose NAS file system.
        
        @description Only General-purpose File Storage NAS (NAS) file systems support this operation.
        
        @param request: GetRecycleBinAttributeRequest
        @return: GetRecycleBinAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_recycle_bin_attribute_with_options_async(request, runtime)

    def list_directories_and_files_with_options(
        self,
        request: nas20170626_models.ListDirectoriesAndFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListDirectoriesAndFilesResponse:
        """
        @summary Queries the infrequently-accessed files in a specified directory of a General-purpose NAS file system and the subdirectories that contain the files.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListDirectoriesAndFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDirectoriesAndFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_only):
            query['DirectoryOnly'] = request.directory_only
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDirectoriesAndFiles',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListDirectoriesAndFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_directories_and_files_with_options_async(
        self,
        request: nas20170626_models.ListDirectoriesAndFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListDirectoriesAndFilesResponse:
        """
        @summary Queries the infrequently-accessed files in a specified directory of a General-purpose NAS file system and the subdirectories that contain the files.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListDirectoriesAndFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDirectoriesAndFilesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_only):
            query['DirectoryOnly'] = request.directory_only
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDirectoriesAndFiles',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListDirectoriesAndFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_directories_and_files(
        self,
        request: nas20170626_models.ListDirectoriesAndFilesRequest,
    ) -> nas20170626_models.ListDirectoriesAndFilesResponse:
        """
        @summary Queries the infrequently-accessed files in a specified directory of a General-purpose NAS file system and the subdirectories that contain the files.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListDirectoriesAndFilesRequest
        @return: ListDirectoriesAndFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_directories_and_files_with_options(request, runtime)

    async def list_directories_and_files_async(
        self,
        request: nas20170626_models.ListDirectoriesAndFilesRequest,
    ) -> nas20170626_models.ListDirectoriesAndFilesResponse:
        """
        @summary Queries the infrequently-accessed files in a specified directory of a General-purpose NAS file system and the subdirectories that contain the files.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListDirectoriesAndFilesRequest
        @return: ListDirectoriesAndFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_directories_and_files_with_options_async(request, runtime)

    def list_lifecycle_retrieve_jobs_with_options(
        self,
        request: nas20170626_models.ListLifecycleRetrieveJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListLifecycleRetrieveJobsResponse:
        """
        @summary Queries data retrieval tasks.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListLifecycleRetrieveJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLifecycleRetrieveJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLifecycleRetrieveJobs',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListLifecycleRetrieveJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lifecycle_retrieve_jobs_with_options_async(
        self,
        request: nas20170626_models.ListLifecycleRetrieveJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListLifecycleRetrieveJobsResponse:
        """
        @summary Queries data retrieval tasks.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListLifecycleRetrieveJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLifecycleRetrieveJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLifecycleRetrieveJobs',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListLifecycleRetrieveJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_lifecycle_retrieve_jobs(
        self,
        request: nas20170626_models.ListLifecycleRetrieveJobsRequest,
    ) -> nas20170626_models.ListLifecycleRetrieveJobsResponse:
        """
        @summary Queries data retrieval tasks.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListLifecycleRetrieveJobsRequest
        @return: ListLifecycleRetrieveJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_lifecycle_retrieve_jobs_with_options(request, runtime)

    async def list_lifecycle_retrieve_jobs_async(
        self,
        request: nas20170626_models.ListLifecycleRetrieveJobsRequest,
    ) -> nas20170626_models.ListLifecycleRetrieveJobsResponse:
        """
        @summary Queries data retrieval tasks.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListLifecycleRetrieveJobsRequest
        @return: ListLifecycleRetrieveJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_lifecycle_retrieve_jobs_with_options_async(request, runtime)

    def list_recently_recycled_directories_with_options(
        self,
        request: nas20170626_models.ListRecentlyRecycledDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListRecentlyRecycledDirectoriesResponse:
        """
        @summary Queries the directories that are recently deleted.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListRecentlyRecycledDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecentlyRecycledDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecentlyRecycledDirectories',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecentlyRecycledDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recently_recycled_directories_with_options_async(
        self,
        request: nas20170626_models.ListRecentlyRecycledDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListRecentlyRecycledDirectoriesResponse:
        """
        @summary Queries the directories that are recently deleted.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListRecentlyRecycledDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecentlyRecycledDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecentlyRecycledDirectories',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecentlyRecycledDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recently_recycled_directories(
        self,
        request: nas20170626_models.ListRecentlyRecycledDirectoriesRequest,
    ) -> nas20170626_models.ListRecentlyRecycledDirectoriesResponse:
        """
        @summary Queries the directories that are recently deleted.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListRecentlyRecycledDirectoriesRequest
        @return: ListRecentlyRecycledDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_recently_recycled_directories_with_options(request, runtime)

    async def list_recently_recycled_directories_async(
        self,
        request: nas20170626_models.ListRecentlyRecycledDirectoriesRequest,
    ) -> nas20170626_models.ListRecentlyRecycledDirectoriesResponse:
        """
        @summary Queries the directories that are recently deleted.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListRecentlyRecycledDirectoriesRequest
        @return: ListRecentlyRecycledDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_recently_recycled_directories_with_options_async(request, runtime)

    def list_recycle_bin_jobs_with_options(
        self,
        request: nas20170626_models.ListRecycleBinJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListRecycleBinJobsResponse:
        """
        @summary Queries the jobs of the recycle bin.
        
        @description    Only General-purpose NAS file systems support this operation.
        You can query a maximum of 50 jobs that are recently executed.
        
        @param request: ListRecycleBinJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecycleBinJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecycleBinJobs',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecycleBinJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recycle_bin_jobs_with_options_async(
        self,
        request: nas20170626_models.ListRecycleBinJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListRecycleBinJobsResponse:
        """
        @summary Queries the jobs of the recycle bin.
        
        @description    Only General-purpose NAS file systems support this operation.
        You can query a maximum of 50 jobs that are recently executed.
        
        @param request: ListRecycleBinJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecycleBinJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecycleBinJobs',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecycleBinJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recycle_bin_jobs(
        self,
        request: nas20170626_models.ListRecycleBinJobsRequest,
    ) -> nas20170626_models.ListRecycleBinJobsResponse:
        """
        @summary Queries the jobs of the recycle bin.
        
        @description    Only General-purpose NAS file systems support this operation.
        You can query a maximum of 50 jobs that are recently executed.
        
        @param request: ListRecycleBinJobsRequest
        @return: ListRecycleBinJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_recycle_bin_jobs_with_options(request, runtime)

    async def list_recycle_bin_jobs_async(
        self,
        request: nas20170626_models.ListRecycleBinJobsRequest,
    ) -> nas20170626_models.ListRecycleBinJobsResponse:
        """
        @summary Queries the jobs of the recycle bin.
        
        @description    Only General-purpose NAS file systems support this operation.
        You can query a maximum of 50 jobs that are recently executed.
        
        @param request: ListRecycleBinJobsRequest
        @return: ListRecycleBinJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_recycle_bin_jobs_with_options_async(request, runtime)

    def list_recycled_directories_and_files_with_options(
        self,
        request: nas20170626_models.ListRecycledDirectoriesAndFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListRecycledDirectoriesAndFilesResponse:
        """
        @summary Queries deleted files or directories.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListRecycledDirectoriesAndFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecycledDirectoriesAndFilesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecycledDirectoriesAndFiles',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecycledDirectoriesAndFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_recycled_directories_and_files_with_options_async(
        self,
        request: nas20170626_models.ListRecycledDirectoriesAndFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListRecycledDirectoriesAndFilesResponse:
        """
        @summary Queries deleted files or directories.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListRecycledDirectoriesAndFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecycledDirectoriesAndFilesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecycledDirectoriesAndFiles',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListRecycledDirectoriesAndFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_recycled_directories_and_files(
        self,
        request: nas20170626_models.ListRecycledDirectoriesAndFilesRequest,
    ) -> nas20170626_models.ListRecycledDirectoriesAndFilesResponse:
        """
        @summary Queries deleted files or directories.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListRecycledDirectoriesAndFilesRequest
        @return: ListRecycledDirectoriesAndFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_recycled_directories_and_files_with_options(request, runtime)

    async def list_recycled_directories_and_files_async(
        self,
        request: nas20170626_models.ListRecycledDirectoriesAndFilesRequest,
    ) -> nas20170626_models.ListRecycledDirectoriesAndFilesResponse:
        """
        @summary Queries deleted files or directories.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ListRecycledDirectoriesAndFilesRequest
        @return: ListRecycledDirectoriesAndFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_recycled_directories_and_files_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: nas20170626_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListTagResourcesResponse:
        """
        @summary Queries tags.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: nas20170626_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ListTagResourcesResponse:
        """
        @summary Queries tags.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: nas20170626_models.ListTagResourcesRequest,
    ) -> nas20170626_models.ListTagResourcesResponse:
        """
        @summary Queries tags.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: nas20170626_models.ListTagResourcesRequest,
    ) -> nas20170626_models.ListTagResourcesResponse:
        """
        @summary Queries tags.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_access_group_with_options(
        self,
        request: nas20170626_models.ModifyAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAccessGroupResponse:
        """
        @summary Modifies a permission group.
        
        @description The default permission group (DEFAULT_VPC_GROUP_NAME) cannot be modified.
        
        @param request: ModifyAccessGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccessGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_access_group_with_options_async(
        self,
        request: nas20170626_models.ModifyAccessGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAccessGroupResponse:
        """
        @summary Modifies a permission group.
        
        @description The default permission group (DEFAULT_VPC_GROUP_NAME) cannot be modified.
        
        @param request: ModifyAccessGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccessGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccessGroup',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_access_group(
        self,
        request: nas20170626_models.ModifyAccessGroupRequest,
    ) -> nas20170626_models.ModifyAccessGroupResponse:
        """
        @summary Modifies a permission group.
        
        @description The default permission group (DEFAULT_VPC_GROUP_NAME) cannot be modified.
        
        @param request: ModifyAccessGroupRequest
        @return: ModifyAccessGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_access_group_with_options(request, runtime)

    async def modify_access_group_async(
        self,
        request: nas20170626_models.ModifyAccessGroupRequest,
    ) -> nas20170626_models.ModifyAccessGroupResponse:
        """
        @summary Modifies a permission group.
        
        @description The default permission group (DEFAULT_VPC_GROUP_NAME) cannot be modified.
        
        @param request: ModifyAccessGroupRequest
        @return: ModifyAccessGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_access_group_with_options_async(request, runtime)

    def modify_access_point_with_options(
        self,
        request: nas20170626_models.ModifyAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAccessPointResponse:
        """
        @summary Modifies the information about an access point.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: ModifyAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group):
            query['AccessGroup'] = request.access_group
        if not UtilClient.is_unset(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not UtilClient.is_unset(request.access_point_name):
            query['AccessPointName'] = request.access_point_name
        if not UtilClient.is_unset(request.enabled_ram):
            query['EnabledRam'] = request.enabled_ram
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccessPoint',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessPointResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_access_point_with_options_async(
        self,
        request: nas20170626_models.ModifyAccessPointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAccessPointResponse:
        """
        @summary Modifies the information about an access point.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: ModifyAccessPointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccessPointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group):
            query['AccessGroup'] = request.access_group
        if not UtilClient.is_unset(request.access_point_id):
            query['AccessPointId'] = request.access_point_id
        if not UtilClient.is_unset(request.access_point_name):
            query['AccessPointName'] = request.access_point_name
        if not UtilClient.is_unset(request.enabled_ram):
            query['EnabledRam'] = request.enabled_ram
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccessPoint',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessPointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_access_point(
        self,
        request: nas20170626_models.ModifyAccessPointRequest,
    ) -> nas20170626_models.ModifyAccessPointResponse:
        """
        @summary Modifies the information about an access point.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: ModifyAccessPointRequest
        @return: ModifyAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_access_point_with_options(request, runtime)

    async def modify_access_point_async(
        self,
        request: nas20170626_models.ModifyAccessPointRequest,
    ) -> nas20170626_models.ModifyAccessPointResponse:
        """
        @summary Modifies the information about an access point.
        
        @description Only General-purpose Network File System (NFS) file systems support this operation.
        
        @param request: ModifyAccessPointRequest
        @return: ModifyAccessPointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_access_point_with_options_async(request, runtime)

    def modify_access_rule_with_options(
        self,
        request: nas20170626_models.ModifyAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAccessRuleResponse:
        """
        @summary Modifies a rule in a permission group.
        
        @description The rules in the default permission group (DEFAULT_VPC_GROUP_NAME) cannot be modified.
        
        @param request: ModifyAccessRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccessRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.user_access_type):
            query['UserAccessType'] = request.user_access_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_access_rule_with_options_async(
        self,
        request: nas20170626_models.ModifyAccessRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAccessRuleResponse:
        """
        @summary Modifies a rule in a permission group.
        
        @description The rules in the default permission group (DEFAULT_VPC_GROUP_NAME) cannot be modified.
        
        @param request: ModifyAccessRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccessRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.access_rule_id):
            query['AccessRuleId'] = request.access_rule_id
        if not UtilClient.is_unset(request.file_system_type):
            query['FileSystemType'] = request.file_system_type
        if not UtilClient.is_unset(request.ipv_6source_cidr_ip):
            query['Ipv6SourceCidrIp'] = request.ipv_6source_cidr_ip
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.rwaccess_type):
            query['RWAccessType'] = request.rwaccess_type
        if not UtilClient.is_unset(request.source_cidr_ip):
            query['SourceCidrIp'] = request.source_cidr_ip
        if not UtilClient.is_unset(request.user_access_type):
            query['UserAccessType'] = request.user_access_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccessRule',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAccessRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_access_rule(
        self,
        request: nas20170626_models.ModifyAccessRuleRequest,
    ) -> nas20170626_models.ModifyAccessRuleResponse:
        """
        @summary Modifies a rule in a permission group.
        
        @description The rules in the default permission group (DEFAULT_VPC_GROUP_NAME) cannot be modified.
        
        @param request: ModifyAccessRuleRequest
        @return: ModifyAccessRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_access_rule_with_options(request, runtime)

    async def modify_access_rule_async(
        self,
        request: nas20170626_models.ModifyAccessRuleRequest,
    ) -> nas20170626_models.ModifyAccessRuleResponse:
        """
        @summary Modifies a rule in a permission group.
        
        @description The rules in the default permission group (DEFAULT_VPC_GROUP_NAME) cannot be modified.
        
        @param request: ModifyAccessRuleRequest
        @return: ModifyAccessRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_access_rule_with_options_async(request, runtime)

    def modify_auto_snapshot_policy_with_options(
        self,
        request: nas20170626_models.ModifyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAutoSnapshotPolicyResponse:
        """
        @summary An automatic snapshot policy is modified. After you modify an automatic snapshot policy that is applied to a file system, the modification immediately applies to subsequent snapshots that are created for the file system.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: ModifyAutoSnapshotPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.auto_snapshot_policy_name):
            query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        if not UtilClient.is_unset(request.repeat_weekdays):
            query['RepeatWeekdays'] = request.repeat_weekdays
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.time_points):
            query['TimePoints'] = request.time_points
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAutoSnapshotPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_auto_snapshot_policy_with_options_async(
        self,
        request: nas20170626_models.ModifyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyAutoSnapshotPolicyResponse:
        """
        @summary An automatic snapshot policy is modified. After you modify an automatic snapshot policy that is applied to a file system, the modification immediately applies to subsequent snapshots that are created for the file system.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: ModifyAutoSnapshotPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAutoSnapshotPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_snapshot_policy_id):
            query['AutoSnapshotPolicyId'] = request.auto_snapshot_policy_id
        if not UtilClient.is_unset(request.auto_snapshot_policy_name):
            query['AutoSnapshotPolicyName'] = request.auto_snapshot_policy_name
        if not UtilClient.is_unset(request.repeat_weekdays):
            query['RepeatWeekdays'] = request.repeat_weekdays
        if not UtilClient.is_unset(request.retention_days):
            query['RetentionDays'] = request.retention_days
        if not UtilClient.is_unset(request.time_points):
            query['TimePoints'] = request.time_points
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAutoSnapshotPolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyAutoSnapshotPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_auto_snapshot_policy(
        self,
        request: nas20170626_models.ModifyAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.ModifyAutoSnapshotPolicyResponse:
        """
        @summary An automatic snapshot policy is modified. After you modify an automatic snapshot policy that is applied to a file system, the modification immediately applies to subsequent snapshots that are created for the file system.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: ModifyAutoSnapshotPolicyRequest
        @return: ModifyAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_snapshot_policy_with_options(request, runtime)

    async def modify_auto_snapshot_policy_async(
        self,
        request: nas20170626_models.ModifyAutoSnapshotPolicyRequest,
    ) -> nas20170626_models.ModifyAutoSnapshotPolicyResponse:
        """
        @summary An automatic snapshot policy is modified. After you modify an automatic snapshot policy that is applied to a file system, the modification immediately applies to subsequent snapshots that are created for the file system.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        
        @param request: ModifyAutoSnapshotPolicyRequest
        @return: ModifyAutoSnapshotPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_snapshot_policy_with_options_async(request, runtime)

    def modify_data_flow_with_options(
        self,
        request: nas20170626_models.ModifyDataFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyDataFlowResponse:
        """
        @summary Modifies the attributes of a dataflow.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flows.
        You can modify the attributes only of the data flows that are in the `Running` state.
        It generally takes 2 to 5 minutes to modify the attributes of a data flow. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the status of the data flow to be modified.
        
        @param request: ModifyDataFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.throughput):
            query['Throughput'] = request.throughput
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_flow_with_options_async(
        self,
        request: nas20170626_models.ModifyDataFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyDataFlowResponse:
        """
        @summary Modifies the attributes of a dataflow.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flows.
        You can modify the attributes only of the data flows that are in the `Running` state.
        It generally takes 2 to 5 minutes to modify the attributes of a data flow. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the status of the data flow to be modified.
        
        @param request: ModifyDataFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.throughput):
            query['Throughput'] = request.throughput
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyDataFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_flow(
        self,
        request: nas20170626_models.ModifyDataFlowRequest,
    ) -> nas20170626_models.ModifyDataFlowResponse:
        """
        @summary Modifies the attributes of a dataflow.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flows.
        You can modify the attributes only of the data flows that are in the `Running` state.
        It generally takes 2 to 5 minutes to modify the attributes of a data flow. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the status of the data flow to be modified.
        
        @param request: ModifyDataFlowRequest
        @return: ModifyDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_data_flow_with_options(request, runtime)

    async def modify_data_flow_async(
        self,
        request: nas20170626_models.ModifyDataFlowRequest,
    ) -> nas20170626_models.ModifyDataFlowResponse:
        """
        @summary Modifies the attributes of a dataflow.
        
        @description    Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.4.0 and later support data flows.
        You can modify the attributes only of the data flows that are in the `Running` state.
        It generally takes 2 to 5 minutes to modify the attributes of a data flow. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the status of the data flow to be modified.
        
        @param request: ModifyDataFlowRequest
        @return: ModifyDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_data_flow_with_options_async(request, runtime)

    def modify_data_flow_auto_refresh_with_options(
        self,
        request: nas20170626_models.ModifyDataFlowAutoRefreshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyDataFlowAutoRefreshResponse:
        """
        @summary Modifies an AutoRefresh configuration of a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can modify the AutoRefresh configurations only for the dataflows that are in the `Running` or `Stopped` state.
        It generally takes 2 to 5 minutes to modify an AutoRefresh configuration. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the task of modifying an AutoRefresh configuration.
        
        @param request: ModifyDataFlowAutoRefreshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDataFlowAutoRefreshResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not UtilClient.is_unset(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDataFlowAutoRefresh',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyDataFlowAutoRefreshResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_data_flow_auto_refresh_with_options_async(
        self,
        request: nas20170626_models.ModifyDataFlowAutoRefreshRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyDataFlowAutoRefreshResponse:
        """
        @summary Modifies an AutoRefresh configuration of a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can modify the AutoRefresh configurations only for the dataflows that are in the `Running` or `Stopped` state.
        It generally takes 2 to 5 minutes to modify an AutoRefresh configuration. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the task of modifying an AutoRefresh configuration.
        
        @param request: ModifyDataFlowAutoRefreshRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDataFlowAutoRefreshResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_refresh_interval):
            query['AutoRefreshInterval'] = request.auto_refresh_interval
        if not UtilClient.is_unset(request.auto_refresh_policy):
            query['AutoRefreshPolicy'] = request.auto_refresh_policy
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDataFlowAutoRefresh',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyDataFlowAutoRefreshResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_data_flow_auto_refresh(
        self,
        request: nas20170626_models.ModifyDataFlowAutoRefreshRequest,
    ) -> nas20170626_models.ModifyDataFlowAutoRefreshResponse:
        """
        @summary Modifies an AutoRefresh configuration of a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can modify the AutoRefresh configurations only for the dataflows that are in the `Running` or `Stopped` state.
        It generally takes 2 to 5 minutes to modify an AutoRefresh configuration. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the task of modifying an AutoRefresh configuration.
        
        @param request: ModifyDataFlowAutoRefreshRequest
        @return: ModifyDataFlowAutoRefreshResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_data_flow_auto_refresh_with_options(request, runtime)

    async def modify_data_flow_auto_refresh_async(
        self,
        request: nas20170626_models.ModifyDataFlowAutoRefreshRequest,
    ) -> nas20170626_models.ModifyDataFlowAutoRefreshResponse:
        """
        @summary Modifies an AutoRefresh configuration of a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can modify the AutoRefresh configurations only for the dataflows that are in the `Running` or `Stopped` state.
        It generally takes 2 to 5 minutes to modify an AutoRefresh configuration. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2838084.html) operation to query the task of modifying an AutoRefresh configuration.
        
        @param request: ModifyDataFlowAutoRefreshRequest
        @return: ModifyDataFlowAutoRefreshResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_data_flow_auto_refresh_with_options_async(request, runtime)

    def modify_file_system_with_options(
        self,
        tmp_req: nas20170626_models.ModifyFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyFileSystemResponse:
        """
        @summary Modifies the description of a file system.
        
        @param tmp_req: ModifyFileSystemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFileSystemResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nas20170626_models.ModifyFileSystemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.options):
            request.options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.options, 'Options', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.options_shrink):
            query['Options'] = request.options_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_file_system_with_options_async(
        self,
        tmp_req: nas20170626_models.ModifyFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyFileSystemResponse:
        """
        @summary Modifies the description of a file system.
        
        @param tmp_req: ModifyFileSystemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFileSystemResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nas20170626_models.ModifyFileSystemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.options):
            request.options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.options, 'Options', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.options_shrink):
            query['Options'] = request.options_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_file_system(
        self,
        request: nas20170626_models.ModifyFileSystemRequest,
    ) -> nas20170626_models.ModifyFileSystemResponse:
        """
        @summary Modifies the description of a file system.
        
        @param request: ModifyFileSystemRequest
        @return: ModifyFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_file_system_with_options(request, runtime)

    async def modify_file_system_async(
        self,
        request: nas20170626_models.ModifyFileSystemRequest,
    ) -> nas20170626_models.ModifyFileSystemResponse:
        """
        @summary Modifies the description of a file system.
        
        @param request: ModifyFileSystemRequest
        @return: ModifyFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_file_system_with_options_async(request, runtime)

    def modify_fileset_with_options(
        self,
        request: nas20170626_models.ModifyFilesetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyFilesetResponse:
        """
        @summary Modifies a fileset.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation.
        
        @param request: ModifyFilesetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFilesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFileset',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyFilesetResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_fileset_with_options_async(
        self,
        request: nas20170626_models.ModifyFilesetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyFilesetResponse:
        """
        @summary Modifies a fileset.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation.
        
        @param request: ModifyFilesetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFilesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFileset',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyFilesetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_fileset(
        self,
        request: nas20170626_models.ModifyFilesetRequest,
    ) -> nas20170626_models.ModifyFilesetResponse:
        """
        @summary Modifies a fileset.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation.
        
        @param request: ModifyFilesetRequest
        @return: ModifyFilesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_fileset_with_options(request, runtime)

    async def modify_fileset_async(
        self,
        request: nas20170626_models.ModifyFilesetRequest,
    ) -> nas20170626_models.ModifyFilesetResponse:
        """
        @summary Modifies a fileset.
        
        @description Only Cloud Parallel File Storage (CPFS) for LINGJUN V2.7.0 and later support this operation.
        
        @param request: ModifyFilesetRequest
        @return: ModifyFilesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_fileset_with_options_async(request, runtime)

    def modify_ldapconfig_with_options(
        self,
        request: nas20170626_models.ModifyLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyLDAPConfigResponse:
        """
        @deprecated OpenAPI ModifyLDAPConfig is deprecated
        
        @summary Used to modify LDAP configuration.
        
        @description The API operation is available only for Cloud Parallel File Storage (CPFS) file systems.
        
        @param request: ModifyLDAPConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLDAPConfigResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_dn):
            query['BindDN'] = request.bind_dn
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.search_base):
            query['SearchBase'] = request.search_base
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyLDAPConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_ldapconfig_with_options_async(
        self,
        request: nas20170626_models.ModifyLDAPConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyLDAPConfigResponse:
        """
        @deprecated OpenAPI ModifyLDAPConfig is deprecated
        
        @summary Used to modify LDAP configuration.
        
        @description The API operation is available only for Cloud Parallel File Storage (CPFS) file systems.
        
        @param request: ModifyLDAPConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLDAPConfigResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bind_dn):
            query['BindDN'] = request.bind_dn
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.search_base):
            query['SearchBase'] = request.search_base
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLDAPConfig',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyLDAPConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_ldapconfig(
        self,
        request: nas20170626_models.ModifyLDAPConfigRequest,
    ) -> nas20170626_models.ModifyLDAPConfigResponse:
        """
        @deprecated OpenAPI ModifyLDAPConfig is deprecated
        
        @summary Used to modify LDAP configuration.
        
        @description The API operation is available only for Cloud Parallel File Storage (CPFS) file systems.
        
        @param request: ModifyLDAPConfigRequest
        @return: ModifyLDAPConfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_ldapconfig_with_options(request, runtime)

    async def modify_ldapconfig_async(
        self,
        request: nas20170626_models.ModifyLDAPConfigRequest,
    ) -> nas20170626_models.ModifyLDAPConfigResponse:
        """
        @deprecated OpenAPI ModifyLDAPConfig is deprecated
        
        @summary Used to modify LDAP configuration.
        
        @description The API operation is available only for Cloud Parallel File Storage (CPFS) file systems.
        
        @param request: ModifyLDAPConfigRequest
        @return: ModifyLDAPConfigResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_ldapconfig_with_options_async(request, runtime)

    def modify_lifecycle_policy_with_options(
        self,
        request: nas20170626_models.ModifyLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyLifecyclePolicyResponse:
        """
        @summary Modifies a lifecycle policy.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ModifyLifecyclePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLifecyclePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        if not UtilClient.is_unset(request.lifecycle_rule_name):
            query['LifecycleRuleName'] = request.lifecycle_rule_name
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyLifecyclePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_lifecycle_policy_with_options_async(
        self,
        request: nas20170626_models.ModifyLifecyclePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyLifecyclePolicyResponse:
        """
        @summary Modifies a lifecycle policy.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ModifyLifecyclePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLifecyclePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.lifecycle_policy_name):
            query['LifecyclePolicyName'] = request.lifecycle_policy_name
        if not UtilClient.is_unset(request.lifecycle_rule_name):
            query['LifecycleRuleName'] = request.lifecycle_rule_name
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLifecyclePolicy',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyLifecyclePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_lifecycle_policy(
        self,
        request: nas20170626_models.ModifyLifecyclePolicyRequest,
    ) -> nas20170626_models.ModifyLifecyclePolicyResponse:
        """
        @summary Modifies a lifecycle policy.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ModifyLifecyclePolicyRequest
        @return: ModifyLifecyclePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_lifecycle_policy_with_options(request, runtime)

    async def modify_lifecycle_policy_async(
        self,
        request: nas20170626_models.ModifyLifecyclePolicyRequest,
    ) -> nas20170626_models.ModifyLifecyclePolicyResponse:
        """
        @summary Modifies a lifecycle policy.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: ModifyLifecyclePolicyRequest
        @return: ModifyLifecyclePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_lifecycle_policy_with_options_async(request, runtime)

    def modify_mount_target_with_options(
        self,
        request: nas20170626_models.ModifyMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyMountTargetResponse:
        """
        @summary Modifies a mount target.
        
        @param request: ModifyMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.dual_stack_mount_target_domain):
            query['DualStackMountTargetDomain'] = request.dual_stack_mount_target_domain
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_mount_target_with_options_async(
        self,
        request: nas20170626_models.ModifyMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyMountTargetResponse:
        """
        @summary Modifies a mount target.
        
        @param request: ModifyMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_group_name):
            query['AccessGroupName'] = request.access_group_name
        if not UtilClient.is_unset(request.dual_stack_mount_target_domain):
            query['DualStackMountTargetDomain'] = request.dual_stack_mount_target_domain
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.mount_target_domain):
            query['MountTargetDomain'] = request.mount_target_domain
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_mount_target(
        self,
        request: nas20170626_models.ModifyMountTargetRequest,
    ) -> nas20170626_models.ModifyMountTargetResponse:
        """
        @summary Modifies a mount target.
        
        @param request: ModifyMountTargetRequest
        @return: ModifyMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_mount_target_with_options(request, runtime)

    async def modify_mount_target_async(
        self,
        request: nas20170626_models.ModifyMountTargetRequest,
    ) -> nas20170626_models.ModifyMountTargetResponse:
        """
        @summary Modifies a mount target.
        
        @param request: ModifyMountTargetRequest
        @return: ModifyMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_mount_target_with_options_async(request, runtime)

    def modify_protocol_mount_target_with_options(
        self,
        request: nas20170626_models.ModifyProtocolMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyProtocolMountTargetResponse:
        """
        @summary Modifies the export directory parameters of a protocol service. Only the description can be modified. The virtual private cloud (VPC) ID and vSwitch ID cannot be changed. To change these IDs, you must delete the export directory and create a new one.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: ModifyProtocolMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProtocolMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtocolMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyProtocolMountTargetResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_protocol_mount_target_with_options_async(
        self,
        request: nas20170626_models.ModifyProtocolMountTargetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyProtocolMountTargetResponse:
        """
        @summary Modifies the export directory parameters of a protocol service. Only the description can be modified. The virtual private cloud (VPC) ID and vSwitch ID cannot be changed. To change these IDs, you must delete the export directory and create a new one.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: ModifyProtocolMountTargetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProtocolMountTargetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.export_id):
            query['ExportId'] = request.export_id
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtocolMountTarget',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyProtocolMountTargetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_protocol_mount_target(
        self,
        request: nas20170626_models.ModifyProtocolMountTargetRequest,
    ) -> nas20170626_models.ModifyProtocolMountTargetResponse:
        """
        @summary Modifies the export directory parameters of a protocol service. Only the description can be modified. The virtual private cloud (VPC) ID and vSwitch ID cannot be changed. To change these IDs, you must delete the export directory and create a new one.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: ModifyProtocolMountTargetRequest
        @return: ModifyProtocolMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_protocol_mount_target_with_options(request, runtime)

    async def modify_protocol_mount_target_async(
        self,
        request: nas20170626_models.ModifyProtocolMountTargetRequest,
    ) -> nas20170626_models.ModifyProtocolMountTargetResponse:
        """
        @summary Modifies the export directory parameters of a protocol service. Only the description can be modified. The virtual private cloud (VPC) ID and vSwitch ID cannot be changed. To change these IDs, you must delete the export directory and create a new one.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: ModifyProtocolMountTargetRequest
        @return: ModifyProtocolMountTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_protocol_mount_target_with_options_async(request, runtime)

    def modify_protocol_service_with_options(
        self,
        request: nas20170626_models.ModifyProtocolServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyProtocolServiceResponse:
        """
        @summary Modifies a protocol service. You can modify the description of a protocol service.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: ModifyProtocolServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProtocolServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtocolService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyProtocolServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_protocol_service_with_options_async(
        self,
        request: nas20170626_models.ModifyProtocolServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifyProtocolServiceResponse:
        """
        @summary Modifies a protocol service. You can modify the description of a protocol service.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: ModifyProtocolServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProtocolServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.protocol_service_id):
            query['ProtocolServiceId'] = request.protocol_service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtocolService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifyProtocolServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_protocol_service(
        self,
        request: nas20170626_models.ModifyProtocolServiceRequest,
    ) -> nas20170626_models.ModifyProtocolServiceResponse:
        """
        @summary Modifies a protocol service. You can modify the description of a protocol service.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: ModifyProtocolServiceRequest
        @return: ModifyProtocolServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_protocol_service_with_options(request, runtime)

    async def modify_protocol_service_async(
        self,
        request: nas20170626_models.ModifyProtocolServiceRequest,
    ) -> nas20170626_models.ModifyProtocolServiceResponse:
        """
        @summary Modifies a protocol service. You can modify the description of a protocol service.
        
        @description This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        
        @param request: ModifyProtocolServiceRequest
        @return: ModifyProtocolServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_protocol_service_with_options_async(request, runtime)

    def modify_smb_acl_with_options(
        self,
        request: nas20170626_models.ModifySmbAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifySmbAclResponse:
        """
        @summary Updates the information about the access control list (ACL) feature of a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: ModifySmbAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySmbAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_anonymous_access):
            query['EnableAnonymousAccess'] = request.enable_anonymous_access
        if not UtilClient.is_unset(request.encrypt_data):
            query['EncryptData'] = request.encrypt_data
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.home_dir_path):
            query['HomeDirPath'] = request.home_dir_path
        if not UtilClient.is_unset(request.keytab):
            query['Keytab'] = request.keytab
        if not UtilClient.is_unset(request.keytab_md_5):
            query['KeytabMd5'] = request.keytab_md_5
        if not UtilClient.is_unset(request.reject_unencrypted_access):
            query['RejectUnencryptedAccess'] = request.reject_unencrypted_access
        if not UtilClient.is_unset(request.super_admin_sid):
            query['SuperAdminSid'] = request.super_admin_sid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySmbAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifySmbAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_smb_acl_with_options_async(
        self,
        request: nas20170626_models.ModifySmbAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ModifySmbAclResponse:
        """
        @summary Updates the information about the access control list (ACL) feature of a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: ModifySmbAclRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySmbAclResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_anonymous_access):
            query['EnableAnonymousAccess'] = request.enable_anonymous_access
        if not UtilClient.is_unset(request.encrypt_data):
            query['EncryptData'] = request.encrypt_data
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.home_dir_path):
            query['HomeDirPath'] = request.home_dir_path
        if not UtilClient.is_unset(request.keytab):
            query['Keytab'] = request.keytab
        if not UtilClient.is_unset(request.keytab_md_5):
            query['KeytabMd5'] = request.keytab_md_5
        if not UtilClient.is_unset(request.reject_unencrypted_access):
            query['RejectUnencryptedAccess'] = request.reject_unencrypted_access
        if not UtilClient.is_unset(request.super_admin_sid):
            query['SuperAdminSid'] = request.super_admin_sid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySmbAcl',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ModifySmbAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_smb_acl(
        self,
        request: nas20170626_models.ModifySmbAclRequest,
    ) -> nas20170626_models.ModifySmbAclResponse:
        """
        @summary Updates the information about the access control list (ACL) feature of a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: ModifySmbAclRequest
        @return: ModifySmbAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_smb_acl_with_options(request, runtime)

    async def modify_smb_acl_async(
        self,
        request: nas20170626_models.ModifySmbAclRequest,
    ) -> nas20170626_models.ModifySmbAclResponse:
        """
        @summary Updates the information about the access control list (ACL) feature of a Server Message Block (SMB) file system that resides in an Active Directory (AD) domain.
        
        @param request: ModifySmbAclRequest
        @return: ModifySmbAclResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_smb_acl_with_options_async(request, runtime)

    def open_nasservice_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.OpenNASServiceResponse:
        """
        @summary Activates File Storage NAS.
        
        @param request: OpenNASServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenNASServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenNASService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.OpenNASServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_nasservice_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.OpenNASServiceResponse:
        """
        @summary Activates File Storage NAS.
        
        @param request: OpenNASServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenNASServiceResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenNASService',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.OpenNASServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_nasservice(self) -> nas20170626_models.OpenNASServiceResponse:
        """
        @summary Activates File Storage NAS.
        
        @return: OpenNASServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_nasservice_with_options(runtime)

    async def open_nasservice_async(self) -> nas20170626_models.OpenNASServiceResponse:
        """
        @summary Activates File Storage NAS.
        
        @return: OpenNASServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.open_nasservice_with_options_async(runtime)

    def remove_client_from_black_list_with_options(
        self,
        request: nas20170626_models.RemoveClientFromBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.RemoveClientFromBlackListResponse:
        """
        @deprecated OpenAPI RemoveClientFromBlackList is deprecated
        
        @summary Remove the client from the blacklist.
        
        @description The API operation is available only for CPFS file systems.
        
        @param request: RemoveClientFromBlackListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveClientFromBlackListResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveClientFromBlackList',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.RemoveClientFromBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_client_from_black_list_with_options_async(
        self,
        request: nas20170626_models.RemoveClientFromBlackListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.RemoveClientFromBlackListResponse:
        """
        @deprecated OpenAPI RemoveClientFromBlackList is deprecated
        
        @summary Remove the client from the blacklist.
        
        @description The API operation is available only for CPFS file systems.
        
        @param request: RemoveClientFromBlackListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveClientFromBlackListResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIP'] = request.client_ip
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveClientFromBlackList',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.RemoveClientFromBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_client_from_black_list(
        self,
        request: nas20170626_models.RemoveClientFromBlackListRequest,
    ) -> nas20170626_models.RemoveClientFromBlackListResponse:
        """
        @deprecated OpenAPI RemoveClientFromBlackList is deprecated
        
        @summary Remove the client from the blacklist.
        
        @description The API operation is available only for CPFS file systems.
        
        @param request: RemoveClientFromBlackListRequest
        @return: RemoveClientFromBlackListResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_client_from_black_list_with_options(request, runtime)

    async def remove_client_from_black_list_async(
        self,
        request: nas20170626_models.RemoveClientFromBlackListRequest,
    ) -> nas20170626_models.RemoveClientFromBlackListResponse:
        """
        @deprecated OpenAPI RemoveClientFromBlackList is deprecated
        
        @summary Remove the client from the blacklist.
        
        @description The API operation is available only for CPFS file systems.
        
        @param request: RemoveClientFromBlackListRequest
        @return: RemoveClientFromBlackListResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_client_from_black_list_with_options_async(request, runtime)

    def reset_file_system_with_options(
        self,
        request: nas20170626_models.ResetFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ResetFileSystemResponse:
        """
        @summary Rolls back a file system to a snapshot of the file system.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        The file system must be in the Running state.
        To roll back a file system to a snapshot, you must specify the ID of the snapshot that is created from the file system.
        
        @param request: ResetFileSystemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ResetFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_file_system_with_options_async(
        self,
        request: nas20170626_models.ResetFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.ResetFileSystemResponse:
        """
        @summary Rolls back a file system to a snapshot of the file system.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        The file system must be in the Running state.
        To roll back a file system to a snapshot, you must specify the ID of the snapshot that is created from the file system.
        
        @param request: ResetFileSystemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.ResetFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_file_system(
        self,
        request: nas20170626_models.ResetFileSystemRequest,
    ) -> nas20170626_models.ResetFileSystemResponse:
        """
        @summary Rolls back a file system to a snapshot of the file system.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        The file system must be in the Running state.
        To roll back a file system to a snapshot, you must specify the ID of the snapshot that is created from the file system.
        
        @param request: ResetFileSystemRequest
        @return: ResetFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_file_system_with_options(request, runtime)

    async def reset_file_system_async(
        self,
        request: nas20170626_models.ResetFileSystemRequest,
    ) -> nas20170626_models.ResetFileSystemResponse:
        """
        @summary Rolls back a file system to a snapshot of the file system.
        
        @description    The snapshot feature is in public preview and is provided free of charge. [File Storage NAS Service Level Agreement (SLA)](https://www.alibabacloud.com/help/legal/latest/network-attached-storage-service-level-agreement) is not guaranteed in public preview.
        Only advanced Extreme NAS file systems support this feature.
        The file system must be in the Running state.
        To roll back a file system to a snapshot, you must specify the ID of the snapshot that is created from the file system.
        
        @param request: ResetFileSystemRequest
        @return: ResetFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_file_system_with_options_async(request, runtime)

    def retry_lifecycle_retrieve_job_with_options(
        self,
        request: nas20170626_models.RetryLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.RetryLifecycleRetrieveJobResponse:
        """
        @summary Retries failed a data retrieval task.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: RetryLifecycleRetrieveJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryLifecycleRetrieveJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.RetryLifecycleRetrieveJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_lifecycle_retrieve_job_with_options_async(
        self,
        request: nas20170626_models.RetryLifecycleRetrieveJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.RetryLifecycleRetrieveJobResponse:
        """
        @summary Retries failed a data retrieval task.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: RetryLifecycleRetrieveJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RetryLifecycleRetrieveJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryLifecycleRetrieveJob',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.RetryLifecycleRetrieveJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_lifecycle_retrieve_job(
        self,
        request: nas20170626_models.RetryLifecycleRetrieveJobRequest,
    ) -> nas20170626_models.RetryLifecycleRetrieveJobResponse:
        """
        @summary Retries failed a data retrieval task.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: RetryLifecycleRetrieveJobRequest
        @return: RetryLifecycleRetrieveJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.retry_lifecycle_retrieve_job_with_options(request, runtime)

    async def retry_lifecycle_retrieve_job_async(
        self,
        request: nas20170626_models.RetryLifecycleRetrieveJobRequest,
    ) -> nas20170626_models.RetryLifecycleRetrieveJobResponse:
        """
        @summary Retries failed a data retrieval task.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: RetryLifecycleRetrieveJobRequest
        @return: RetryLifecycleRetrieveJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.retry_lifecycle_retrieve_job_with_options_async(request, runtime)

    def set_dir_quota_with_options(
        self,
        request: nas20170626_models.SetDirQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.SetDirQuotaResponse:
        """
        @summary Creates a directory quota for a file system.
        
        @description Only General-purpose File Storage NAS (NAS) file systems support the directory quota feature.
        
        @param request: SetDirQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDirQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_count_limit):
            query['FileCountLimit'] = request.file_count_limit
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.quota_type):
            query['QuotaType'] = request.quota_type
        if not UtilClient.is_unset(request.size_limit):
            query['SizeLimit'] = request.size_limit
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDirQuota',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.SetDirQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dir_quota_with_options_async(
        self,
        request: nas20170626_models.SetDirQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.SetDirQuotaResponse:
        """
        @summary Creates a directory quota for a file system.
        
        @description Only General-purpose File Storage NAS (NAS) file systems support the directory quota feature.
        
        @param request: SetDirQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDirQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_count_limit):
            query['FileCountLimit'] = request.file_count_limit
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.quota_type):
            query['QuotaType'] = request.quota_type
        if not UtilClient.is_unset(request.size_limit):
            query['SizeLimit'] = request.size_limit
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            query['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDirQuota',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.SetDirQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dir_quota(
        self,
        request: nas20170626_models.SetDirQuotaRequest,
    ) -> nas20170626_models.SetDirQuotaResponse:
        """
        @summary Creates a directory quota for a file system.
        
        @description Only General-purpose File Storage NAS (NAS) file systems support the directory quota feature.
        
        @param request: SetDirQuotaRequest
        @return: SetDirQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_dir_quota_with_options(request, runtime)

    async def set_dir_quota_async(
        self,
        request: nas20170626_models.SetDirQuotaRequest,
    ) -> nas20170626_models.SetDirQuotaResponse:
        """
        @summary Creates a directory quota for a file system.
        
        @description Only General-purpose File Storage NAS (NAS) file systems support the directory quota feature.
        
        @param request: SetDirQuotaRequest
        @return: SetDirQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_dir_quota_with_options_async(request, runtime)

    def set_fileset_quota_with_options(
        self,
        request: nas20170626_models.SetFilesetQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.SetFilesetQuotaResponse:
        """
        @summary Sets the quota for a fileset.
        
        @description    Only Cloud Parallel File Storage (CPFS) for Lingjun V2.7.0 and later support this operation.
        The minimum capacity quota of a fileset is 10 GiB. The scaling step size is 1 GiB.
        A fileset supports a minimum of 10,000 files or directories and a maximum of 10 billion files or directories. The scaling step size is 1.
        When you modify a directory quota, you must set the quota capacity or the file quantity to be greater than the capacity or file quantity that has been used.
        The quota statistics have a 15-minute latency. The actual usage takes effect after 15 minutes.
        
        @param request: SetFilesetQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetFilesetQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_count_limit):
            query['FileCountLimit'] = request.file_count_limit
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        if not UtilClient.is_unset(request.size_limit):
            query['SizeLimit'] = request.size_limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetFilesetQuota',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.SetFilesetQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_fileset_quota_with_options_async(
        self,
        request: nas20170626_models.SetFilesetQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.SetFilesetQuotaResponse:
        """
        @summary Sets the quota for a fileset.
        
        @description    Only Cloud Parallel File Storage (CPFS) for Lingjun V2.7.0 and later support this operation.
        The minimum capacity quota of a fileset is 10 GiB. The scaling step size is 1 GiB.
        A fileset supports a minimum of 10,000 files or directories and a maximum of 10 billion files or directories. The scaling step size is 1.
        When you modify a directory quota, you must set the quota capacity or the file quantity to be greater than the capacity or file quantity that has been used.
        The quota statistics have a 15-minute latency. The actual usage takes effect after 15 minutes.
        
        @param request: SetFilesetQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetFilesetQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_count_limit):
            query['FileCountLimit'] = request.file_count_limit
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        if not UtilClient.is_unset(request.fset_id):
            query['FsetId'] = request.fset_id
        if not UtilClient.is_unset(request.size_limit):
            query['SizeLimit'] = request.size_limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetFilesetQuota',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.SetFilesetQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_fileset_quota(
        self,
        request: nas20170626_models.SetFilesetQuotaRequest,
    ) -> nas20170626_models.SetFilesetQuotaResponse:
        """
        @summary Sets the quota for a fileset.
        
        @description    Only Cloud Parallel File Storage (CPFS) for Lingjun V2.7.0 and later support this operation.
        The minimum capacity quota of a fileset is 10 GiB. The scaling step size is 1 GiB.
        A fileset supports a minimum of 10,000 files or directories and a maximum of 10 billion files or directories. The scaling step size is 1.
        When you modify a directory quota, you must set the quota capacity or the file quantity to be greater than the capacity or file quantity that has been used.
        The quota statistics have a 15-minute latency. The actual usage takes effect after 15 minutes.
        
        @param request: SetFilesetQuotaRequest
        @return: SetFilesetQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_fileset_quota_with_options(request, runtime)

    async def set_fileset_quota_async(
        self,
        request: nas20170626_models.SetFilesetQuotaRequest,
    ) -> nas20170626_models.SetFilesetQuotaResponse:
        """
        @summary Sets the quota for a fileset.
        
        @description    Only Cloud Parallel File Storage (CPFS) for Lingjun V2.7.0 and later support this operation.
        The minimum capacity quota of a fileset is 10 GiB. The scaling step size is 1 GiB.
        A fileset supports a minimum of 10,000 files or directories and a maximum of 10 billion files or directories. The scaling step size is 1.
        When you modify a directory quota, you must set the quota capacity or the file quantity to be greater than the capacity or file quantity that has been used.
        The quota statistics have a 15-minute latency. The actual usage takes effect after 15 minutes.
        
        @param request: SetFilesetQuotaRequest
        @return: SetFilesetQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_fileset_quota_with_options_async(request, runtime)

    def start_data_flow_with_options(
        self,
        request: nas20170626_models.StartDataFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.StartDataFlowResponse:
        """
        @summary Enables a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support data flows. You can view the version information on the file system details page in the console.
        You can enable the data flows that are only in the `Stopped` state.
        If the value of DryRun is `true`, you can check whether sufficient resources are available to enable the specified data flow. If the resources are insufficient, the data flow cannot be enabled.
        It generally takes 2 to 5 minutes to enable a data flow. You can query the data flow status by calling the [DescribeDataFlows](https://help.aliyun.com/document_detail/2402270.html) operation.
        
        @param request: StartDataFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.StartDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_data_flow_with_options_async(
        self,
        request: nas20170626_models.StartDataFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.StartDataFlowResponse:
        """
        @summary Enables a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support data flows. You can view the version information on the file system details page in the console.
        You can enable the data flows that are only in the `Stopped` state.
        If the value of DryRun is `true`, you can check whether sufficient resources are available to enable the specified data flow. If the resources are insufficient, the data flow cannot be enabled.
        It generally takes 2 to 5 minutes to enable a data flow. You can query the data flow status by calling the [DescribeDataFlows](https://help.aliyun.com/document_detail/2402270.html) operation.
        
        @param request: StartDataFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.StartDataFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_data_flow(
        self,
        request: nas20170626_models.StartDataFlowRequest,
    ) -> nas20170626_models.StartDataFlowResponse:
        """
        @summary Enables a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support data flows. You can view the version information on the file system details page in the console.
        You can enable the data flows that are only in the `Stopped` state.
        If the value of DryRun is `true`, you can check whether sufficient resources are available to enable the specified data flow. If the resources are insufficient, the data flow cannot be enabled.
        It generally takes 2 to 5 minutes to enable a data flow. You can query the data flow status by calling the [DescribeDataFlows](https://help.aliyun.com/document_detail/2402270.html) operation.
        
        @param request: StartDataFlowRequest
        @return: StartDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_data_flow_with_options(request, runtime)

    async def start_data_flow_async(
        self,
        request: nas20170626_models.StartDataFlowRequest,
    ) -> nas20170626_models.StartDataFlowResponse:
        """
        @summary Enables a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support data flows. You can view the version information on the file system details page in the console.
        You can enable the data flows that are only in the `Stopped` state.
        If the value of DryRun is `true`, you can check whether sufficient resources are available to enable the specified data flow. If the resources are insufficient, the data flow cannot be enabled.
        It generally takes 2 to 5 minutes to enable a data flow. You can query the data flow status by calling the [DescribeDataFlows](https://help.aliyun.com/document_detail/2402270.html) operation.
        
        @param request: StartDataFlowRequest
        @return: StartDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_data_flow_with_options_async(request, runtime)

    def stop_data_flow_with_options(
        self,
        request: nas20170626_models.StopDataFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.StopDataFlowResponse:
        """
        @summary Disables a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can disable only the dataflows that are in the `Running` state.
        After a dataflow is disabled, you cannot create a dataflow task for the dataflow. If AutoRefresh is configured, source data updates are not synchronized to CPFS.
        After a dataflow is disabled, the dataflow throughput is no longer billed because resources are reclaimed. However, the dataflow may fail to be restarted due to insufficient resources.
        It generally takes 2 to 5 minutes to disable a dataflow. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2402271.html) operation to query the dataflow status.
        
        @param request: StopDataFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.StopDataFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_data_flow_with_options_async(
        self,
        request: nas20170626_models.StopDataFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.StopDataFlowResponse:
        """
        @summary Disables a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can disable only the dataflows that are in the `Running` state.
        After a dataflow is disabled, you cannot create a dataflow task for the dataflow. If AutoRefresh is configured, source data updates are not synchronized to CPFS.
        After a dataflow is disabled, the dataflow throughput is no longer billed because resources are reclaimed. However, the dataflow may fail to be restarted due to insufficient resources.
        It generally takes 2 to 5 minutes to disable a dataflow. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2402271.html) operation to query the dataflow status.
        
        @param request: StopDataFlowRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDataFlowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.data_flow_id):
            query['DataFlowId'] = request.data_flow_id
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDataFlow',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.StopDataFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_data_flow(
        self,
        request: nas20170626_models.StopDataFlowRequest,
    ) -> nas20170626_models.StopDataFlowResponse:
        """
        @summary Disables a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can disable only the dataflows that are in the `Running` state.
        After a dataflow is disabled, you cannot create a dataflow task for the dataflow. If AutoRefresh is configured, source data updates are not synchronized to CPFS.
        After a dataflow is disabled, the dataflow throughput is no longer billed because resources are reclaimed. However, the dataflow may fail to be restarted due to insufficient resources.
        It generally takes 2 to 5 minutes to disable a dataflow. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2402271.html) operation to query the dataflow status.
        
        @param request: StopDataFlowRequest
        @return: StopDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_data_flow_with_options(request, runtime)

    async def stop_data_flow_async(
        self,
        request: nas20170626_models.StopDataFlowRequest,
    ) -> nas20170626_models.StopDataFlowResponse:
        """
        @summary Disables a dataflow.
        
        @description    This operation is available only to Cloud Parallel File Storage (CPFS) file systems on the China site (aliyun.com).
        Only CPFS V2.2.0 and later support dataflows. You can view the version information on the file system details page in the console.
        You can disable only the dataflows that are in the `Running` state.
        After a dataflow is disabled, you cannot create a dataflow task for the dataflow. If AutoRefresh is configured, source data updates are not synchronized to CPFS.
        After a dataflow is disabled, the dataflow throughput is no longer billed because resources are reclaimed. However, the dataflow may fail to be restarted due to insufficient resources.
        It generally takes 2 to 5 minutes to disable a dataflow. You can call the [DescribeDataFlows](https://help.aliyun.com/document_detail/2402271.html) operation to query the dataflow status.
        
        @param request: StopDataFlowRequest
        @return: StopDataFlowResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_data_flow_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: nas20170626_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.TagResourcesResponse:
        """
        @summary Creates tags and binds the tags to file systems.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: nas20170626_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.TagResourcesResponse:
        """
        @summary Creates tags and binds the tags to file systems.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: nas20170626_models.TagResourcesRequest,
    ) -> nas20170626_models.TagResourcesResponse:
        """
        @summary Creates tags and binds the tags to file systems.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: nas20170626_models.TagResourcesRequest,
    ) -> nas20170626_models.TagResourcesResponse:
        """
        @summary Creates tags and binds the tags to file systems.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: nas20170626_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UntagResourcesResponse:
        """
        @summary Removes tags from a file system.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: nas20170626_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UntagResourcesResponse:
        """
        @summary Removes tags from a file system.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: nas20170626_models.UntagResourcesRequest,
    ) -> nas20170626_models.UntagResourcesResponse:
        """
        @summary Removes tags from a file system.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: nas20170626_models.UntagResourcesRequest,
    ) -> nas20170626_models.UntagResourcesResponse:
        """
        @summary Removes tags from a file system.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_recycle_bin_attribute_with_options(
        self,
        request: nas20170626_models.UpdateRecycleBinAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UpdateRecycleBinAttributeResponse:
        """
        @summary Modifies the retention period of data in the recycle bin of a file system.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: UpdateRecycleBinAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRecycleBinAttributeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecycleBinAttribute',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.UpdateRecycleBinAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_recycle_bin_attribute_with_options_async(
        self,
        request: nas20170626_models.UpdateRecycleBinAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UpdateRecycleBinAttributeResponse:
        """
        @summary Modifies the retention period of data in the recycle bin of a file system.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: UpdateRecycleBinAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRecycleBinAttributeResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecycleBinAttribute',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.UpdateRecycleBinAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_recycle_bin_attribute(
        self,
        request: nas20170626_models.UpdateRecycleBinAttributeRequest,
    ) -> nas20170626_models.UpdateRecycleBinAttributeResponse:
        """
        @summary Modifies the retention period of data in the recycle bin of a file system.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: UpdateRecycleBinAttributeRequest
        @return: UpdateRecycleBinAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_recycle_bin_attribute_with_options(request, runtime)

    async def update_recycle_bin_attribute_async(
        self,
        request: nas20170626_models.UpdateRecycleBinAttributeRequest,
    ) -> nas20170626_models.UpdateRecycleBinAttributeResponse:
        """
        @summary Modifies the retention period of data in the recycle bin of a file system.
        
        @description Only General-purpose NAS file systems support this operation.
        
        @param request: UpdateRecycleBinAttributeRequest
        @return: UpdateRecycleBinAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_recycle_bin_attribute_with_options_async(request, runtime)

    def upgrade_file_system_with_options(
        self,
        request: nas20170626_models.UpgradeFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UpgradeFileSystemResponse:
        """
        @summary Scales up an Extreme NAS file system or a Cloud Parallel File Storage (CPFS) file system.
        
        @description    Only Extreme NAS file systems and CPFS file systems can be scaled up. CPFS file systems are available only on the China site (aliyun.com).
        A General-purpose NAS file system is automatically scaled up. You do not need to call this operation to scale up a General-purpose NAS file system.
        
        @param request: UpgradeFileSystemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.UpgradeFileSystemResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_file_system_with_options_async(
        self,
        request: nas20170626_models.UpgradeFileSystemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nas20170626_models.UpgradeFileSystemResponse:
        """
        @summary Scales up an Extreme NAS file system or a Cloud Parallel File Storage (CPFS) file system.
        
        @description    Only Extreme NAS file systems and CPFS file systems can be scaled up. CPFS file systems are available only on the China site (aliyun.com).
        A General-purpose NAS file system is automatically scaled up. You do not need to call this operation to scale up a General-purpose NAS file system.
        
        @param request: UpgradeFileSystemRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeFileSystemResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.file_system_id):
            query['FileSystemId'] = request.file_system_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeFileSystem',
            version='2017-06-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nas20170626_models.UpgradeFileSystemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_file_system(
        self,
        request: nas20170626_models.UpgradeFileSystemRequest,
    ) -> nas20170626_models.UpgradeFileSystemResponse:
        """
        @summary Scales up an Extreme NAS file system or a Cloud Parallel File Storage (CPFS) file system.
        
        @description    Only Extreme NAS file systems and CPFS file systems can be scaled up. CPFS file systems are available only on the China site (aliyun.com).
        A General-purpose NAS file system is automatically scaled up. You do not need to call this operation to scale up a General-purpose NAS file system.
        
        @param request: UpgradeFileSystemRequest
        @return: UpgradeFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_file_system_with_options(request, runtime)

    async def upgrade_file_system_async(
        self,
        request: nas20170626_models.UpgradeFileSystemRequest,
    ) -> nas20170626_models.UpgradeFileSystemResponse:
        """
        @summary Scales up an Extreme NAS file system or a Cloud Parallel File Storage (CPFS) file system.
        
        @description    Only Extreme NAS file systems and CPFS file systems can be scaled up. CPFS file systems are available only on the China site (aliyun.com).
        A General-purpose NAS file system is automatically scaled up. You do not need to call this operation to scale up a General-purpose NAS file system.
        
        @param request: UpgradeFileSystemRequest
        @return: UpgradeFileSystemResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_file_system_with_options_async(request, runtime)
