# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_nis20211216 import models as nis_20211216_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('nis', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_and_analyze_network_path_with_options(
        self,
        request: nis_20211216_models.CreateAndAnalyzeNetworkPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.CreateAndAnalyzeNetworkPathResponse:
        """
        @summary Initiates a task for analyzing network reachability.
        
        @description You can call this operation to initiate a task for analyzing network reachability by specifying only the information about the source and destination. You do not need to create a network path for reachability analysis. The analysis result is not recorded in the system. If you want to record the path parameters and analysis result in the Network Intelligence Service (NIS) console, we recommend that you call the *createNetworkReachableAnalysis** operation.
        
        @param request: CreateAndAnalyzeNetworkPathRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAndAnalyzeNetworkPathResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAndAnalyzeNetworkPath',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.CreateAndAnalyzeNetworkPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_and_analyze_network_path_with_options_async(
        self,
        request: nis_20211216_models.CreateAndAnalyzeNetworkPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.CreateAndAnalyzeNetworkPathResponse:
        """
        @summary Initiates a task for analyzing network reachability.
        
        @description You can call this operation to initiate a task for analyzing network reachability by specifying only the information about the source and destination. You do not need to create a network path for reachability analysis. The analysis result is not recorded in the system. If you want to record the path parameters and analysis result in the Network Intelligence Service (NIS) console, we recommend that you call the *createNetworkReachableAnalysis** operation.
        
        @param request: CreateAndAnalyzeNetworkPathRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAndAnalyzeNetworkPathResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAndAnalyzeNetworkPath',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.CreateAndAnalyzeNetworkPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_and_analyze_network_path(
        self,
        request: nis_20211216_models.CreateAndAnalyzeNetworkPathRequest,
    ) -> nis_20211216_models.CreateAndAnalyzeNetworkPathResponse:
        """
        @summary Initiates a task for analyzing network reachability.
        
        @description You can call this operation to initiate a task for analyzing network reachability by specifying only the information about the source and destination. You do not need to create a network path for reachability analysis. The analysis result is not recorded in the system. If you want to record the path parameters and analysis result in the Network Intelligence Service (NIS) console, we recommend that you call the *createNetworkReachableAnalysis** operation.
        
        @param request: CreateAndAnalyzeNetworkPathRequest
        @return: CreateAndAnalyzeNetworkPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_and_analyze_network_path_with_options(request, runtime)

    async def create_and_analyze_network_path_async(
        self,
        request: nis_20211216_models.CreateAndAnalyzeNetworkPathRequest,
    ) -> nis_20211216_models.CreateAndAnalyzeNetworkPathResponse:
        """
        @summary Initiates a task for analyzing network reachability.
        
        @description You can call this operation to initiate a task for analyzing network reachability by specifying only the information about the source and destination. You do not need to create a network path for reachability analysis. The analysis result is not recorded in the system. If you want to record the path parameters and analysis result in the Network Intelligence Service (NIS) console, we recommend that you call the *createNetworkReachableAnalysis** operation.
        
        @param request: CreateAndAnalyzeNetworkPathRequest
        @return: CreateAndAnalyzeNetworkPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_and_analyze_network_path_with_options_async(request, runtime)

    def create_network_path_with_options(
        self,
        request: nis_20211216_models.CreateNetworkPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.CreateNetworkPathResponse:
        """
        @summary Creates a network path in the cloud for reachability analysis.
        
        @description    You can call the **CreateNetworkPath** operation to create network paths in multiple networking scenarios and between multiple resources. After a path is created, the path parameters are saved for repeated analysis.
        You can create up to 100 network paths within one Alibaba Cloud account.
        
        @param request: CreateNetworkPathRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkPathResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_path_description):
            query['NetworkPathDescription'] = request.network_path_description
        if not UtilClient.is_unset(request.network_path_name):
            query['NetworkPathName'] = request.network_path_name
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_ip_address):
            query['SourceIpAddress'] = request.source_ip_address
        if not UtilClient.is_unset(request.source_port):
            query['SourcePort'] = request.source_port
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_ip_address):
            query['TargetIpAddress'] = request.target_ip_address
        if not UtilClient.is_unset(request.target_port):
            query['TargetPort'] = request.target_port
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkPath',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.CreateNetworkPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_path_with_options_async(
        self,
        request: nis_20211216_models.CreateNetworkPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.CreateNetworkPathResponse:
        """
        @summary Creates a network path in the cloud for reachability analysis.
        
        @description    You can call the **CreateNetworkPath** operation to create network paths in multiple networking scenarios and between multiple resources. After a path is created, the path parameters are saved for repeated analysis.
        You can create up to 100 network paths within one Alibaba Cloud account.
        
        @param request: CreateNetworkPathRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkPathResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_path_description):
            query['NetworkPathDescription'] = request.network_path_description
        if not UtilClient.is_unset(request.network_path_name):
            query['NetworkPathName'] = request.network_path_name
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_id):
            query['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.source_ip_address):
            query['SourceIpAddress'] = request.source_ip_address
        if not UtilClient.is_unset(request.source_port):
            query['SourcePort'] = request.source_port
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.target_ip_address):
            query['TargetIpAddress'] = request.target_ip_address
        if not UtilClient.is_unset(request.target_port):
            query['TargetPort'] = request.target_port
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkPath',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.CreateNetworkPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_path(
        self,
        request: nis_20211216_models.CreateNetworkPathRequest,
    ) -> nis_20211216_models.CreateNetworkPathResponse:
        """
        @summary Creates a network path in the cloud for reachability analysis.
        
        @description    You can call the **CreateNetworkPath** operation to create network paths in multiple networking scenarios and between multiple resources. After a path is created, the path parameters are saved for repeated analysis.
        You can create up to 100 network paths within one Alibaba Cloud account.
        
        @param request: CreateNetworkPathRequest
        @return: CreateNetworkPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_network_path_with_options(request, runtime)

    async def create_network_path_async(
        self,
        request: nis_20211216_models.CreateNetworkPathRequest,
    ) -> nis_20211216_models.CreateNetworkPathResponse:
        """
        @summary Creates a network path in the cloud for reachability analysis.
        
        @description    You can call the **CreateNetworkPath** operation to create network paths in multiple networking scenarios and between multiple resources. After a path is created, the path parameters are saved for repeated analysis.
        You can create up to 100 network paths within one Alibaba Cloud account.
        
        @param request: CreateNetworkPathRequest
        @return: CreateNetworkPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_network_path_with_options_async(request, runtime)

    def create_network_reachable_analysis_with_options(
        self,
        request: nis_20211216_models.CreateNetworkReachableAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.CreateNetworkReachableAnalysisResponse:
        """
        @summary Creates a task for analyzing network reachability.
        
        @description    The **CreateNetworkReachableAnalysis** operation is used to create a task for analyzing the reachability of the network path that is created by calling the **CreateNetworkPath** operation and record the analysis results.
        The **CreateNetworkReachableAnalysis** operation can be called to repeatedly analyze the reachability of a network path.
        You can create up to 1,000 reachability analysis records within one Alibaba Cloud account.
        
        @param request: CreateNetworkReachableAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkReachableAnalysisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_path_id):
            query['NetworkPathId'] = request.network_path_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkReachableAnalysis',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.CreateNetworkReachableAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_network_reachable_analysis_with_options_async(
        self,
        request: nis_20211216_models.CreateNetworkReachableAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.CreateNetworkReachableAnalysisResponse:
        """
        @summary Creates a task for analyzing network reachability.
        
        @description    The **CreateNetworkReachableAnalysis** operation is used to create a task for analyzing the reachability of the network path that is created by calling the **CreateNetworkPath** operation and record the analysis results.
        The **CreateNetworkReachableAnalysis** operation can be called to repeatedly analyze the reachability of a network path.
        You can create up to 1,000 reachability analysis records within one Alibaba Cloud account.
        
        @param request: CreateNetworkReachableAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetworkReachableAnalysisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_path_id):
            query['NetworkPathId'] = request.network_path_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNetworkReachableAnalysis',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.CreateNetworkReachableAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_network_reachable_analysis(
        self,
        request: nis_20211216_models.CreateNetworkReachableAnalysisRequest,
    ) -> nis_20211216_models.CreateNetworkReachableAnalysisResponse:
        """
        @summary Creates a task for analyzing network reachability.
        
        @description    The **CreateNetworkReachableAnalysis** operation is used to create a task for analyzing the reachability of the network path that is created by calling the **CreateNetworkPath** operation and record the analysis results.
        The **CreateNetworkReachableAnalysis** operation can be called to repeatedly analyze the reachability of a network path.
        You can create up to 1,000 reachability analysis records within one Alibaba Cloud account.
        
        @param request: CreateNetworkReachableAnalysisRequest
        @return: CreateNetworkReachableAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_network_reachable_analysis_with_options(request, runtime)

    async def create_network_reachable_analysis_async(
        self,
        request: nis_20211216_models.CreateNetworkReachableAnalysisRequest,
    ) -> nis_20211216_models.CreateNetworkReachableAnalysisResponse:
        """
        @summary Creates a task for analyzing network reachability.
        
        @description    The **CreateNetworkReachableAnalysis** operation is used to create a task for analyzing the reachability of the network path that is created by calling the **CreateNetworkPath** operation and record the analysis results.
        The **CreateNetworkReachableAnalysis** operation can be called to repeatedly analyze the reachability of a network path.
        You can create up to 1,000 reachability analysis records within one Alibaba Cloud account.
        
        @param request: CreateNetworkReachableAnalysisRequest
        @return: CreateNetworkReachableAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_network_reachable_analysis_with_options_async(request, runtime)

    def delete_network_path_with_options(
        self,
        tmp_req: nis_20211216_models.DeleteNetworkPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.DeleteNetworkPathResponse:
        """
        @summary Deletes a network path.
        
        @param tmp_req: DeleteNetworkPathRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkPathResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nis_20211216_models.DeleteNetworkPathShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.network_path_ids):
            request.network_path_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network_path_ids, 'NetworkPathIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.network_path_ids_shrink):
            query['NetworkPathIds'] = request.network_path_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkPath',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.DeleteNetworkPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_path_with_options_async(
        self,
        tmp_req: nis_20211216_models.DeleteNetworkPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.DeleteNetworkPathResponse:
        """
        @summary Deletes a network path.
        
        @param tmp_req: DeleteNetworkPathRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkPathResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nis_20211216_models.DeleteNetworkPathShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.network_path_ids):
            request.network_path_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network_path_ids, 'NetworkPathIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.network_path_ids_shrink):
            query['NetworkPathIds'] = request.network_path_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkPath',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.DeleteNetworkPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_path(
        self,
        request: nis_20211216_models.DeleteNetworkPathRequest,
    ) -> nis_20211216_models.DeleteNetworkPathResponse:
        """
        @summary Deletes a network path.
        
        @param request: DeleteNetworkPathRequest
        @return: DeleteNetworkPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_network_path_with_options(request, runtime)

    async def delete_network_path_async(
        self,
        request: nis_20211216_models.DeleteNetworkPathRequest,
    ) -> nis_20211216_models.DeleteNetworkPathResponse:
        """
        @summary Deletes a network path.
        
        @param request: DeleteNetworkPathRequest
        @return: DeleteNetworkPathResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_path_with_options_async(request, runtime)

    def delete_network_reachable_analysis_with_options(
        self,
        tmp_req: nis_20211216_models.DeleteNetworkReachableAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.DeleteNetworkReachableAnalysisResponse:
        """
        @summary Deletes a task for analyzing network reachability.
        
        @param tmp_req: DeleteNetworkReachableAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkReachableAnalysisResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nis_20211216_models.DeleteNetworkReachableAnalysisShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.network_reachable_analysis_ids):
            request.network_reachable_analysis_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network_reachable_analysis_ids, 'NetworkReachableAnalysisIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.network_reachable_analysis_ids_shrink):
            query['NetworkReachableAnalysisIds'] = request.network_reachable_analysis_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkReachableAnalysis',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.DeleteNetworkReachableAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_network_reachable_analysis_with_options_async(
        self,
        tmp_req: nis_20211216_models.DeleteNetworkReachableAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.DeleteNetworkReachableAnalysisResponse:
        """
        @summary Deletes a task for analyzing network reachability.
        
        @param tmp_req: DeleteNetworkReachableAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNetworkReachableAnalysisResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nis_20211216_models.DeleteNetworkReachableAnalysisShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.network_reachable_analysis_ids):
            request.network_reachable_analysis_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.network_reachable_analysis_ids, 'NetworkReachableAnalysisIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.network_reachable_analysis_ids_shrink):
            query['NetworkReachableAnalysisIds'] = request.network_reachable_analysis_ids_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNetworkReachableAnalysis',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.DeleteNetworkReachableAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_network_reachable_analysis(
        self,
        request: nis_20211216_models.DeleteNetworkReachableAnalysisRequest,
    ) -> nis_20211216_models.DeleteNetworkReachableAnalysisResponse:
        """
        @summary Deletes a task for analyzing network reachability.
        
        @param request: DeleteNetworkReachableAnalysisRequest
        @return: DeleteNetworkReachableAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_network_reachable_analysis_with_options(request, runtime)

    async def delete_network_reachable_analysis_async(
        self,
        request: nis_20211216_models.DeleteNetworkReachableAnalysisRequest,
    ) -> nis_20211216_models.DeleteNetworkReachableAnalysisResponse:
        """
        @summary Deletes a task for analyzing network reachability.
        
        @param request: DeleteNetworkReachableAnalysisRequest
        @return: DeleteNetworkReachableAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_reachable_analysis_with_options_async(request, runtime)

    def get_internet_tuple_with_options(
        self,
        tmp_req: nis_20211216_models.GetInternetTupleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.GetInternetTupleResponse:
        """
        @summary Queries the rankings of Internet traffic data in the form of 1-tuple, 2-tuple, or 5-tuple. Internet traffic data can be ranked by metrics such as traffic volumes and the number of packets.
        
        @param tmp_req: GetInternetTupleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInternetTupleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nis_20211216_models.GetInternetTupleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cloud_ip_list):
            request.cloud_ip_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cloud_ip_list, 'CloudIpList', 'json')
        if not UtilClient.is_unset(tmp_req.instance_list):
            request.instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.cloud_ip):
            query['CloudIp'] = request.cloud_ip
        if not UtilClient.is_unset(request.cloud_ip_list_shrink):
            query['CloudIpList'] = request.cloud_ip_list_shrink
        if not UtilClient.is_unset(request.cloud_isp):
            query['CloudIsp'] = request.cloud_isp
        if not UtilClient.is_unset(request.cloud_port):
            query['CloudPort'] = request.cloud_port
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.other_city):
            query['OtherCity'] = request.other_city
        if not UtilClient.is_unset(request.other_country):
            query['OtherCountry'] = request.other_country
        if not UtilClient.is_unset(request.other_ip):
            query['OtherIp'] = request.other_ip
        if not UtilClient.is_unset(request.other_isp):
            query['OtherIsp'] = request.other_isp
        if not UtilClient.is_unset(request.other_port):
            query['OtherPort'] = request.other_port
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.top_n):
            query['TopN'] = request.top_n
        if not UtilClient.is_unset(request.tuple_type):
            query['TupleType'] = request.tuple_type
        if not UtilClient.is_unset(request.use_multi_account):
            query['UseMultiAccount'] = request.use_multi_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInternetTuple',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.GetInternetTupleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_internet_tuple_with_options_async(
        self,
        tmp_req: nis_20211216_models.GetInternetTupleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.GetInternetTupleResponse:
        """
        @summary Queries the rankings of Internet traffic data in the form of 1-tuple, 2-tuple, or 5-tuple. Internet traffic data can be ranked by metrics such as traffic volumes and the number of packets.
        
        @param tmp_req: GetInternetTupleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInternetTupleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nis_20211216_models.GetInternetTupleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cloud_ip_list):
            request.cloud_ip_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cloud_ip_list, 'CloudIpList', 'json')
        if not UtilClient.is_unset(tmp_req.instance_list):
            request.instance_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_list, 'InstanceList', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.cloud_ip):
            query['CloudIp'] = request.cloud_ip
        if not UtilClient.is_unset(request.cloud_ip_list_shrink):
            query['CloudIpList'] = request.cloud_ip_list_shrink
        if not UtilClient.is_unset(request.cloud_isp):
            query['CloudIsp'] = request.cloud_isp
        if not UtilClient.is_unset(request.cloud_port):
            query['CloudPort'] = request.cloud_port
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_list_shrink):
            query['InstanceList'] = request.instance_list_shrink
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.other_city):
            query['OtherCity'] = request.other_city
        if not UtilClient.is_unset(request.other_country):
            query['OtherCountry'] = request.other_country
        if not UtilClient.is_unset(request.other_ip):
            query['OtherIp'] = request.other_ip
        if not UtilClient.is_unset(request.other_isp):
            query['OtherIsp'] = request.other_isp
        if not UtilClient.is_unset(request.other_port):
            query['OtherPort'] = request.other_port
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.top_n):
            query['TopN'] = request.top_n
        if not UtilClient.is_unset(request.tuple_type):
            query['TupleType'] = request.tuple_type
        if not UtilClient.is_unset(request.use_multi_account):
            query['UseMultiAccount'] = request.use_multi_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInternetTuple',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.GetInternetTupleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_internet_tuple(
        self,
        request: nis_20211216_models.GetInternetTupleRequest,
    ) -> nis_20211216_models.GetInternetTupleResponse:
        """
        @summary Queries the rankings of Internet traffic data in the form of 1-tuple, 2-tuple, or 5-tuple. Internet traffic data can be ranked by metrics such as traffic volumes and the number of packets.
        
        @param request: GetInternetTupleRequest
        @return: GetInternetTupleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_internet_tuple_with_options(request, runtime)

    async def get_internet_tuple_async(
        self,
        request: nis_20211216_models.GetInternetTupleRequest,
    ) -> nis_20211216_models.GetInternetTupleResponse:
        """
        @summary Queries the rankings of Internet traffic data in the form of 1-tuple, 2-tuple, or 5-tuple. Internet traffic data can be ranked by metrics such as traffic volumes and the number of packets.
        
        @param request: GetInternetTupleRequest
        @return: GetInternetTupleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_internet_tuple_with_options_async(request, runtime)

    def get_nat_top_nwith_options(
        self,
        request: nis_20211216_models.GetNatTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.GetNatTopNResponse:
        """
        @summary Queries the real-time SNAT performance ranking of a NAT gateway.
        
        @param request: GetNatTopNRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNatTopNResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.top_n):
            query['TopN'] = request.top_n
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNatTopN',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.GetNatTopNResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_nat_top_nwith_options_async(
        self,
        request: nis_20211216_models.GetNatTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.GetNatTopNResponse:
        """
        @summary Queries the real-time SNAT performance ranking of a NAT gateway.
        
        @param request: GetNatTopNRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNatTopNResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.nat_gateway_id):
            query['NatGatewayId'] = request.nat_gateway_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.top_n):
            query['TopN'] = request.top_n
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNatTopN',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.GetNatTopNResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_nat_top_n(
        self,
        request: nis_20211216_models.GetNatTopNRequest,
    ) -> nis_20211216_models.GetNatTopNResponse:
        """
        @summary Queries the real-time SNAT performance ranking of a NAT gateway.
        
        @param request: GetNatTopNRequest
        @return: GetNatTopNResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_nat_top_nwith_options(request, runtime)

    async def get_nat_top_n_async(
        self,
        request: nis_20211216_models.GetNatTopNRequest,
    ) -> nis_20211216_models.GetNatTopNResponse:
        """
        @summary Queries the real-time SNAT performance ranking of a NAT gateway.
        
        @param request: GetNatTopNRequest
        @return: GetNatTopNResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_nat_top_nwith_options_async(request, runtime)

    def get_network_reachable_analysis_with_options(
        self,
        request: nis_20211216_models.GetNetworkReachableAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.GetNetworkReachableAnalysisResponse:
        """
        @summary Obtains the results of network reachability analysis.
        
        @description *GetNetworkReachableAnalysis** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can query the state of the task for analyzing network reachability.
        The **init** state indicates that the task is in progress.
        The **finish** state indicates that the task is complete. In this state, you can obtain the analysis result.
        
        @param request: GetNetworkReachableAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNetworkReachableAnalysisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_reachable_analysis_id):
            query['NetworkReachableAnalysisId'] = request.network_reachable_analysis_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetworkReachableAnalysis',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.GetNetworkReachableAnalysisResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_reachable_analysis_with_options_async(
        self,
        request: nis_20211216_models.GetNetworkReachableAnalysisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.GetNetworkReachableAnalysisResponse:
        """
        @summary Obtains the results of network reachability analysis.
        
        @description *GetNetworkReachableAnalysis** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can query the state of the task for analyzing network reachability.
        The **init** state indicates that the task is in progress.
        The **finish** state indicates that the task is complete. In this state, you can obtain the analysis result.
        
        @param request: GetNetworkReachableAnalysisRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNetworkReachableAnalysisResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.network_reachable_analysis_id):
            query['NetworkReachableAnalysisId'] = request.network_reachable_analysis_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetworkReachableAnalysis',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.GetNetworkReachableAnalysisResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network_reachable_analysis(
        self,
        request: nis_20211216_models.GetNetworkReachableAnalysisRequest,
    ) -> nis_20211216_models.GetNetworkReachableAnalysisResponse:
        """
        @summary Obtains the results of network reachability analysis.
        
        @description *GetNetworkReachableAnalysis** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can query the state of the task for analyzing network reachability.
        The **init** state indicates that the task is in progress.
        The **finish** state indicates that the task is complete. In this state, you can obtain the analysis result.
        
        @param request: GetNetworkReachableAnalysisRequest
        @return: GetNetworkReachableAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_network_reachable_analysis_with_options(request, runtime)

    async def get_network_reachable_analysis_async(
        self,
        request: nis_20211216_models.GetNetworkReachableAnalysisRequest,
    ) -> nis_20211216_models.GetNetworkReachableAnalysisResponse:
        """
        @summary Obtains the results of network reachability analysis.
        
        @description *GetNetworkReachableAnalysis** is an asynchronous operation. After a request is sent, the system returns a request ID and runs the task in the background. You can query the state of the task for analyzing network reachability.
        The **init** state indicates that the task is in progress.
        The **finish** state indicates that the task is complete. In this state, you can obtain the analysis result.
        
        @param request: GetNetworkReachableAnalysisRequest
        @return: GetNetworkReachableAnalysisResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_network_reachable_analysis_with_options_async(request, runtime)

    def get_nis_network_metrics_with_options(
        self,
        tmp_req: nis_20211216_models.GetNisNetworkMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.GetNisNetworkMetricsResponse:
        """
        @summary 获取云网络指标趋势
        
        @param tmp_req: GetNisNetworkMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNisNetworkMetricsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nis_20211216_models.GetNisNetworkMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dimensions):
            request.dimensions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scan_by):
            query['ScanBy'] = request.scan_by
        if not UtilClient.is_unset(request.use_cross_account):
            query['UseCrossAccount'] = request.use_cross_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNisNetworkMetrics',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.GetNisNetworkMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_nis_network_metrics_with_options_async(
        self,
        tmp_req: nis_20211216_models.GetNisNetworkMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.GetNisNetworkMetricsResponse:
        """
        @summary 获取云网络指标趋势
        
        @param tmp_req: GetNisNetworkMetricsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNisNetworkMetricsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nis_20211216_models.GetNisNetworkMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dimensions):
            request.dimensions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dimensions, 'Dimensions', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.dimensions_shrink):
            query['Dimensions'] = request.dimensions_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scan_by):
            query['ScanBy'] = request.scan_by
        if not UtilClient.is_unset(request.use_cross_account):
            query['UseCrossAccount'] = request.use_cross_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNisNetworkMetrics',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.GetNisNetworkMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_nis_network_metrics(
        self,
        request: nis_20211216_models.GetNisNetworkMetricsRequest,
    ) -> nis_20211216_models.GetNisNetworkMetricsResponse:
        """
        @summary 获取云网络指标趋势
        
        @param request: GetNisNetworkMetricsRequest
        @return: GetNisNetworkMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_nis_network_metrics_with_options(request, runtime)

    async def get_nis_network_metrics_async(
        self,
        request: nis_20211216_models.GetNisNetworkMetricsRequest,
    ) -> nis_20211216_models.GetNisNetworkMetricsResponse:
        """
        @summary 获取云网络指标趋势
        
        @param request: GetNisNetworkMetricsRequest
        @return: GetNisNetworkMetricsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_nis_network_metrics_with_options_async(request, runtime)

    def get_nis_network_ranking_with_options(
        self,
        tmp_req: nis_20211216_models.GetNisNetworkRankingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.GetNisNetworkRankingResponse:
        """
        @summary 获取云网络指标排名
        
        @param tmp_req: GetNisNetworkRankingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNisNetworkRankingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nis_20211216_models.GetNisNetworkRankingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.top_n):
            query['TopN'] = request.top_n
        if not UtilClient.is_unset(request.use_cross_account):
            query['UseCrossAccount'] = request.use_cross_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNisNetworkRanking',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.GetNisNetworkRankingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_nis_network_ranking_with_options_async(
        self,
        tmp_req: nis_20211216_models.GetNisNetworkRankingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.GetNisNetworkRankingResponse:
        """
        @summary 获取云网络指标排名
        
        @param tmp_req: GetNisNetworkRankingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNisNetworkRankingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nis_20211216_models.GetNisNetworkRankingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter_shrink):
            query['Filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.region_no):
            query['RegionNo'] = request.region_no
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.top_n):
            query['TopN'] = request.top_n
        if not UtilClient.is_unset(request.use_cross_account):
            query['UseCrossAccount'] = request.use_cross_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNisNetworkRanking',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.GetNisNetworkRankingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_nis_network_ranking(
        self,
        request: nis_20211216_models.GetNisNetworkRankingRequest,
    ) -> nis_20211216_models.GetNisNetworkRankingResponse:
        """
        @summary 获取云网络指标排名
        
        @param request: GetNisNetworkRankingRequest
        @return: GetNisNetworkRankingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_nis_network_ranking_with_options(request, runtime)

    async def get_nis_network_ranking_async(
        self,
        request: nis_20211216_models.GetNisNetworkRankingRequest,
    ) -> nis_20211216_models.GetNisNetworkRankingResponse:
        """
        @summary 获取云网络指标排名
        
        @param request: GetNisNetworkRankingRequest
        @return: GetNisNetworkRankingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_nis_network_ranking_with_options_async(request, runtime)

    def get_transit_router_flow_top_nwith_options(
        self,
        tmp_req: nis_20211216_models.GetTransitRouterFlowTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.GetTransitRouterFlowTopNResponse:
        """
        @summary Queries the rankings of inter-region traffic data in the form of 1-tuple, 2-tuple, or 5-tuple. Inter-region traffic data can be ranked by metrics such as traffic volumes and the number of packets.
        
        @param tmp_req: GetTransitRouterFlowTopNRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTransitRouterFlowTopNResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nis_20211216_models.GetTransitRouterFlowTopNShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.bandwith_package_id):
            query['BandwithPackageId'] = request.bandwith_package_id
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.other_ip):
            query['OtherIp'] = request.other_ip
        if not UtilClient.is_unset(request.other_port):
            query['OtherPort'] = request.other_port
        if not UtilClient.is_unset(request.other_region):
            query['OtherRegion'] = request.other_region
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.this_ip):
            query['ThisIp'] = request.this_ip
        if not UtilClient.is_unset(request.this_port):
            query['ThisPort'] = request.this_port
        if not UtilClient.is_unset(request.this_region):
            query['ThisRegion'] = request.this_region
        if not UtilClient.is_unset(request.top_n):
            query['TopN'] = request.top_n
        if not UtilClient.is_unset(request.use_multi_account):
            query['UseMultiAccount'] = request.use_multi_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTransitRouterFlowTopN',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.GetTransitRouterFlowTopNResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_transit_router_flow_top_nwith_options_async(
        self,
        tmp_req: nis_20211216_models.GetTransitRouterFlowTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.GetTransitRouterFlowTopNResponse:
        """
        @summary Queries the rankings of inter-region traffic data in the form of 1-tuple, 2-tuple, or 5-tuple. Inter-region traffic data can be ranked by metrics such as traffic volumes and the number of packets.
        
        @param tmp_req: GetTransitRouterFlowTopNRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTransitRouterFlowTopNResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nis_20211216_models.GetTransitRouterFlowTopNShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.bandwith_package_id):
            query['BandwithPackageId'] = request.bandwith_package_id
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.other_ip):
            query['OtherIp'] = request.other_ip
        if not UtilClient.is_unset(request.other_port):
            query['OtherPort'] = request.other_port
        if not UtilClient.is_unset(request.other_region):
            query['OtherRegion'] = request.other_region
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.this_ip):
            query['ThisIp'] = request.this_ip
        if not UtilClient.is_unset(request.this_port):
            query['ThisPort'] = request.this_port
        if not UtilClient.is_unset(request.this_region):
            query['ThisRegion'] = request.this_region
        if not UtilClient.is_unset(request.top_n):
            query['TopN'] = request.top_n
        if not UtilClient.is_unset(request.use_multi_account):
            query['UseMultiAccount'] = request.use_multi_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTransitRouterFlowTopN',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.GetTransitRouterFlowTopNResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_transit_router_flow_top_n(
        self,
        request: nis_20211216_models.GetTransitRouterFlowTopNRequest,
    ) -> nis_20211216_models.GetTransitRouterFlowTopNResponse:
        """
        @summary Queries the rankings of inter-region traffic data in the form of 1-tuple, 2-tuple, or 5-tuple. Inter-region traffic data can be ranked by metrics such as traffic volumes and the number of packets.
        
        @param request: GetTransitRouterFlowTopNRequest
        @return: GetTransitRouterFlowTopNResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_transit_router_flow_top_nwith_options(request, runtime)

    async def get_transit_router_flow_top_n_async(
        self,
        request: nis_20211216_models.GetTransitRouterFlowTopNRequest,
    ) -> nis_20211216_models.GetTransitRouterFlowTopNResponse:
        """
        @summary Queries the rankings of inter-region traffic data in the form of 1-tuple, 2-tuple, or 5-tuple. Inter-region traffic data can be ranked by metrics such as traffic volumes and the number of packets.
        
        @param request: GetTransitRouterFlowTopNRequest
        @return: GetTransitRouterFlowTopNResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_transit_router_flow_top_nwith_options_async(request, runtime)

    def get_vbr_flow_top_nwith_options(
        self,
        tmp_req: nis_20211216_models.GetVbrFlowTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.GetVbrFlowTopNResponse:
        """
        @summary Queries the rankings of hybrid cloud traffic data in the form of 1-tuple, 2-tuple, or 5-tuple. Hybrid cloud traffic data can be ranked by metrics such as traffic volumes and the number of packets.
        
        @param tmp_req: GetVbrFlowTopNRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVbrFlowTopNResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nis_20211216_models.GetVbrFlowTopNShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.attachment_id):
            query['AttachmentId'] = request.attachment_id
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cloud_ip):
            query['CloudIp'] = request.cloud_ip
        if not UtilClient.is_unset(request.cloud_port):
            query['CloudPort'] = request.cloud_port
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.other_ip):
            query['OtherIp'] = request.other_ip
        if not UtilClient.is_unset(request.other_port):
            query['OtherPort'] = request.other_port
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.top_n):
            query['TopN'] = request.top_n
        if not UtilClient.is_unset(request.use_multi_account):
            query['UseMultiAccount'] = request.use_multi_account
        if not UtilClient.is_unset(request.virtual_border_router_id):
            query['VirtualBorderRouterId'] = request.virtual_border_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVbrFlowTopN',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.GetVbrFlowTopNResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_vbr_flow_top_nwith_options_async(
        self,
        tmp_req: nis_20211216_models.GetVbrFlowTopNRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nis_20211216_models.GetVbrFlowTopNResponse:
        """
        @summary Queries the rankings of hybrid cloud traffic data in the form of 1-tuple, 2-tuple, or 5-tuple. Hybrid cloud traffic data can be ranked by metrics such as traffic volumes and the number of packets.
        
        @param tmp_req: GetVbrFlowTopNRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVbrFlowTopNResponse
        """
        UtilClient.validate_model(tmp_req)
        request = nis_20211216_models.GetVbrFlowTopNShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.attachment_id):
            query['AttachmentId'] = request.attachment_id
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.cen_id):
            query['CenId'] = request.cen_id
        if not UtilClient.is_unset(request.cloud_ip):
            query['CloudIp'] = request.cloud_ip
        if not UtilClient.is_unset(request.cloud_port):
            query['CloudPort'] = request.cloud_port
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.other_ip):
            query['OtherIp'] = request.other_ip
        if not UtilClient.is_unset(request.other_port):
            query['OtherPort'] = request.other_port
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.top_n):
            query['TopN'] = request.top_n
        if not UtilClient.is_unset(request.use_multi_account):
            query['UseMultiAccount'] = request.use_multi_account
        if not UtilClient.is_unset(request.virtual_border_router_id):
            query['VirtualBorderRouterId'] = request.virtual_border_router_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVbrFlowTopN',
            version='2021-12-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nis_20211216_models.GetVbrFlowTopNResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_vbr_flow_top_n(
        self,
        request: nis_20211216_models.GetVbrFlowTopNRequest,
    ) -> nis_20211216_models.GetVbrFlowTopNResponse:
        """
        @summary Queries the rankings of hybrid cloud traffic data in the form of 1-tuple, 2-tuple, or 5-tuple. Hybrid cloud traffic data can be ranked by metrics such as traffic volumes and the number of packets.
        
        @param request: GetVbrFlowTopNRequest
        @return: GetVbrFlowTopNResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_vbr_flow_top_nwith_options(request, runtime)

    async def get_vbr_flow_top_n_async(
        self,
        request: nis_20211216_models.GetVbrFlowTopNRequest,
    ) -> nis_20211216_models.GetVbrFlowTopNResponse:
        """
        @summary Queries the rankings of hybrid cloud traffic data in the form of 1-tuple, 2-tuple, or 5-tuple. Hybrid cloud traffic data can be ranked by metrics such as traffic volumes and the number of packets.
        
        @param request: GetVbrFlowTopNRequest
        @return: GetVbrFlowTopNResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_vbr_flow_top_nwith_options_async(request, runtime)
