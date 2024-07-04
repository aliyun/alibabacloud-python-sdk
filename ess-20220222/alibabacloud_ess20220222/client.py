# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ess20220222 import models as ess_20220222_models
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
            'cn-qingdao': 'ess.aliyuncs.com',
            'cn-beijing': 'ess.aliyuncs.com',
            'cn-hangzhou': 'ess.aliyuncs.com',
            'cn-shanghai': 'ess.aliyuncs.com',
            'cn-shenzhen': 'ess.aliyuncs.com',
            'cn-hongkong': 'ess.aliyuncs.com',
            'ap-southeast-1': 'ess.aliyuncs.com',
            'us-east-1': 'ess.aliyuncs.com',
            'us-west-1': 'ess.aliyuncs.com',
            'cn-shanghai-finance-1': 'ess.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ess.aliyuncs.com',
            'cn-north-2-gov-1': 'ess.aliyuncs.com',
            'ap-northeast-2-pop': 'ess.aliyuncs.com',
            'cn-beijing-finance-pop': 'ess.aliyuncs.com',
            'cn-beijing-gov-1': 'ess.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ess.aliyuncs.com',
            'cn-edge-1': 'ess.aliyuncs.com',
            'cn-fujian': 'ess.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ess.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ess.aliyuncs.com',
            'cn-hangzhou-finance': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ess.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ess.aliyuncs.com',
            'cn-hangzhou-test-306': 'ess.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ess.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'ess.aliyuncs.com',
            'cn-qingdao-nebula': 'ess.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ess.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ess.aliyuncs.com',
            'cn-shanghai-inner': 'ess.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ess.aliyuncs.com',
            'cn-shenzhen-inner': 'ess.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ess.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ess.aliyuncs.com',
            'cn-wuhan': 'ess.aliyuncs.com',
            'cn-yushanfang': 'ess.aliyuncs.com',
            'cn-zhangbei': 'ess.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ess.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ess.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ess.aliyuncs.com',
            'eu-west-1-oxs': 'ess.aliyuncs.com',
            'rus-west-1-pop': 'ess.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ess', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def apply_eci_scaling_configuration_with_options(
        self,
        request: ess_20220222_models.ApplyEciScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ApplyEciScalingConfigurationResponse:
        """
        @summary Applies a scaling configuration of the Elastic Container Instance type. If you want to create and manage scaling configurations of the Elastic Container Instance type by using a configuration file, you can call the ApplyEciScalingConfiguration operation.
        
        @description Before you use a YAML configuration file to manage scaling configurations of the Elastic Container Instance type, you must take note of the following items:
        If you include a scaling configuration ID within your request, the system updates the scaling configuration based on the YAML configuration file.
        If you do not include a scaling configuration ID within your request, the system creates a scaling configuration of the Elastic Container Instance type based on the YAML configuration file.
        
        @param request: ApplyEciScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.format):
            query['Format'] = request.format
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ApplyEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_eci_scaling_configuration_with_options_async(
        self,
        request: ess_20220222_models.ApplyEciScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ApplyEciScalingConfigurationResponse:
        """
        @summary Applies a scaling configuration of the Elastic Container Instance type. If you want to create and manage scaling configurations of the Elastic Container Instance type by using a configuration file, you can call the ApplyEciScalingConfiguration operation.
        
        @description Before you use a YAML configuration file to manage scaling configurations of the Elastic Container Instance type, you must take note of the following items:
        If you include a scaling configuration ID within your request, the system updates the scaling configuration based on the YAML configuration file.
        If you do not include a scaling configuration ID within your request, the system creates a scaling configuration of the Elastic Container Instance type based on the YAML configuration file.
        
        @param request: ApplyEciScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.format):
            query['Format'] = request.format
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ApplyEciScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_eci_scaling_configuration(
        self,
        request: ess_20220222_models.ApplyEciScalingConfigurationRequest,
    ) -> ess_20220222_models.ApplyEciScalingConfigurationResponse:
        """
        @summary Applies a scaling configuration of the Elastic Container Instance type. If you want to create and manage scaling configurations of the Elastic Container Instance type by using a configuration file, you can call the ApplyEciScalingConfiguration operation.
        
        @description Before you use a YAML configuration file to manage scaling configurations of the Elastic Container Instance type, you must take note of the following items:
        If you include a scaling configuration ID within your request, the system updates the scaling configuration based on the YAML configuration file.
        If you do not include a scaling configuration ID within your request, the system creates a scaling configuration of the Elastic Container Instance type based on the YAML configuration file.
        
        @param request: ApplyEciScalingConfigurationRequest
        @return: ApplyEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_eci_scaling_configuration_with_options(request, runtime)

    async def apply_eci_scaling_configuration_async(
        self,
        request: ess_20220222_models.ApplyEciScalingConfigurationRequest,
    ) -> ess_20220222_models.ApplyEciScalingConfigurationResponse:
        """
        @summary Applies a scaling configuration of the Elastic Container Instance type. If you want to create and manage scaling configurations of the Elastic Container Instance type by using a configuration file, you can call the ApplyEciScalingConfiguration operation.
        
        @description Before you use a YAML configuration file to manage scaling configurations of the Elastic Container Instance type, you must take note of the following items:
        If you include a scaling configuration ID within your request, the system updates the scaling configuration based on the YAML configuration file.
        If you do not include a scaling configuration ID within your request, the system creates a scaling configuration of the Elastic Container Instance type based on the YAML configuration file.
        
        @param request: ApplyEciScalingConfigurationRequest
        @return: ApplyEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_eci_scaling_configuration_with_options_async(request, runtime)

    def apply_scaling_group_with_options(
        self,
        request: ess_20220222_models.ApplyScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ApplyScalingGroupResponse:
        """
        @summary 基于yaml配置进行弹性伸缩管理
        
        @description You can call the ApplyScalingGroup operation to create scaling groups of the Elastic Container Instance type with ease. The resources of the scaling groups are defined in Kubernetes Deployment YAML files. You can also call this operation to extend annotations for elastic container instances in Kubernetes Deployment YAML files. For more information, see "Supported annotations" in this topic.
        Mapping between YAML files and scaling groups: You can map the triplet of namespace, kind, and name in a YAML file to a scaling group name. A YAML file and a scaling group have a one-to-one mapping relationship in a region. For example, if you use the Kubernetes Deployment YAML file whose name is NGINX in the default namespace to create a scaling group in a region, the unique name of the mapped scaling group is k8s_default_Deployment_nginx.
        You can use a Kubernetes Deployment YAML file to manage a scaling group based on the following logic:
        If an existing scaling group has a mapping relationship with your Kubernetes Deployment YAML file, you can update the scaling group by using the YAML file.
        If no scaling group that has a mapping relationship with your Kubernetes Deployment YAML file exists, you can create a scaling group with ease by using the YAML file.
        ### Precautions
        1. If you do not specify a virtual private cloud (VPC), vSwitch, security group, or annotation in your Kubernetes Deployment YAML file, the system creates a default VPC that has default vSwitches and uses the default security group ess-default-sg of Auto Scaling. By default, the security group rule allows traffic on Transmission Control Protocol (TCP)-based port 22 and port 3389 and enables Internet Control Message Protocol (ICMP) for IPv4 addresses. If you want to enable other ports or protocols, you can create custom security group rules.
        2. If you want to use a public image, you must enable the Internet access feature and configure the k8s.aliyun.com/eci-with-eip pod annotation to enable the elastic IP address (EIP) feature.
        3. After you call the ApplyScalingGroup operation to apply a Kubernetes Deployment YAML file, the scaling group immediately enters the Enabled state and the scaling configuration immediately enters the Active state. If the number of replicas that you specified in the YAML file is grater than 0, elastic container instances are automatically created.
        ### Supported annotations
        For more information about annotations, see [ECI Pod Annotation](https://help.aliyun.com/document_detail/186939.html).
        |Annotation|Example|Description|
        |---|---|---|
        |k8s.aliyun.com/ess-scaling-group-min-size|1|The minimum size of the scaling group that you want to create. Default value: 0.|
        |k8s.aliyun.com/ess-scaling-group-max-size|20|The maximum size of the scaling group that you want to create. Default value: maximum number of replicas or 30, whichever is greater.|
        |k8s.aliyun.com/eci-ntp-server|100.100..*|The IP address of the Network Time Protocol (NTP) server.|
        |k8s.aliyun.com/eci-use-specs|2-4Gi|The specifications of 2 vCPUs and 4 GB memory. For more information, see [Create pods by specifying multiple specifications](https://help.aliyun.com/document_detail/451267.html).|
        |k8s.aliyun.com/eci-vswitch|vsw-bp1xpiowfm5vo8o3c\\\\*\\*\\*|The ID of the vSwitch. You can specify multiple vSwitches to specify multiple zones.|
        |k8s.aliyun.com/eci-security-group|sg-bp1dktddjsg5nktv\\\\*\\*\\*|The ID of the security group. Before you configure this annotation, take note of the following requirements:<ul data-sourcepos="26:74-26:168"><li data-sourcepos="26:78-26:114">You can specify one or more security groups. You can specify up to five security groups for each scaling group.</li><li data-sourcepos="26:114-26:140">If you specify multiple security groups, the security groups must belong to the same VPC.</li><li data-sourcepos="26:140-26:163">If you specify multiple security groups, the security groups must be of the same type.</li></ul>|
        |k8s.aliyun.com/eci-sls-enable|"false"|If you set the value to false, the log collection feature is disabled.
        If you do not want to use Custom Resource Definition (CRD) for Simple Log Service to collect logs of specific pods, you can configure this annotation for the pods and set the value to false. This prevents resource wastes caused by Logtails created by the system.|
        |k8s.aliyun.com/eci-spot-strategy|SpotAsPriceGo|The bidding policy for the preemptible instance. Valid values:<ul data-sourcepos="28:69-28:204"><li data-sourcepos="28:73-28:158">SpotWithPriceLimit: The instance is created as a preemptible instance for which you specify the maximum hourly price If you set the value to SpotWithPriceLimit, you must configure the k8s.aliyun.com/eci-spot-price-limit annotation.</li><li data-sourcepos="28:158-28:199">SpotAsPriceGo: The instance is a preemptible instance for which the market price at the time of purchase is used as the bid price.</li></ul>|
        |k8s.aliyun.com/eci-spot-price-limit|"0.5"|The maximum hourly price of the preemptible instance. This value can be accurate to up to three decimal places.
        This annotation takes effect only when you set the k8s.aliyun.com/eci-spot-strategy annotation to SpotWithPriceLimit.|
        |k8s.aliyun.com/eci-with-eip|"true"|If you set the value to true, an EIP is automatically created and bound to each elastic container instance.|
        |k8s.aliyun.com/eci-data-cache-bucket|default|The bucket of the specified DataCache. If you want to use a DataCache to create a pod, you must configure this annotation.|
        |k8s.aliyun.com/eci-data-cache-pl|PL1|The performance level (PL) of the cloud disk that you want to create by using the specified DataCache.
        By default, enhanced SSDs (ESSDs) are created. Default value: PL1.|
        |k8s.aliyun.com/eci-data-cache-provisionedIops|"40000"|The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50000, 1000 × Capacity - Baseline IOPS}. Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        If you configure this annotation, the cloud disk that is created by using the specified DataCache is of the ESSD AutoPL type.|
        |k8s.aliyun.com/eci-data-cache-burstingEnabled|"true"|Specifies whether the Burst feature is enabled for the ESSD AutoPL disk. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        If you configure this annotation, the cloud disk that is created by using the specified DataCache is of the ESSD AutoPL type.|
        |k8s.aliyun.com/eci-custom-tags|"env:test,name:alice"|The tags that you want to add to each elastic container instance. You can add up to three tags for each elastic container instance. Separate a tag key and a tag value with a colon (:). Separate multiple tags with commas (,).|
        
        @param request: ApplyScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.format):
            query['Format'] = request.format
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ApplyScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_scaling_group_with_options_async(
        self,
        request: ess_20220222_models.ApplyScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ApplyScalingGroupResponse:
        """
        @summary 基于yaml配置进行弹性伸缩管理
        
        @description You can call the ApplyScalingGroup operation to create scaling groups of the Elastic Container Instance type with ease. The resources of the scaling groups are defined in Kubernetes Deployment YAML files. You can also call this operation to extend annotations for elastic container instances in Kubernetes Deployment YAML files. For more information, see "Supported annotations" in this topic.
        Mapping between YAML files and scaling groups: You can map the triplet of namespace, kind, and name in a YAML file to a scaling group name. A YAML file and a scaling group have a one-to-one mapping relationship in a region. For example, if you use the Kubernetes Deployment YAML file whose name is NGINX in the default namespace to create a scaling group in a region, the unique name of the mapped scaling group is k8s_default_Deployment_nginx.
        You can use a Kubernetes Deployment YAML file to manage a scaling group based on the following logic:
        If an existing scaling group has a mapping relationship with your Kubernetes Deployment YAML file, you can update the scaling group by using the YAML file.
        If no scaling group that has a mapping relationship with your Kubernetes Deployment YAML file exists, you can create a scaling group with ease by using the YAML file.
        ### Precautions
        1. If you do not specify a virtual private cloud (VPC), vSwitch, security group, or annotation in your Kubernetes Deployment YAML file, the system creates a default VPC that has default vSwitches and uses the default security group ess-default-sg of Auto Scaling. By default, the security group rule allows traffic on Transmission Control Protocol (TCP)-based port 22 and port 3389 and enables Internet Control Message Protocol (ICMP) for IPv4 addresses. If you want to enable other ports or protocols, you can create custom security group rules.
        2. If you want to use a public image, you must enable the Internet access feature and configure the k8s.aliyun.com/eci-with-eip pod annotation to enable the elastic IP address (EIP) feature.
        3. After you call the ApplyScalingGroup operation to apply a Kubernetes Deployment YAML file, the scaling group immediately enters the Enabled state and the scaling configuration immediately enters the Active state. If the number of replicas that you specified in the YAML file is grater than 0, elastic container instances are automatically created.
        ### Supported annotations
        For more information about annotations, see [ECI Pod Annotation](https://help.aliyun.com/document_detail/186939.html).
        |Annotation|Example|Description|
        |---|---|---|
        |k8s.aliyun.com/ess-scaling-group-min-size|1|The minimum size of the scaling group that you want to create. Default value: 0.|
        |k8s.aliyun.com/ess-scaling-group-max-size|20|The maximum size of the scaling group that you want to create. Default value: maximum number of replicas or 30, whichever is greater.|
        |k8s.aliyun.com/eci-ntp-server|100.100..*|The IP address of the Network Time Protocol (NTP) server.|
        |k8s.aliyun.com/eci-use-specs|2-4Gi|The specifications of 2 vCPUs and 4 GB memory. For more information, see [Create pods by specifying multiple specifications](https://help.aliyun.com/document_detail/451267.html).|
        |k8s.aliyun.com/eci-vswitch|vsw-bp1xpiowfm5vo8o3c\\\\*\\*\\*|The ID of the vSwitch. You can specify multiple vSwitches to specify multiple zones.|
        |k8s.aliyun.com/eci-security-group|sg-bp1dktddjsg5nktv\\\\*\\*\\*|The ID of the security group. Before you configure this annotation, take note of the following requirements:<ul data-sourcepos="26:74-26:168"><li data-sourcepos="26:78-26:114">You can specify one or more security groups. You can specify up to five security groups for each scaling group.</li><li data-sourcepos="26:114-26:140">If you specify multiple security groups, the security groups must belong to the same VPC.</li><li data-sourcepos="26:140-26:163">If you specify multiple security groups, the security groups must be of the same type.</li></ul>|
        |k8s.aliyun.com/eci-sls-enable|"false"|If you set the value to false, the log collection feature is disabled.
        If you do not want to use Custom Resource Definition (CRD) for Simple Log Service to collect logs of specific pods, you can configure this annotation for the pods and set the value to false. This prevents resource wastes caused by Logtails created by the system.|
        |k8s.aliyun.com/eci-spot-strategy|SpotAsPriceGo|The bidding policy for the preemptible instance. Valid values:<ul data-sourcepos="28:69-28:204"><li data-sourcepos="28:73-28:158">SpotWithPriceLimit: The instance is created as a preemptible instance for which you specify the maximum hourly price If you set the value to SpotWithPriceLimit, you must configure the k8s.aliyun.com/eci-spot-price-limit annotation.</li><li data-sourcepos="28:158-28:199">SpotAsPriceGo: The instance is a preemptible instance for which the market price at the time of purchase is used as the bid price.</li></ul>|
        |k8s.aliyun.com/eci-spot-price-limit|"0.5"|The maximum hourly price of the preemptible instance. This value can be accurate to up to three decimal places.
        This annotation takes effect only when you set the k8s.aliyun.com/eci-spot-strategy annotation to SpotWithPriceLimit.|
        |k8s.aliyun.com/eci-with-eip|"true"|If you set the value to true, an EIP is automatically created and bound to each elastic container instance.|
        |k8s.aliyun.com/eci-data-cache-bucket|default|The bucket of the specified DataCache. If you want to use a DataCache to create a pod, you must configure this annotation.|
        |k8s.aliyun.com/eci-data-cache-pl|PL1|The performance level (PL) of the cloud disk that you want to create by using the specified DataCache.
        By default, enhanced SSDs (ESSDs) are created. Default value: PL1.|
        |k8s.aliyun.com/eci-data-cache-provisionedIops|"40000"|The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50000, 1000 × Capacity - Baseline IOPS}. Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        If you configure this annotation, the cloud disk that is created by using the specified DataCache is of the ESSD AutoPL type.|
        |k8s.aliyun.com/eci-data-cache-burstingEnabled|"true"|Specifies whether the Burst feature is enabled for the ESSD AutoPL disk. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        If you configure this annotation, the cloud disk that is created by using the specified DataCache is of the ESSD AutoPL type.|
        |k8s.aliyun.com/eci-custom-tags|"env:test,name:alice"|The tags that you want to add to each elastic container instance. You can add up to three tags for each elastic container instance. Separate a tag key and a tag value with a colon (:). Separate multiple tags with commas (,).|
        
        @param request: ApplyScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.format):
            query['Format'] = request.format
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ApplyScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_scaling_group(
        self,
        request: ess_20220222_models.ApplyScalingGroupRequest,
    ) -> ess_20220222_models.ApplyScalingGroupResponse:
        """
        @summary 基于yaml配置进行弹性伸缩管理
        
        @description You can call the ApplyScalingGroup operation to create scaling groups of the Elastic Container Instance type with ease. The resources of the scaling groups are defined in Kubernetes Deployment YAML files. You can also call this operation to extend annotations for elastic container instances in Kubernetes Deployment YAML files. For more information, see "Supported annotations" in this topic.
        Mapping between YAML files and scaling groups: You can map the triplet of namespace, kind, and name in a YAML file to a scaling group name. A YAML file and a scaling group have a one-to-one mapping relationship in a region. For example, if you use the Kubernetes Deployment YAML file whose name is NGINX in the default namespace to create a scaling group in a region, the unique name of the mapped scaling group is k8s_default_Deployment_nginx.
        You can use a Kubernetes Deployment YAML file to manage a scaling group based on the following logic:
        If an existing scaling group has a mapping relationship with your Kubernetes Deployment YAML file, you can update the scaling group by using the YAML file.
        If no scaling group that has a mapping relationship with your Kubernetes Deployment YAML file exists, you can create a scaling group with ease by using the YAML file.
        ### Precautions
        1. If you do not specify a virtual private cloud (VPC), vSwitch, security group, or annotation in your Kubernetes Deployment YAML file, the system creates a default VPC that has default vSwitches and uses the default security group ess-default-sg of Auto Scaling. By default, the security group rule allows traffic on Transmission Control Protocol (TCP)-based port 22 and port 3389 and enables Internet Control Message Protocol (ICMP) for IPv4 addresses. If you want to enable other ports or protocols, you can create custom security group rules.
        2. If you want to use a public image, you must enable the Internet access feature and configure the k8s.aliyun.com/eci-with-eip pod annotation to enable the elastic IP address (EIP) feature.
        3. After you call the ApplyScalingGroup operation to apply a Kubernetes Deployment YAML file, the scaling group immediately enters the Enabled state and the scaling configuration immediately enters the Active state. If the number of replicas that you specified in the YAML file is grater than 0, elastic container instances are automatically created.
        ### Supported annotations
        For more information about annotations, see [ECI Pod Annotation](https://help.aliyun.com/document_detail/186939.html).
        |Annotation|Example|Description|
        |---|---|---|
        |k8s.aliyun.com/ess-scaling-group-min-size|1|The minimum size of the scaling group that you want to create. Default value: 0.|
        |k8s.aliyun.com/ess-scaling-group-max-size|20|The maximum size of the scaling group that you want to create. Default value: maximum number of replicas or 30, whichever is greater.|
        |k8s.aliyun.com/eci-ntp-server|100.100..*|The IP address of the Network Time Protocol (NTP) server.|
        |k8s.aliyun.com/eci-use-specs|2-4Gi|The specifications of 2 vCPUs and 4 GB memory. For more information, see [Create pods by specifying multiple specifications](https://help.aliyun.com/document_detail/451267.html).|
        |k8s.aliyun.com/eci-vswitch|vsw-bp1xpiowfm5vo8o3c\\\\*\\*\\*|The ID of the vSwitch. You can specify multiple vSwitches to specify multiple zones.|
        |k8s.aliyun.com/eci-security-group|sg-bp1dktddjsg5nktv\\\\*\\*\\*|The ID of the security group. Before you configure this annotation, take note of the following requirements:<ul data-sourcepos="26:74-26:168"><li data-sourcepos="26:78-26:114">You can specify one or more security groups. You can specify up to five security groups for each scaling group.</li><li data-sourcepos="26:114-26:140">If you specify multiple security groups, the security groups must belong to the same VPC.</li><li data-sourcepos="26:140-26:163">If you specify multiple security groups, the security groups must be of the same type.</li></ul>|
        |k8s.aliyun.com/eci-sls-enable|"false"|If you set the value to false, the log collection feature is disabled.
        If you do not want to use Custom Resource Definition (CRD) for Simple Log Service to collect logs of specific pods, you can configure this annotation for the pods and set the value to false. This prevents resource wastes caused by Logtails created by the system.|
        |k8s.aliyun.com/eci-spot-strategy|SpotAsPriceGo|The bidding policy for the preemptible instance. Valid values:<ul data-sourcepos="28:69-28:204"><li data-sourcepos="28:73-28:158">SpotWithPriceLimit: The instance is created as a preemptible instance for which you specify the maximum hourly price If you set the value to SpotWithPriceLimit, you must configure the k8s.aliyun.com/eci-spot-price-limit annotation.</li><li data-sourcepos="28:158-28:199">SpotAsPriceGo: The instance is a preemptible instance for which the market price at the time of purchase is used as the bid price.</li></ul>|
        |k8s.aliyun.com/eci-spot-price-limit|"0.5"|The maximum hourly price of the preemptible instance. This value can be accurate to up to three decimal places.
        This annotation takes effect only when you set the k8s.aliyun.com/eci-spot-strategy annotation to SpotWithPriceLimit.|
        |k8s.aliyun.com/eci-with-eip|"true"|If you set the value to true, an EIP is automatically created and bound to each elastic container instance.|
        |k8s.aliyun.com/eci-data-cache-bucket|default|The bucket of the specified DataCache. If you want to use a DataCache to create a pod, you must configure this annotation.|
        |k8s.aliyun.com/eci-data-cache-pl|PL1|The performance level (PL) of the cloud disk that you want to create by using the specified DataCache.
        By default, enhanced SSDs (ESSDs) are created. Default value: PL1.|
        |k8s.aliyun.com/eci-data-cache-provisionedIops|"40000"|The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50000, 1000 × Capacity - Baseline IOPS}. Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        If you configure this annotation, the cloud disk that is created by using the specified DataCache is of the ESSD AutoPL type.|
        |k8s.aliyun.com/eci-data-cache-burstingEnabled|"true"|Specifies whether the Burst feature is enabled for the ESSD AutoPL disk. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        If you configure this annotation, the cloud disk that is created by using the specified DataCache is of the ESSD AutoPL type.|
        |k8s.aliyun.com/eci-custom-tags|"env:test,name:alice"|The tags that you want to add to each elastic container instance. You can add up to three tags for each elastic container instance. Separate a tag key and a tag value with a colon (:). Separate multiple tags with commas (,).|
        
        @param request: ApplyScalingGroupRequest
        @return: ApplyScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_scaling_group_with_options(request, runtime)

    async def apply_scaling_group_async(
        self,
        request: ess_20220222_models.ApplyScalingGroupRequest,
    ) -> ess_20220222_models.ApplyScalingGroupResponse:
        """
        @summary 基于yaml配置进行弹性伸缩管理
        
        @description You can call the ApplyScalingGroup operation to create scaling groups of the Elastic Container Instance type with ease. The resources of the scaling groups are defined in Kubernetes Deployment YAML files. You can also call this operation to extend annotations for elastic container instances in Kubernetes Deployment YAML files. For more information, see "Supported annotations" in this topic.
        Mapping between YAML files and scaling groups: You can map the triplet of namespace, kind, and name in a YAML file to a scaling group name. A YAML file and a scaling group have a one-to-one mapping relationship in a region. For example, if you use the Kubernetes Deployment YAML file whose name is NGINX in the default namespace to create a scaling group in a region, the unique name of the mapped scaling group is k8s_default_Deployment_nginx.
        You can use a Kubernetes Deployment YAML file to manage a scaling group based on the following logic:
        If an existing scaling group has a mapping relationship with your Kubernetes Deployment YAML file, you can update the scaling group by using the YAML file.
        If no scaling group that has a mapping relationship with your Kubernetes Deployment YAML file exists, you can create a scaling group with ease by using the YAML file.
        ### Precautions
        1. If you do not specify a virtual private cloud (VPC), vSwitch, security group, or annotation in your Kubernetes Deployment YAML file, the system creates a default VPC that has default vSwitches and uses the default security group ess-default-sg of Auto Scaling. By default, the security group rule allows traffic on Transmission Control Protocol (TCP)-based port 22 and port 3389 and enables Internet Control Message Protocol (ICMP) for IPv4 addresses. If you want to enable other ports or protocols, you can create custom security group rules.
        2. If you want to use a public image, you must enable the Internet access feature and configure the k8s.aliyun.com/eci-with-eip pod annotation to enable the elastic IP address (EIP) feature.
        3. After you call the ApplyScalingGroup operation to apply a Kubernetes Deployment YAML file, the scaling group immediately enters the Enabled state and the scaling configuration immediately enters the Active state. If the number of replicas that you specified in the YAML file is grater than 0, elastic container instances are automatically created.
        ### Supported annotations
        For more information about annotations, see [ECI Pod Annotation](https://help.aliyun.com/document_detail/186939.html).
        |Annotation|Example|Description|
        |---|---|---|
        |k8s.aliyun.com/ess-scaling-group-min-size|1|The minimum size of the scaling group that you want to create. Default value: 0.|
        |k8s.aliyun.com/ess-scaling-group-max-size|20|The maximum size of the scaling group that you want to create. Default value: maximum number of replicas or 30, whichever is greater.|
        |k8s.aliyun.com/eci-ntp-server|100.100..*|The IP address of the Network Time Protocol (NTP) server.|
        |k8s.aliyun.com/eci-use-specs|2-4Gi|The specifications of 2 vCPUs and 4 GB memory. For more information, see [Create pods by specifying multiple specifications](https://help.aliyun.com/document_detail/451267.html).|
        |k8s.aliyun.com/eci-vswitch|vsw-bp1xpiowfm5vo8o3c\\\\*\\*\\*|The ID of the vSwitch. You can specify multiple vSwitches to specify multiple zones.|
        |k8s.aliyun.com/eci-security-group|sg-bp1dktddjsg5nktv\\\\*\\*\\*|The ID of the security group. Before you configure this annotation, take note of the following requirements:<ul data-sourcepos="26:74-26:168"><li data-sourcepos="26:78-26:114">You can specify one or more security groups. You can specify up to five security groups for each scaling group.</li><li data-sourcepos="26:114-26:140">If you specify multiple security groups, the security groups must belong to the same VPC.</li><li data-sourcepos="26:140-26:163">If you specify multiple security groups, the security groups must be of the same type.</li></ul>|
        |k8s.aliyun.com/eci-sls-enable|"false"|If you set the value to false, the log collection feature is disabled.
        If you do not want to use Custom Resource Definition (CRD) for Simple Log Service to collect logs of specific pods, you can configure this annotation for the pods and set the value to false. This prevents resource wastes caused by Logtails created by the system.|
        |k8s.aliyun.com/eci-spot-strategy|SpotAsPriceGo|The bidding policy for the preemptible instance. Valid values:<ul data-sourcepos="28:69-28:204"><li data-sourcepos="28:73-28:158">SpotWithPriceLimit: The instance is created as a preemptible instance for which you specify the maximum hourly price If you set the value to SpotWithPriceLimit, you must configure the k8s.aliyun.com/eci-spot-price-limit annotation.</li><li data-sourcepos="28:158-28:199">SpotAsPriceGo: The instance is a preemptible instance for which the market price at the time of purchase is used as the bid price.</li></ul>|
        |k8s.aliyun.com/eci-spot-price-limit|"0.5"|The maximum hourly price of the preemptible instance. This value can be accurate to up to three decimal places.
        This annotation takes effect only when you set the k8s.aliyun.com/eci-spot-strategy annotation to SpotWithPriceLimit.|
        |k8s.aliyun.com/eci-with-eip|"true"|If you set the value to true, an EIP is automatically created and bound to each elastic container instance.|
        |k8s.aliyun.com/eci-data-cache-bucket|default|The bucket of the specified DataCache. If you want to use a DataCache to create a pod, you must configure this annotation.|
        |k8s.aliyun.com/eci-data-cache-pl|PL1|The performance level (PL) of the cloud disk that you want to create by using the specified DataCache.
        By default, enhanced SSDs (ESSDs) are created. Default value: PL1.|
        |k8s.aliyun.com/eci-data-cache-provisionedIops|"40000"|The provisioned read/write IOPS of the ESSD AutoPL disk. Valid values: 0 to min{50000, 1000 × Capacity - Baseline IOPS}. Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        If you configure this annotation, the cloud disk that is created by using the specified DataCache is of the ESSD AutoPL type.|
        |k8s.aliyun.com/eci-data-cache-burstingEnabled|"true"|Specifies whether the Burst feature is enabled for the ESSD AutoPL disk. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        If you configure this annotation, the cloud disk that is created by using the specified DataCache is of the ESSD AutoPL type.|
        |k8s.aliyun.com/eci-custom-tags|"env:test,name:alice"|The tags that you want to add to each elastic container instance. You can add up to three tags for each elastic container instance. Separate a tag key and a tag value with a colon (:). Separate multiple tags with commas (,).|
        
        @param request: ApplyScalingGroupRequest
        @return: ApplyScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_scaling_group_with_options_async(request, runtime)

    def attach_alb_server_groups_with_options(
        self,
        request: ess_20220222_models.AttachAlbServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachAlbServerGroupsResponse:
        """
        @summary Attaches Application Load Balancer (ALB) server groups to a scaling group. To seamlessly adjust the number of instances in response to changes in your business workload or to maintain the uninterrupted accessibility of your application, you can call the AttachAlbServerGroups operation. By attaching ALB server groups to your scaling group, this operation enables Auto Scaling to automatically tailor your computing capacity to your business needs. Furthermore, it optimizes traffic routing by dynamically allocating incoming requests based on current workload patterns, which significantly improves the stability and performance of your application.
        
        @description Before you call the operation to attach an ALB server group to your scaling group, make sure that the following requirements are met:
        The scaling group and the ALB server group share the same virtual private cloud (VPC).
        The ALB server group is in the Available state.
        
        @param request: AttachAlbServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachAlbServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachAlbServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachAlbServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_alb_server_groups_with_options_async(
        self,
        request: ess_20220222_models.AttachAlbServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachAlbServerGroupsResponse:
        """
        @summary Attaches Application Load Balancer (ALB) server groups to a scaling group. To seamlessly adjust the number of instances in response to changes in your business workload or to maintain the uninterrupted accessibility of your application, you can call the AttachAlbServerGroups operation. By attaching ALB server groups to your scaling group, this operation enables Auto Scaling to automatically tailor your computing capacity to your business needs. Furthermore, it optimizes traffic routing by dynamically allocating incoming requests based on current workload patterns, which significantly improves the stability and performance of your application.
        
        @description Before you call the operation to attach an ALB server group to your scaling group, make sure that the following requirements are met:
        The scaling group and the ALB server group share the same virtual private cloud (VPC).
        The ALB server group is in the Available state.
        
        @param request: AttachAlbServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachAlbServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachAlbServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachAlbServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_alb_server_groups(
        self,
        request: ess_20220222_models.AttachAlbServerGroupsRequest,
    ) -> ess_20220222_models.AttachAlbServerGroupsResponse:
        """
        @summary Attaches Application Load Balancer (ALB) server groups to a scaling group. To seamlessly adjust the number of instances in response to changes in your business workload or to maintain the uninterrupted accessibility of your application, you can call the AttachAlbServerGroups operation. By attaching ALB server groups to your scaling group, this operation enables Auto Scaling to automatically tailor your computing capacity to your business needs. Furthermore, it optimizes traffic routing by dynamically allocating incoming requests based on current workload patterns, which significantly improves the stability and performance of your application.
        
        @description Before you call the operation to attach an ALB server group to your scaling group, make sure that the following requirements are met:
        The scaling group and the ALB server group share the same virtual private cloud (VPC).
        The ALB server group is in the Available state.
        
        @param request: AttachAlbServerGroupsRequest
        @return: AttachAlbServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_alb_server_groups_with_options(request, runtime)

    async def attach_alb_server_groups_async(
        self,
        request: ess_20220222_models.AttachAlbServerGroupsRequest,
    ) -> ess_20220222_models.AttachAlbServerGroupsResponse:
        """
        @summary Attaches Application Load Balancer (ALB) server groups to a scaling group. To seamlessly adjust the number of instances in response to changes in your business workload or to maintain the uninterrupted accessibility of your application, you can call the AttachAlbServerGroups operation. By attaching ALB server groups to your scaling group, this operation enables Auto Scaling to automatically tailor your computing capacity to your business needs. Furthermore, it optimizes traffic routing by dynamically allocating incoming requests based on current workload patterns, which significantly improves the stability and performance of your application.
        
        @description Before you call the operation to attach an ALB server group to your scaling group, make sure that the following requirements are met:
        The scaling group and the ALB server group share the same virtual private cloud (VPC).
        The ALB server group is in the Available state.
        
        @param request: AttachAlbServerGroupsRequest
        @return: AttachAlbServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_alb_server_groups_with_options_async(request, runtime)

    def attach_dbinstances_with_options(
        self,
        request: ess_20220222_models.AttachDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachDBInstancesResponse:
        """
        @summary Associates one or more ApsaraDB RDS instances with a scaling group.
        
        @description Before you associate an ApsaraDB RDS instance with a scaling group, make sure that the ApsaraDB RDS instance meets the following requirements:
        The ApsaraDB RDS instance and the scaling group must belong to the same Alibaba Cloud account.
        The ApsaraDB RDS instance must be unlocked. For more information about the lock policy, see [ApsaraDB RDS usage notes](https://help.aliyun.com/document_detail/41872.html).
        The ApsaraDB RDS instance must be in the Running state.
        After an ApsaraDB RDS instance is associated with the scaling group, the default IP address whitelist of the ApsaraDB RDS instance can contain no more than 1,000 IP addresses. For more information, see [Set the whitelist](https://help.aliyun.com/document_detail/43185.html).
        
        @param request: AttachDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_mode):
            query['AttachMode'] = request.attach_mode
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDBInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_dbinstances_with_options_async(
        self,
        request: ess_20220222_models.AttachDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachDBInstancesResponse:
        """
        @summary Associates one or more ApsaraDB RDS instances with a scaling group.
        
        @description Before you associate an ApsaraDB RDS instance with a scaling group, make sure that the ApsaraDB RDS instance meets the following requirements:
        The ApsaraDB RDS instance and the scaling group must belong to the same Alibaba Cloud account.
        The ApsaraDB RDS instance must be unlocked. For more information about the lock policy, see [ApsaraDB RDS usage notes](https://help.aliyun.com/document_detail/41872.html).
        The ApsaraDB RDS instance must be in the Running state.
        After an ApsaraDB RDS instance is associated with the scaling group, the default IP address whitelist of the ApsaraDB RDS instance can contain no more than 1,000 IP addresses. For more information, see [Set the whitelist](https://help.aliyun.com/document_detail/43185.html).
        
        @param request: AttachDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_mode):
            query['AttachMode'] = request.attach_mode
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDBInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_dbinstances(
        self,
        request: ess_20220222_models.AttachDBInstancesRequest,
    ) -> ess_20220222_models.AttachDBInstancesResponse:
        """
        @summary Associates one or more ApsaraDB RDS instances with a scaling group.
        
        @description Before you associate an ApsaraDB RDS instance with a scaling group, make sure that the ApsaraDB RDS instance meets the following requirements:
        The ApsaraDB RDS instance and the scaling group must belong to the same Alibaba Cloud account.
        The ApsaraDB RDS instance must be unlocked. For more information about the lock policy, see [ApsaraDB RDS usage notes](https://help.aliyun.com/document_detail/41872.html).
        The ApsaraDB RDS instance must be in the Running state.
        After an ApsaraDB RDS instance is associated with the scaling group, the default IP address whitelist of the ApsaraDB RDS instance can contain no more than 1,000 IP addresses. For more information, see [Set the whitelist](https://help.aliyun.com/document_detail/43185.html).
        
        @param request: AttachDBInstancesRequest
        @return: AttachDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_dbinstances_with_options(request, runtime)

    async def attach_dbinstances_async(
        self,
        request: ess_20220222_models.AttachDBInstancesRequest,
    ) -> ess_20220222_models.AttachDBInstancesResponse:
        """
        @summary Associates one or more ApsaraDB RDS instances with a scaling group.
        
        @description Before you associate an ApsaraDB RDS instance with a scaling group, make sure that the ApsaraDB RDS instance meets the following requirements:
        The ApsaraDB RDS instance and the scaling group must belong to the same Alibaba Cloud account.
        The ApsaraDB RDS instance must be unlocked. For more information about the lock policy, see [ApsaraDB RDS usage notes](https://help.aliyun.com/document_detail/41872.html).
        The ApsaraDB RDS instance must be in the Running state.
        After an ApsaraDB RDS instance is associated with the scaling group, the default IP address whitelist of the ApsaraDB RDS instance can contain no more than 1,000 IP addresses. For more information, see [Set the whitelist](https://help.aliyun.com/document_detail/43185.html).
        
        @param request: AttachDBInstancesRequest
        @return: AttachDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_dbinstances_with_options_async(request, runtime)

    def attach_instances_with_options(
        self,
        request: ess_20220222_models.AttachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachInstancesResponse:
        """
        @summary Adds instances to a scaling group to provide services or restarts Elastic Compute Service (ECS) instances stopped in Economical Mode to provide services. You can call the AttachInstances operation to add ECS instances, elastic container instances, or third-party instances managed by Alibaba Cloud to your scaling group to provide services. You can also call this operation to restart ECS instances stopped in Economical Mode in your scaling group to provide services.
        
        @description Before you call this operation, take note of the following items:
        The scaling group is in the Active state.
        No scaling activities in the scaling group are in progress.
        The ECS instances or the elastic container instances that you want to add to a scaling group must meet the following requirements:
        The instances reside in the same region as the scaling group.
        The instances must be in the Running state.
        The instances are not added to other scaling groups.
        The instances use the subscription or pay-as-you-go billing method, or are preemptible instances.
        If the VswitchID parameter is specified for a scaling group, the instances that are in the classic network or those that are not in the same virtual private cloud (VPC) as the specified vSwitch cannot be added to the scaling group.
        If the VswitchID parameter is not specified for a scaling group, the instances that are in VPCs cannot be added to the scaling group.
        If no scaling activities in the specified scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the ScalingActivityId parameter in the response.
        If the sum of the number of instances that you want to add and the number of existing instances in the scaling group is greater than the value of the MaxSize parameter, the call fails.
        Instances that are manually added by calling the AttachInstances operation are not associated with the active scaling configuration of the scaling group.
        
        @param request: AttachInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.entrusted):
            query['Entrusted'] = request.entrusted
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lifecycle_hook):
            query['LifecycleHook'] = request.lifecycle_hook
        if not UtilClient.is_unset(request.load_balancer_weights):
            query['LoadBalancerWeights'] = request.load_balancer_weights
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_instances_with_options_async(
        self,
        request: ess_20220222_models.AttachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachInstancesResponse:
        """
        @summary Adds instances to a scaling group to provide services or restarts Elastic Compute Service (ECS) instances stopped in Economical Mode to provide services. You can call the AttachInstances operation to add ECS instances, elastic container instances, or third-party instances managed by Alibaba Cloud to your scaling group to provide services. You can also call this operation to restart ECS instances stopped in Economical Mode in your scaling group to provide services.
        
        @description Before you call this operation, take note of the following items:
        The scaling group is in the Active state.
        No scaling activities in the scaling group are in progress.
        The ECS instances or the elastic container instances that you want to add to a scaling group must meet the following requirements:
        The instances reside in the same region as the scaling group.
        The instances must be in the Running state.
        The instances are not added to other scaling groups.
        The instances use the subscription or pay-as-you-go billing method, or are preemptible instances.
        If the VswitchID parameter is specified for a scaling group, the instances that are in the classic network or those that are not in the same virtual private cloud (VPC) as the specified vSwitch cannot be added to the scaling group.
        If the VswitchID parameter is not specified for a scaling group, the instances that are in VPCs cannot be added to the scaling group.
        If no scaling activities in the specified scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the ScalingActivityId parameter in the response.
        If the sum of the number of instances that you want to add and the number of existing instances in the scaling group is greater than the value of the MaxSize parameter, the call fails.
        Instances that are manually added by calling the AttachInstances operation are not associated with the active scaling configuration of the scaling group.
        
        @param request: AttachInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.entrusted):
            query['Entrusted'] = request.entrusted
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lifecycle_hook):
            query['LifecycleHook'] = request.lifecycle_hook
        if not UtilClient.is_unset(request.load_balancer_weights):
            query['LoadBalancerWeights'] = request.load_balancer_weights
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_instances(
        self,
        request: ess_20220222_models.AttachInstancesRequest,
    ) -> ess_20220222_models.AttachInstancesResponse:
        """
        @summary Adds instances to a scaling group to provide services or restarts Elastic Compute Service (ECS) instances stopped in Economical Mode to provide services. You can call the AttachInstances operation to add ECS instances, elastic container instances, or third-party instances managed by Alibaba Cloud to your scaling group to provide services. You can also call this operation to restart ECS instances stopped in Economical Mode in your scaling group to provide services.
        
        @description Before you call this operation, take note of the following items:
        The scaling group is in the Active state.
        No scaling activities in the scaling group are in progress.
        The ECS instances or the elastic container instances that you want to add to a scaling group must meet the following requirements:
        The instances reside in the same region as the scaling group.
        The instances must be in the Running state.
        The instances are not added to other scaling groups.
        The instances use the subscription or pay-as-you-go billing method, or are preemptible instances.
        If the VswitchID parameter is specified for a scaling group, the instances that are in the classic network or those that are not in the same virtual private cloud (VPC) as the specified vSwitch cannot be added to the scaling group.
        If the VswitchID parameter is not specified for a scaling group, the instances that are in VPCs cannot be added to the scaling group.
        If no scaling activities in the specified scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the ScalingActivityId parameter in the response.
        If the sum of the number of instances that you want to add and the number of existing instances in the scaling group is greater than the value of the MaxSize parameter, the call fails.
        Instances that are manually added by calling the AttachInstances operation are not associated with the active scaling configuration of the scaling group.
        
        @param request: AttachInstancesRequest
        @return: AttachInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_instances_with_options(request, runtime)

    async def attach_instances_async(
        self,
        request: ess_20220222_models.AttachInstancesRequest,
    ) -> ess_20220222_models.AttachInstancesResponse:
        """
        @summary Adds instances to a scaling group to provide services or restarts Elastic Compute Service (ECS) instances stopped in Economical Mode to provide services. You can call the AttachInstances operation to add ECS instances, elastic container instances, or third-party instances managed by Alibaba Cloud to your scaling group to provide services. You can also call this operation to restart ECS instances stopped in Economical Mode in your scaling group to provide services.
        
        @description Before you call this operation, take note of the following items:
        The scaling group is in the Active state.
        No scaling activities in the scaling group are in progress.
        The ECS instances or the elastic container instances that you want to add to a scaling group must meet the following requirements:
        The instances reside in the same region as the scaling group.
        The instances must be in the Running state.
        The instances are not added to other scaling groups.
        The instances use the subscription or pay-as-you-go billing method, or are preemptible instances.
        If the VswitchID parameter is specified for a scaling group, the instances that are in the classic network or those that are not in the same virtual private cloud (VPC) as the specified vSwitch cannot be added to the scaling group.
        If the VswitchID parameter is not specified for a scaling group, the instances that are in VPCs cannot be added to the scaling group.
        If no scaling activities in the specified scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the ScalingActivityId parameter in the response.
        If the sum of the number of instances that you want to add and the number of existing instances in the scaling group is greater than the value of the MaxSize parameter, the call fails.
        Instances that are manually added by calling the AttachInstances operation are not associated with the active scaling configuration of the scaling group.
        
        @param request: AttachInstancesRequest
        @return: AttachInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_instances_with_options_async(request, runtime)

    def attach_load_balancers_with_options(
        self,
        request: ess_20220222_models.AttachLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachLoadBalancersResponse:
        """
        @summary Attaches load balancers to a scaling group. Auto Scaling supports the attachment of load balancers to scaling groups. Load balancers help distribute the access traffic to the instances in scaling groups, which effectively improves the service performance of the scaling groups. You can call the AttachLoadBalancers operation to attach one or more load balancers to your scaling group.
        
        @description Before you call this operation, make sure that the following requirements are met:
        The load balancer and the scaling group belong to the same Alibaba Cloud account and region.
        The load balancer is in the `Running` state.
        At least one listener is configured for the load balancer, and the health check feature is enabled for the load balancer.
        If the network type of the load balancer and the scaling group is virtual private cloud (VPC), they use the same VPC.
        If the network type of the scaling group is VPC, and that of the load balancer is classic network and a backend server of the load balancer uses a VPC, the scaling group and the backend server use the same VPC.
        The attachment of load balancers ensures that the cumulative number of load balancers attached to the scaling group stays within the predefined maximum limit. For information about the load balancer quota, see [Limits](https://help.aliyun.com/document_detail/25863.html).
        
        @param request: AttachLoadBalancersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.load_balancer_configs):
            query['LoadBalancerConfigs'] = request.load_balancer_configs
        if not UtilClient.is_unset(request.load_balancers):
            query['LoadBalancers'] = request.load_balancers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachLoadBalancers',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_load_balancers_with_options_async(
        self,
        request: ess_20220222_models.AttachLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachLoadBalancersResponse:
        """
        @summary Attaches load balancers to a scaling group. Auto Scaling supports the attachment of load balancers to scaling groups. Load balancers help distribute the access traffic to the instances in scaling groups, which effectively improves the service performance of the scaling groups. You can call the AttachLoadBalancers operation to attach one or more load balancers to your scaling group.
        
        @description Before you call this operation, make sure that the following requirements are met:
        The load balancer and the scaling group belong to the same Alibaba Cloud account and region.
        The load balancer is in the `Running` state.
        At least one listener is configured for the load balancer, and the health check feature is enabled for the load balancer.
        If the network type of the load balancer and the scaling group is virtual private cloud (VPC), they use the same VPC.
        If the network type of the scaling group is VPC, and that of the load balancer is classic network and a backend server of the load balancer uses a VPC, the scaling group and the backend server use the same VPC.
        The attachment of load balancers ensures that the cumulative number of load balancers attached to the scaling group stays within the predefined maximum limit. For information about the load balancer quota, see [Limits](https://help.aliyun.com/document_detail/25863.html).
        
        @param request: AttachLoadBalancersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.load_balancer_configs):
            query['LoadBalancerConfigs'] = request.load_balancer_configs
        if not UtilClient.is_unset(request.load_balancers):
            query['LoadBalancers'] = request.load_balancers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachLoadBalancers',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_load_balancers(
        self,
        request: ess_20220222_models.AttachLoadBalancersRequest,
    ) -> ess_20220222_models.AttachLoadBalancersResponse:
        """
        @summary Attaches load balancers to a scaling group. Auto Scaling supports the attachment of load balancers to scaling groups. Load balancers help distribute the access traffic to the instances in scaling groups, which effectively improves the service performance of the scaling groups. You can call the AttachLoadBalancers operation to attach one or more load balancers to your scaling group.
        
        @description Before you call this operation, make sure that the following requirements are met:
        The load balancer and the scaling group belong to the same Alibaba Cloud account and region.
        The load balancer is in the `Running` state.
        At least one listener is configured for the load balancer, and the health check feature is enabled for the load balancer.
        If the network type of the load balancer and the scaling group is virtual private cloud (VPC), they use the same VPC.
        If the network type of the scaling group is VPC, and that of the load balancer is classic network and a backend server of the load balancer uses a VPC, the scaling group and the backend server use the same VPC.
        The attachment of load balancers ensures that the cumulative number of load balancers attached to the scaling group stays within the predefined maximum limit. For information about the load balancer quota, see [Limits](https://help.aliyun.com/document_detail/25863.html).
        
        @param request: AttachLoadBalancersRequest
        @return: AttachLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_load_balancers_with_options(request, runtime)

    async def attach_load_balancers_async(
        self,
        request: ess_20220222_models.AttachLoadBalancersRequest,
    ) -> ess_20220222_models.AttachLoadBalancersResponse:
        """
        @summary Attaches load balancers to a scaling group. Auto Scaling supports the attachment of load balancers to scaling groups. Load balancers help distribute the access traffic to the instances in scaling groups, which effectively improves the service performance of the scaling groups. You can call the AttachLoadBalancers operation to attach one or more load balancers to your scaling group.
        
        @description Before you call this operation, make sure that the following requirements are met:
        The load balancer and the scaling group belong to the same Alibaba Cloud account and region.
        The load balancer is in the `Running` state.
        At least one listener is configured for the load balancer, and the health check feature is enabled for the load balancer.
        If the network type of the load balancer and the scaling group is virtual private cloud (VPC), they use the same VPC.
        If the network type of the scaling group is VPC, and that of the load balancer is classic network and a backend server of the load balancer uses a VPC, the scaling group and the backend server use the same VPC.
        The attachment of load balancers ensures that the cumulative number of load balancers attached to the scaling group stays within the predefined maximum limit. For information about the load balancer quota, see [Limits](https://help.aliyun.com/document_detail/25863.html).
        
        @param request: AttachLoadBalancersRequest
        @return: AttachLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_load_balancers_with_options_async(request, runtime)

    def attach_server_groups_with_options(
        self,
        request: ess_20220222_models.AttachServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachServerGroupsResponse:
        """
        @summary Attaches server groups to a scaling group. To seamlessly adjust the number of instances in response to changes in your business workload or to maintain the uninterrupted accessibility of your application, you can call the AttachServerGroups operation. By attaching Application Load Balancer (ALB) or Network Load Balancer (NLB) server groups to your scaling group, this operation enables Auto Scaling to automatically tailor your computing capacity to your business needs. Furthermore, it optimizes traffic routing by dynamically allocating incoming requests based on current workload patterns, which significantly improves the stability and performance of your application.
        
        @param request: AttachServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_server_groups_with_options_async(
        self,
        request: ess_20220222_models.AttachServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachServerGroupsResponse:
        """
        @summary Attaches server groups to a scaling group. To seamlessly adjust the number of instances in response to changes in your business workload or to maintain the uninterrupted accessibility of your application, you can call the AttachServerGroups operation. By attaching Application Load Balancer (ALB) or Network Load Balancer (NLB) server groups to your scaling group, this operation enables Auto Scaling to automatically tailor your computing capacity to your business needs. Furthermore, it optimizes traffic routing by dynamically allocating incoming requests based on current workload patterns, which significantly improves the stability and performance of your application.
        
        @param request: AttachServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_server_groups(
        self,
        request: ess_20220222_models.AttachServerGroupsRequest,
    ) -> ess_20220222_models.AttachServerGroupsResponse:
        """
        @summary Attaches server groups to a scaling group. To seamlessly adjust the number of instances in response to changes in your business workload or to maintain the uninterrupted accessibility of your application, you can call the AttachServerGroups operation. By attaching Application Load Balancer (ALB) or Network Load Balancer (NLB) server groups to your scaling group, this operation enables Auto Scaling to automatically tailor your computing capacity to your business needs. Furthermore, it optimizes traffic routing by dynamically allocating incoming requests based on current workload patterns, which significantly improves the stability and performance of your application.
        
        @param request: AttachServerGroupsRequest
        @return: AttachServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_server_groups_with_options(request, runtime)

    async def attach_server_groups_async(
        self,
        request: ess_20220222_models.AttachServerGroupsRequest,
    ) -> ess_20220222_models.AttachServerGroupsResponse:
        """
        @summary Attaches server groups to a scaling group. To seamlessly adjust the number of instances in response to changes in your business workload or to maintain the uninterrupted accessibility of your application, you can call the AttachServerGroups operation. By attaching Application Load Balancer (ALB) or Network Load Balancer (NLB) server groups to your scaling group, this operation enables Auto Scaling to automatically tailor your computing capacity to your business needs. Furthermore, it optimizes traffic routing by dynamically allocating incoming requests based on current workload patterns, which significantly improves the stability and performance of your application.
        
        @param request: AttachServerGroupsRequest
        @return: AttachServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_server_groups_with_options_async(request, runtime)

    def attach_vserver_groups_with_options(
        self,
        request: ess_20220222_models.AttachVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachVServerGroupsResponse:
        """
        @summary Attaches vServer groups to a scaling group. After a Classic Load Balancer (CLB) instance is attached to your scaling group, the instances in the scaling group are automatically added as backend servers of the CLB instance. These servers then handle requests forwarded by the CLB instance, streamlining the processing of incoming traffic. To direct varying access requests to separate backend servers or to distribute requests based on domain names or URLs, you can call the AttachVServerGroups operation. This operation enables the addition of multiple vServer groups, allowing for efficient management of various backend server configurations tailored to your routing preferences.
        
        @description    Before you call this operation, make sure that the following requirements are met:
        The CLB instance and the scaling group belong to the same Alibaba Cloud account.
        The CLB instance and the scaling group reside in the same region.
        The CLB instance is in the Running state.
        The CLB instance is configured with at least one listener. The health check feature is enabled for the CLB instance.
        If the network type of both the CLB instance and the scaling group is virtual private cloud (VPC), they use the same VPC.
        If the network type of the scaling group is VPC and the network type of the CLB instance is classic network, any backend server of the CLB instance within a VPC setup shares the same VPC as the scaling group.
        The vServer groups that you want to attach to the scaling group belong to the CLB instance.
        The operation to attach vServer groups does not result in the total number of vServer groups exceeding the predefined quota limit. For information about the vServer group quota, see [Limits](https://help.aliyun.com/document_detail/25863.html).
        When you call this operation to attach vServer groups, you must specify the following parameters:
        LoadBalancerId: the ID of the CLB instance
        VServerGroupId: the ID of the vServer group
        Port: the port number of the vServer group
        *\
        *Note** If you attempt to attach the same vServer group to a scaling group multiple times over the identical port, the system regards each attempt as a separate vServer group attachment to the scaling group. In your request, if you include the same vServer group ID coupled with the same port number multiple times, only the first configuration of the vServer group and port number pairing is considered valid. Subsequent vServer group and port number parings are disregarded.
        
        @param request: AttachVServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachVServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachVServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachVServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_vserver_groups_with_options_async(
        self,
        request: ess_20220222_models.AttachVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.AttachVServerGroupsResponse:
        """
        @summary Attaches vServer groups to a scaling group. After a Classic Load Balancer (CLB) instance is attached to your scaling group, the instances in the scaling group are automatically added as backend servers of the CLB instance. These servers then handle requests forwarded by the CLB instance, streamlining the processing of incoming traffic. To direct varying access requests to separate backend servers or to distribute requests based on domain names or URLs, you can call the AttachVServerGroups operation. This operation enables the addition of multiple vServer groups, allowing for efficient management of various backend server configurations tailored to your routing preferences.
        
        @description    Before you call this operation, make sure that the following requirements are met:
        The CLB instance and the scaling group belong to the same Alibaba Cloud account.
        The CLB instance and the scaling group reside in the same region.
        The CLB instance is in the Running state.
        The CLB instance is configured with at least one listener. The health check feature is enabled for the CLB instance.
        If the network type of both the CLB instance and the scaling group is virtual private cloud (VPC), they use the same VPC.
        If the network type of the scaling group is VPC and the network type of the CLB instance is classic network, any backend server of the CLB instance within a VPC setup shares the same VPC as the scaling group.
        The vServer groups that you want to attach to the scaling group belong to the CLB instance.
        The operation to attach vServer groups does not result in the total number of vServer groups exceeding the predefined quota limit. For information about the vServer group quota, see [Limits](https://help.aliyun.com/document_detail/25863.html).
        When you call this operation to attach vServer groups, you must specify the following parameters:
        LoadBalancerId: the ID of the CLB instance
        VServerGroupId: the ID of the vServer group
        Port: the port number of the vServer group
        *\
        *Note** If you attempt to attach the same vServer group to a scaling group multiple times over the identical port, the system regards each attempt as a separate vServer group attachment to the scaling group. In your request, if you include the same vServer group ID coupled with the same port number multiple times, only the first configuration of the vServer group and port number pairing is considered valid. Subsequent vServer group and port number parings are disregarded.
        
        @param request: AttachVServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachVServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_attach):
            query['ForceAttach'] = request.force_attach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachVServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.AttachVServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_vserver_groups(
        self,
        request: ess_20220222_models.AttachVServerGroupsRequest,
    ) -> ess_20220222_models.AttachVServerGroupsResponse:
        """
        @summary Attaches vServer groups to a scaling group. After a Classic Load Balancer (CLB) instance is attached to your scaling group, the instances in the scaling group are automatically added as backend servers of the CLB instance. These servers then handle requests forwarded by the CLB instance, streamlining the processing of incoming traffic. To direct varying access requests to separate backend servers or to distribute requests based on domain names or URLs, you can call the AttachVServerGroups operation. This operation enables the addition of multiple vServer groups, allowing for efficient management of various backend server configurations tailored to your routing preferences.
        
        @description    Before you call this operation, make sure that the following requirements are met:
        The CLB instance and the scaling group belong to the same Alibaba Cloud account.
        The CLB instance and the scaling group reside in the same region.
        The CLB instance is in the Running state.
        The CLB instance is configured with at least one listener. The health check feature is enabled for the CLB instance.
        If the network type of both the CLB instance and the scaling group is virtual private cloud (VPC), they use the same VPC.
        If the network type of the scaling group is VPC and the network type of the CLB instance is classic network, any backend server of the CLB instance within a VPC setup shares the same VPC as the scaling group.
        The vServer groups that you want to attach to the scaling group belong to the CLB instance.
        The operation to attach vServer groups does not result in the total number of vServer groups exceeding the predefined quota limit. For information about the vServer group quota, see [Limits](https://help.aliyun.com/document_detail/25863.html).
        When you call this operation to attach vServer groups, you must specify the following parameters:
        LoadBalancerId: the ID of the CLB instance
        VServerGroupId: the ID of the vServer group
        Port: the port number of the vServer group
        *\
        *Note** If you attempt to attach the same vServer group to a scaling group multiple times over the identical port, the system regards each attempt as a separate vServer group attachment to the scaling group. In your request, if you include the same vServer group ID coupled with the same port number multiple times, only the first configuration of the vServer group and port number pairing is considered valid. Subsequent vServer group and port number parings are disregarded.
        
        @param request: AttachVServerGroupsRequest
        @return: AttachVServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_vserver_groups_with_options(request, runtime)

    async def attach_vserver_groups_async(
        self,
        request: ess_20220222_models.AttachVServerGroupsRequest,
    ) -> ess_20220222_models.AttachVServerGroupsResponse:
        """
        @summary Attaches vServer groups to a scaling group. After a Classic Load Balancer (CLB) instance is attached to your scaling group, the instances in the scaling group are automatically added as backend servers of the CLB instance. These servers then handle requests forwarded by the CLB instance, streamlining the processing of incoming traffic. To direct varying access requests to separate backend servers or to distribute requests based on domain names or URLs, you can call the AttachVServerGroups operation. This operation enables the addition of multiple vServer groups, allowing for efficient management of various backend server configurations tailored to your routing preferences.
        
        @description    Before you call this operation, make sure that the following requirements are met:
        The CLB instance and the scaling group belong to the same Alibaba Cloud account.
        The CLB instance and the scaling group reside in the same region.
        The CLB instance is in the Running state.
        The CLB instance is configured with at least one listener. The health check feature is enabled for the CLB instance.
        If the network type of both the CLB instance and the scaling group is virtual private cloud (VPC), they use the same VPC.
        If the network type of the scaling group is VPC and the network type of the CLB instance is classic network, any backend server of the CLB instance within a VPC setup shares the same VPC as the scaling group.
        The vServer groups that you want to attach to the scaling group belong to the CLB instance.
        The operation to attach vServer groups does not result in the total number of vServer groups exceeding the predefined quota limit. For information about the vServer group quota, see [Limits](https://help.aliyun.com/document_detail/25863.html).
        When you call this operation to attach vServer groups, you must specify the following parameters:
        LoadBalancerId: the ID of the CLB instance
        VServerGroupId: the ID of the vServer group
        Port: the port number of the vServer group
        *\
        *Note** If you attempt to attach the same vServer group to a scaling group multiple times over the identical port, the system regards each attempt as a separate vServer group attachment to the scaling group. In your request, if you include the same vServer group ID coupled with the same port number multiple times, only the first configuration of the vServer group and port number pairing is considered valid. Subsequent vServer group and port number parings are disregarded.
        
        @param request: AttachVServerGroupsRequest
        @return: AttachVServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_vserver_groups_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: ess_20220222_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ChangeResourceGroupResponse:
        """
        @summary Changes a resource group. Resource groups are a means to categorize and manage cloud resources, such as scaling groups, based on specific objectives, permissions, or ownership. In large, multifaceted organizations that manage numerous projects and users, this feature adopts a tiered management approach, simplifying management tasks and improving the effectiveness and oversight of resource allocation. You can call the ChangeResourceGroup operation to move your scaling groups from one resource group to another resource group, which facilitates streamlined monitoring and management within the context of the new group. This operation eliminates the need for repetitive and time-consuming cross-service resource queries, thereby enhancing operational efficiency.
        
        @description    A resource is an entity of cloud services that you create on Alibaba Cloud. For example, a scaling group is a resource.
        A resource group serves as a powerful organizational tool within your Alibaba Cloud account, enabling you to manage and monitor multiple resources collectively. It effectively addresses complexities surrounding resource categorization and permission control under a single Alibaba Cloud account, thereby enhancing management efficiency and control. For more information, see [What is resource management?](https://help.aliyun.com/document_detail/94475.html)
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: ess_20220222_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ChangeResourceGroupResponse:
        """
        @summary Changes a resource group. Resource groups are a means to categorize and manage cloud resources, such as scaling groups, based on specific objectives, permissions, or ownership. In large, multifaceted organizations that manage numerous projects and users, this feature adopts a tiered management approach, simplifying management tasks and improving the effectiveness and oversight of resource allocation. You can call the ChangeResourceGroup operation to move your scaling groups from one resource group to another resource group, which facilitates streamlined monitoring and management within the context of the new group. This operation eliminates the need for repetitive and time-consuming cross-service resource queries, thereby enhancing operational efficiency.
        
        @description    A resource is an entity of cloud services that you create on Alibaba Cloud. For example, a scaling group is a resource.
        A resource group serves as a powerful organizational tool within your Alibaba Cloud account, enabling you to manage and monitor multiple resources collectively. It effectively addresses complexities surrounding resource categorization and permission control under a single Alibaba Cloud account, thereby enhancing management efficiency and control. For more information, see [What is resource management?](https://help.aliyun.com/document_detail/94475.html)
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: ess_20220222_models.ChangeResourceGroupRequest,
    ) -> ess_20220222_models.ChangeResourceGroupResponse:
        """
        @summary Changes a resource group. Resource groups are a means to categorize and manage cloud resources, such as scaling groups, based on specific objectives, permissions, or ownership. In large, multifaceted organizations that manage numerous projects and users, this feature adopts a tiered management approach, simplifying management tasks and improving the effectiveness and oversight of resource allocation. You can call the ChangeResourceGroup operation to move your scaling groups from one resource group to another resource group, which facilitates streamlined monitoring and management within the context of the new group. This operation eliminates the need for repetitive and time-consuming cross-service resource queries, thereby enhancing operational efficiency.
        
        @description    A resource is an entity of cloud services that you create on Alibaba Cloud. For example, a scaling group is a resource.
        A resource group serves as a powerful organizational tool within your Alibaba Cloud account, enabling you to manage and monitor multiple resources collectively. It effectively addresses complexities surrounding resource categorization and permission control under a single Alibaba Cloud account, thereby enhancing management efficiency and control. For more information, see [What is resource management?](https://help.aliyun.com/document_detail/94475.html)
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: ess_20220222_models.ChangeResourceGroupRequest,
    ) -> ess_20220222_models.ChangeResourceGroupResponse:
        """
        @summary Changes a resource group. Resource groups are a means to categorize and manage cloud resources, such as scaling groups, based on specific objectives, permissions, or ownership. In large, multifaceted organizations that manage numerous projects and users, this feature adopts a tiered management approach, simplifying management tasks and improving the effectiveness and oversight of resource allocation. You can call the ChangeResourceGroup operation to move your scaling groups from one resource group to another resource group, which facilitates streamlined monitoring and management within the context of the new group. This operation eliminates the need for repetitive and time-consuming cross-service resource queries, thereby enhancing operational efficiency.
        
        @description    A resource is an entity of cloud services that you create on Alibaba Cloud. For example, a scaling group is a resource.
        A resource group serves as a powerful organizational tool within your Alibaba Cloud account, enabling you to manage and monitor multiple resources collectively. It effectively addresses complexities surrounding resource categorization and permission control under a single Alibaba Cloud account, thereby enhancing management efficiency and control. For more information, see [What is resource management?](https://help.aliyun.com/document_detail/94475.html)
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def complete_lifecycle_action_with_options(
        self,
        request: ess_20220222_models.CompleteLifecycleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CompleteLifecycleActionResponse:
        """
        @summary Ends the timeout period of a lifecycle hook ahead of schedule. If you have created a lifecycle hook for your scaling group, you can call the CompleteLifecycleAction operation to end the timeout period of the lifecycle hook ahead of schedule based on your business requirements.
        
        @description When you manually cut short the timeout period of a lifecycle hook, Auto Scaling proceeds with one of the following actions based on the predefined settings: responding to the scaling request, aborting the scaling request, and initiating a rollback process.
        
        @param request: CompleteLifecycleActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompleteLifecycleActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lifecycle_action_result):
            query['LifecycleActionResult'] = request.lifecycle_action_result
        if not UtilClient.is_unset(request.lifecycle_action_token):
            query['LifecycleActionToken'] = request.lifecycle_action_token
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteLifecycleAction',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CompleteLifecycleActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def complete_lifecycle_action_with_options_async(
        self,
        request: ess_20220222_models.CompleteLifecycleActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CompleteLifecycleActionResponse:
        """
        @summary Ends the timeout period of a lifecycle hook ahead of schedule. If you have created a lifecycle hook for your scaling group, you can call the CompleteLifecycleAction operation to end the timeout period of the lifecycle hook ahead of schedule based on your business requirements.
        
        @description When you manually cut short the timeout period of a lifecycle hook, Auto Scaling proceeds with one of the following actions based on the predefined settings: responding to the scaling request, aborting the scaling request, and initiating a rollback process.
        
        @param request: CompleteLifecycleActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompleteLifecycleActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lifecycle_action_result):
            query['LifecycleActionResult'] = request.lifecycle_action_result
        if not UtilClient.is_unset(request.lifecycle_action_token):
            query['LifecycleActionToken'] = request.lifecycle_action_token
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteLifecycleAction',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CompleteLifecycleActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def complete_lifecycle_action(
        self,
        request: ess_20220222_models.CompleteLifecycleActionRequest,
    ) -> ess_20220222_models.CompleteLifecycleActionResponse:
        """
        @summary Ends the timeout period of a lifecycle hook ahead of schedule. If you have created a lifecycle hook for your scaling group, you can call the CompleteLifecycleAction operation to end the timeout period of the lifecycle hook ahead of schedule based on your business requirements.
        
        @description When you manually cut short the timeout period of a lifecycle hook, Auto Scaling proceeds with one of the following actions based on the predefined settings: responding to the scaling request, aborting the scaling request, and initiating a rollback process.
        
        @param request: CompleteLifecycleActionRequest
        @return: CompleteLifecycleActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.complete_lifecycle_action_with_options(request, runtime)

    async def complete_lifecycle_action_async(
        self,
        request: ess_20220222_models.CompleteLifecycleActionRequest,
    ) -> ess_20220222_models.CompleteLifecycleActionResponse:
        """
        @summary Ends the timeout period of a lifecycle hook ahead of schedule. If you have created a lifecycle hook for your scaling group, you can call the CompleteLifecycleAction operation to end the timeout period of the lifecycle hook ahead of schedule based on your business requirements.
        
        @description When you manually cut short the timeout period of a lifecycle hook, Auto Scaling proceeds with one of the following actions based on the predefined settings: responding to the scaling request, aborting the scaling request, and initiating a rollback process.
        
        @param request: CompleteLifecycleActionRequest
        @return: CompleteLifecycleActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.complete_lifecycle_action_with_options_async(request, runtime)

    def create_alarm_with_options(
        self,
        request: ess_20220222_models.CreateAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateAlarmResponse:
        """
        @summary Creates event-triggered tasks. If your business encounters unexpected traffic surges or has no specific patterns, you can call the CreateAlarm operation to create an event-triggered task and associate a CloudMonitor metric with the task. This allows you to dynamically adjust the number of Elastic Compute Service (ECS) instances or elastic container instances in your scaling group and keep updated on the real-time metric data, which facilitates cloud resource management and maintenance.
        
        @description    If you set MetricType to custom, you must report your custom metrics to CloudMonitor before you can create event-triggered tasks by using the custom metrics. For more information, see [Event-triggered tasks of the custom monitoring type](https://help.aliyun.com/document_detail/74861.html).
        When you create an event-triggered task, you must specify MetricName, Dimensions.DimensionKey, and Dimensions.DimensionValue to determine the range of statistics that you want to aggregate for the metrics of the scaling group. For example, you can specify user_id and scaling_group for an event-triggered task to aggregate monitoring data of all ECS instances or elastic container instances in a scaling group within an Alibaba Cloud account.
        If you create an event-triggered task of the custom monitoring type, you can specify only custom metrics in the task.
        If you create an event-triggered task of the system monitoring type, you can specify the system metrics described in [Event-triggered tasks of the system monitoring type](https://help.aliyun.com/document_detail/74854.html) in the task.
        >  user_id and scaling_group are automatically populated. You need to only specify device and state. For more information, see `Dimensions.DimensionKey` and `Dimensions.DimensionValue` in the "Request parameters" section of this topic.
        
        @param request: CreateAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_actions):
            query['AlarmActions'] = request.alarm_actions
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective):
            query['Effective'] = request.effective
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.expressions):
            query['Expressions'] = request.expressions
        if not UtilClient.is_unset(request.expressions_logic_operator):
            query['ExpressionsLogicOperator'] = request.expressions_logic_operator
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.statistics):
            query['Statistics'] = request.statistics
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alarm_with_options_async(
        self,
        request: ess_20220222_models.CreateAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateAlarmResponse:
        """
        @summary Creates event-triggered tasks. If your business encounters unexpected traffic surges or has no specific patterns, you can call the CreateAlarm operation to create an event-triggered task and associate a CloudMonitor metric with the task. This allows you to dynamically adjust the number of Elastic Compute Service (ECS) instances or elastic container instances in your scaling group and keep updated on the real-time metric data, which facilitates cloud resource management and maintenance.
        
        @description    If you set MetricType to custom, you must report your custom metrics to CloudMonitor before you can create event-triggered tasks by using the custom metrics. For more information, see [Event-triggered tasks of the custom monitoring type](https://help.aliyun.com/document_detail/74861.html).
        When you create an event-triggered task, you must specify MetricName, Dimensions.DimensionKey, and Dimensions.DimensionValue to determine the range of statistics that you want to aggregate for the metrics of the scaling group. For example, you can specify user_id and scaling_group for an event-triggered task to aggregate monitoring data of all ECS instances or elastic container instances in a scaling group within an Alibaba Cloud account.
        If you create an event-triggered task of the custom monitoring type, you can specify only custom metrics in the task.
        If you create an event-triggered task of the system monitoring type, you can specify the system metrics described in [Event-triggered tasks of the system monitoring type](https://help.aliyun.com/document_detail/74854.html) in the task.
        >  user_id and scaling_group are automatically populated. You need to only specify device and state. For more information, see `Dimensions.DimensionKey` and `Dimensions.DimensionValue` in the "Request parameters" section of this topic.
        
        @param request: CreateAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_actions):
            query['AlarmActions'] = request.alarm_actions
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective):
            query['Effective'] = request.effective
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.expressions):
            query['Expressions'] = request.expressions
        if not UtilClient.is_unset(request.expressions_logic_operator):
            query['ExpressionsLogicOperator'] = request.expressions_logic_operator
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.statistics):
            query['Statistics'] = request.statistics
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alarm(
        self,
        request: ess_20220222_models.CreateAlarmRequest,
    ) -> ess_20220222_models.CreateAlarmResponse:
        """
        @summary Creates event-triggered tasks. If your business encounters unexpected traffic surges or has no specific patterns, you can call the CreateAlarm operation to create an event-triggered task and associate a CloudMonitor metric with the task. This allows you to dynamically adjust the number of Elastic Compute Service (ECS) instances or elastic container instances in your scaling group and keep updated on the real-time metric data, which facilitates cloud resource management and maintenance.
        
        @description    If you set MetricType to custom, you must report your custom metrics to CloudMonitor before you can create event-triggered tasks by using the custom metrics. For more information, see [Event-triggered tasks of the custom monitoring type](https://help.aliyun.com/document_detail/74861.html).
        When you create an event-triggered task, you must specify MetricName, Dimensions.DimensionKey, and Dimensions.DimensionValue to determine the range of statistics that you want to aggregate for the metrics of the scaling group. For example, you can specify user_id and scaling_group for an event-triggered task to aggregate monitoring data of all ECS instances or elastic container instances in a scaling group within an Alibaba Cloud account.
        If you create an event-triggered task of the custom monitoring type, you can specify only custom metrics in the task.
        If you create an event-triggered task of the system monitoring type, you can specify the system metrics described in [Event-triggered tasks of the system monitoring type](https://help.aliyun.com/document_detail/74854.html) in the task.
        >  user_id and scaling_group are automatically populated. You need to only specify device and state. For more information, see `Dimensions.DimensionKey` and `Dimensions.DimensionValue` in the "Request parameters" section of this topic.
        
        @param request: CreateAlarmRequest
        @return: CreateAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_alarm_with_options(request, runtime)

    async def create_alarm_async(
        self,
        request: ess_20220222_models.CreateAlarmRequest,
    ) -> ess_20220222_models.CreateAlarmResponse:
        """
        @summary Creates event-triggered tasks. If your business encounters unexpected traffic surges or has no specific patterns, you can call the CreateAlarm operation to create an event-triggered task and associate a CloudMonitor metric with the task. This allows you to dynamically adjust the number of Elastic Compute Service (ECS) instances or elastic container instances in your scaling group and keep updated on the real-time metric data, which facilitates cloud resource management and maintenance.
        
        @description    If you set MetricType to custom, you must report your custom metrics to CloudMonitor before you can create event-triggered tasks by using the custom metrics. For more information, see [Event-triggered tasks of the custom monitoring type](https://help.aliyun.com/document_detail/74861.html).
        When you create an event-triggered task, you must specify MetricName, Dimensions.DimensionKey, and Dimensions.DimensionValue to determine the range of statistics that you want to aggregate for the metrics of the scaling group. For example, you can specify user_id and scaling_group for an event-triggered task to aggregate monitoring data of all ECS instances or elastic container instances in a scaling group within an Alibaba Cloud account.
        If you create an event-triggered task of the custom monitoring type, you can specify only custom metrics in the task.
        If you create an event-triggered task of the system monitoring type, you can specify the system metrics described in [Event-triggered tasks of the system monitoring type](https://help.aliyun.com/document_detail/74854.html) in the task.
        >  user_id and scaling_group are automatically populated. You need to only specify device and state. For more information, see `Dimensions.DimensionKey` and `Dimensions.DimensionValue` in the "Request parameters" section of this topic.
        
        @param request: CreateAlarmRequest
        @return: CreateAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_alarm_with_options_async(request, runtime)

    def create_eci_scaling_configuration_with_options(
        self,
        request: ess_20220222_models.CreateEciScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateEciScalingConfigurationResponse:
        """
        @summary Creates a scaling configuration of the Elastic Container Instance type. Auto Scaling uses the scaling configuration as a template to create elastic container instances to meet your business requirements during scale-outs.
        
        @description A scaling configuration is a template that is used to create elastic container instances during scale-out activities.
        You can specify the Cpu and Memory parameters to determine the range of instance types. If you specify the parameters, Auto Scaling determines the available instance types based on factors such as I/O optimization requirements and zones. Auto Scaling preferentially creates elastic container instances of the instance type that is provided at the lowest price. This scaling mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        
        @param request: CreateEciScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not UtilClient.is_unset(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not UtilClient.is_unset(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not UtilClient.is_unset(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not UtilClient.is_unset(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not UtilClient.is_unset(request.containers):
            query['Containers'] = request.containers
        if not UtilClient.is_unset(request.cost_optimization):
            query['CostOptimization'] = request.cost_optimization
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not UtilClient.is_unset(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not UtilClient.is_unset(request.data_cache_bucket):
            query['DataCacheBucket'] = request.data_cache_bucket
        if not UtilClient.is_unset(request.data_cache_bursting_enabled):
            query['DataCacheBurstingEnabled'] = request.data_cache_bursting_enabled
        if not UtilClient.is_unset(request.data_cache_pl):
            query['DataCachePL'] = request.data_cache_pl
        if not UtilClient.is_unset(request.data_cache_provisioned_iops):
            query['DataCacheProvisionedIops'] = request.data_cache_provisioned_iops
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dns_config_name_servers):
            query['DnsConfigNameServers'] = request.dns_config_name_servers
        if not UtilClient.is_unset(request.dns_config_options):
            query['DnsConfigOptions'] = request.dns_config_options
        if not UtilClient.is_unset(request.dns_config_searchs):
            query['DnsConfigSearchs'] = request.dns_config_searchs
        if not UtilClient.is_unset(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not UtilClient.is_unset(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.host_aliases):
            query['HostAliases'] = request.host_aliases
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not UtilClient.is_unset(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not UtilClient.is_unset(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not UtilClient.is_unset(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.ntp_servers):
            query['NtpServers'] = request.ntp_servers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.security_context_sysctls):
            query['SecurityContextSysctls'] = request.security_context_sysctls
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.volumes):
            query['Volumes'] = request.volumes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_eci_scaling_configuration_with_options_async(
        self,
        request: ess_20220222_models.CreateEciScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateEciScalingConfigurationResponse:
        """
        @summary Creates a scaling configuration of the Elastic Container Instance type. Auto Scaling uses the scaling configuration as a template to create elastic container instances to meet your business requirements during scale-outs.
        
        @description A scaling configuration is a template that is used to create elastic container instances during scale-out activities.
        You can specify the Cpu and Memory parameters to determine the range of instance types. If you specify the parameters, Auto Scaling determines the available instance types based on factors such as I/O optimization requirements and zones. Auto Scaling preferentially creates elastic container instances of the instance type that is provided at the lowest price. This scaling mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        
        @param request: CreateEciScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not UtilClient.is_unset(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not UtilClient.is_unset(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not UtilClient.is_unset(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not UtilClient.is_unset(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not UtilClient.is_unset(request.containers):
            query['Containers'] = request.containers
        if not UtilClient.is_unset(request.cost_optimization):
            query['CostOptimization'] = request.cost_optimization
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not UtilClient.is_unset(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not UtilClient.is_unset(request.data_cache_bucket):
            query['DataCacheBucket'] = request.data_cache_bucket
        if not UtilClient.is_unset(request.data_cache_bursting_enabled):
            query['DataCacheBurstingEnabled'] = request.data_cache_bursting_enabled
        if not UtilClient.is_unset(request.data_cache_pl):
            query['DataCachePL'] = request.data_cache_pl
        if not UtilClient.is_unset(request.data_cache_provisioned_iops):
            query['DataCacheProvisionedIops'] = request.data_cache_provisioned_iops
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dns_config_name_servers):
            query['DnsConfigNameServers'] = request.dns_config_name_servers
        if not UtilClient.is_unset(request.dns_config_options):
            query['DnsConfigOptions'] = request.dns_config_options
        if not UtilClient.is_unset(request.dns_config_searchs):
            query['DnsConfigSearchs'] = request.dns_config_searchs
        if not UtilClient.is_unset(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not UtilClient.is_unset(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.host_aliases):
            query['HostAliases'] = request.host_aliases
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not UtilClient.is_unset(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not UtilClient.is_unset(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not UtilClient.is_unset(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.ntp_servers):
            query['NtpServers'] = request.ntp_servers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.security_context_sysctls):
            query['SecurityContextSysctls'] = request.security_context_sysctls
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.volumes):
            query['Volumes'] = request.volumes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateEciScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_eci_scaling_configuration(
        self,
        request: ess_20220222_models.CreateEciScalingConfigurationRequest,
    ) -> ess_20220222_models.CreateEciScalingConfigurationResponse:
        """
        @summary Creates a scaling configuration of the Elastic Container Instance type. Auto Scaling uses the scaling configuration as a template to create elastic container instances to meet your business requirements during scale-outs.
        
        @description A scaling configuration is a template that is used to create elastic container instances during scale-out activities.
        You can specify the Cpu and Memory parameters to determine the range of instance types. If you specify the parameters, Auto Scaling determines the available instance types based on factors such as I/O optimization requirements and zones. Auto Scaling preferentially creates elastic container instances of the instance type that is provided at the lowest price. This scaling mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        
        @param request: CreateEciScalingConfigurationRequest
        @return: CreateEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_eci_scaling_configuration_with_options(request, runtime)

    async def create_eci_scaling_configuration_async(
        self,
        request: ess_20220222_models.CreateEciScalingConfigurationRequest,
    ) -> ess_20220222_models.CreateEciScalingConfigurationResponse:
        """
        @summary Creates a scaling configuration of the Elastic Container Instance type. Auto Scaling uses the scaling configuration as a template to create elastic container instances to meet your business requirements during scale-outs.
        
        @description A scaling configuration is a template that is used to create elastic container instances during scale-out activities.
        You can specify the Cpu and Memory parameters to determine the range of instance types. If you specify the parameters, Auto Scaling determines the available instance types based on factors such as I/O optimization requirements and zones. Auto Scaling preferentially creates elastic container instances of the instance type that is provided at the lowest price. This scaling mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        
        @param request: CreateEciScalingConfigurationRequest
        @return: CreateEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_eci_scaling_configuration_with_options_async(request, runtime)

    def create_lifecycle_hook_with_options(
        self,
        request: ess_20220222_models.CreateLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateLifecycleHookResponse:
        """
        @summary Creates one or more lifecycle hooks in a scaling group. A lifecycle hook allows you to execute custom actions like sending notifications or automating script execution at critical stages (such as instance startup and termination) in the lifecycle of an instance. Implementing the lifecycle hook feature allows for finer control and management of instances. For example, you can verify configurations, set up custom tasks, or back up data on your instances when lifecycle hooks take effect, thus enhancing the flexibility and reliability of application deployment.
        
        @description You can create up to six lifecycle hooks for each scaling group. After a lifecycle hook is created for a scaling group, Elastic Compute Service (ECS) instances in the scaling group waits to be added to or removed from the scaling group during scaling activities. You can use the HeartbeatTimeout parameter to specify the timeout period of the lifecycle hook. During the timeout period of a lifecycle hook, you can perform custom operations such as initialize ECS instance configurations and download ECS instance data on the ECS instances for which the lifecycle hook is applied.
        During a scale-out activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be added to the associated whitelist that manages access to the ApsaraDB RDS instance. The ECS instances also wait to be added to the backend server group of the associated Classic Load Balancer (CLB) instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are added to the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also added to the backend server group of the associated CLB instance. During a scale-in activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances also wait to be removed from the backend server group of the associated CLB instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also removed from the backend server group of the associated CLB instance.
        You can configure a notification method for a lifecycle hook. When the lifecycle hook is triggered, a notification can be sent to the specified Message Service (MNS) topic or queue, or an operation can be performed based on the specified Operation Orchestration Service (OOS) template. If you want to configure an OOS template, you must create a Resource Access Management (RAM) role for OOS. For more information, see [Grant RAM permissions to OOS](https://help.aliyun.com/document_detail/120810.html).
        > If your scaling group has existing ECS instances and you configured an OOS template that is used to add the private IP addresses of ECS instances to or remove the private IP addresses of ECS instances from the whitelists that manage access to cloud databases that are not ApsaraDB RDS databases, you must manually add the private IP addresses of the ECS instances to or remove the private IP addresses of the ECS instances from the whitelists that manage access to the cloud databases.
        
        @param request: CreateLifecycleHookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLifecycleHookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_result):
            query['DefaultResult'] = request.default_result
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['HeartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.lifecycle_transition):
            query['LifecycleTransition'] = request.lifecycle_transition
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_metadata):
            query['NotificationMetadata'] = request.notification_metadata
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateLifecycleHookResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_lifecycle_hook_with_options_async(
        self,
        request: ess_20220222_models.CreateLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateLifecycleHookResponse:
        """
        @summary Creates one or more lifecycle hooks in a scaling group. A lifecycle hook allows you to execute custom actions like sending notifications or automating script execution at critical stages (such as instance startup and termination) in the lifecycle of an instance. Implementing the lifecycle hook feature allows for finer control and management of instances. For example, you can verify configurations, set up custom tasks, or back up data on your instances when lifecycle hooks take effect, thus enhancing the flexibility and reliability of application deployment.
        
        @description You can create up to six lifecycle hooks for each scaling group. After a lifecycle hook is created for a scaling group, Elastic Compute Service (ECS) instances in the scaling group waits to be added to or removed from the scaling group during scaling activities. You can use the HeartbeatTimeout parameter to specify the timeout period of the lifecycle hook. During the timeout period of a lifecycle hook, you can perform custom operations such as initialize ECS instance configurations and download ECS instance data on the ECS instances for which the lifecycle hook is applied.
        During a scale-out activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be added to the associated whitelist that manages access to the ApsaraDB RDS instance. The ECS instances also wait to be added to the backend server group of the associated Classic Load Balancer (CLB) instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are added to the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also added to the backend server group of the associated CLB instance. During a scale-in activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances also wait to be removed from the backend server group of the associated CLB instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also removed from the backend server group of the associated CLB instance.
        You can configure a notification method for a lifecycle hook. When the lifecycle hook is triggered, a notification can be sent to the specified Message Service (MNS) topic or queue, or an operation can be performed based on the specified Operation Orchestration Service (OOS) template. If you want to configure an OOS template, you must create a Resource Access Management (RAM) role for OOS. For more information, see [Grant RAM permissions to OOS](https://help.aliyun.com/document_detail/120810.html).
        > If your scaling group has existing ECS instances and you configured an OOS template that is used to add the private IP addresses of ECS instances to or remove the private IP addresses of ECS instances from the whitelists that manage access to cloud databases that are not ApsaraDB RDS databases, you must manually add the private IP addresses of the ECS instances to or remove the private IP addresses of the ECS instances from the whitelists that manage access to the cloud databases.
        
        @param request: CreateLifecycleHookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLifecycleHookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_result):
            query['DefaultResult'] = request.default_result
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['HeartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.lifecycle_transition):
            query['LifecycleTransition'] = request.lifecycle_transition
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_metadata):
            query['NotificationMetadata'] = request.notification_metadata
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateLifecycleHookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_lifecycle_hook(
        self,
        request: ess_20220222_models.CreateLifecycleHookRequest,
    ) -> ess_20220222_models.CreateLifecycleHookResponse:
        """
        @summary Creates one or more lifecycle hooks in a scaling group. A lifecycle hook allows you to execute custom actions like sending notifications or automating script execution at critical stages (such as instance startup and termination) in the lifecycle of an instance. Implementing the lifecycle hook feature allows for finer control and management of instances. For example, you can verify configurations, set up custom tasks, or back up data on your instances when lifecycle hooks take effect, thus enhancing the flexibility and reliability of application deployment.
        
        @description You can create up to six lifecycle hooks for each scaling group. After a lifecycle hook is created for a scaling group, Elastic Compute Service (ECS) instances in the scaling group waits to be added to or removed from the scaling group during scaling activities. You can use the HeartbeatTimeout parameter to specify the timeout period of the lifecycle hook. During the timeout period of a lifecycle hook, you can perform custom operations such as initialize ECS instance configurations and download ECS instance data on the ECS instances for which the lifecycle hook is applied.
        During a scale-out activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be added to the associated whitelist that manages access to the ApsaraDB RDS instance. The ECS instances also wait to be added to the backend server group of the associated Classic Load Balancer (CLB) instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are added to the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also added to the backend server group of the associated CLB instance. During a scale-in activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances also wait to be removed from the backend server group of the associated CLB instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also removed from the backend server group of the associated CLB instance.
        You can configure a notification method for a lifecycle hook. When the lifecycle hook is triggered, a notification can be sent to the specified Message Service (MNS) topic or queue, or an operation can be performed based on the specified Operation Orchestration Service (OOS) template. If you want to configure an OOS template, you must create a Resource Access Management (RAM) role for OOS. For more information, see [Grant RAM permissions to OOS](https://help.aliyun.com/document_detail/120810.html).
        > If your scaling group has existing ECS instances and you configured an OOS template that is used to add the private IP addresses of ECS instances to or remove the private IP addresses of ECS instances from the whitelists that manage access to cloud databases that are not ApsaraDB RDS databases, you must manually add the private IP addresses of the ECS instances to or remove the private IP addresses of the ECS instances from the whitelists that manage access to the cloud databases.
        
        @param request: CreateLifecycleHookRequest
        @return: CreateLifecycleHookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_lifecycle_hook_with_options(request, runtime)

    async def create_lifecycle_hook_async(
        self,
        request: ess_20220222_models.CreateLifecycleHookRequest,
    ) -> ess_20220222_models.CreateLifecycleHookResponse:
        """
        @summary Creates one or more lifecycle hooks in a scaling group. A lifecycle hook allows you to execute custom actions like sending notifications or automating script execution at critical stages (such as instance startup and termination) in the lifecycle of an instance. Implementing the lifecycle hook feature allows for finer control and management of instances. For example, you can verify configurations, set up custom tasks, or back up data on your instances when lifecycle hooks take effect, thus enhancing the flexibility and reliability of application deployment.
        
        @description You can create up to six lifecycle hooks for each scaling group. After a lifecycle hook is created for a scaling group, Elastic Compute Service (ECS) instances in the scaling group waits to be added to or removed from the scaling group during scaling activities. You can use the HeartbeatTimeout parameter to specify the timeout period of the lifecycle hook. During the timeout period of a lifecycle hook, you can perform custom operations such as initialize ECS instance configurations and download ECS instance data on the ECS instances for which the lifecycle hook is applied.
        During a scale-out activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be added to the associated whitelist that manages access to the ApsaraDB RDS instance. The ECS instances also wait to be added to the backend server group of the associated Classic Load Balancer (CLB) instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are added to the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also added to the backend server group of the associated CLB instance. During a scale-in activity and the timeout period of a lifecycle hook, the private IP addresses of ECS instances wait to be removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances also wait to be removed from the backend server group of the associated CLB instance. After the lifecycle hook times out, the private IP addresses of the ECS instances are removed from the whitelist that manages access to the associated ApsaraDB RDS instance. The ECS instances are also removed from the backend server group of the associated CLB instance.
        You can configure a notification method for a lifecycle hook. When the lifecycle hook is triggered, a notification can be sent to the specified Message Service (MNS) topic or queue, or an operation can be performed based on the specified Operation Orchestration Service (OOS) template. If you want to configure an OOS template, you must create a Resource Access Management (RAM) role for OOS. For more information, see [Grant RAM permissions to OOS](https://help.aliyun.com/document_detail/120810.html).
        > If your scaling group has existing ECS instances and you configured an OOS template that is used to add the private IP addresses of ECS instances to or remove the private IP addresses of ECS instances from the whitelists that manage access to cloud databases that are not ApsaraDB RDS databases, you must manually add the private IP addresses of the ECS instances to or remove the private IP addresses of the ECS instances from the whitelists that manage access to the cloud databases.
        
        @param request: CreateLifecycleHookRequest
        @return: CreateLifecycleHookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_lifecycle_hook_with_options_async(request, runtime)

    def create_notification_configuration_with_options(
        self,
        request: ess_20220222_models.CreateNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateNotificationConfigurationResponse:
        """
        @summary Creates a notification rule. You can call the CreateNotificationConfiguration operation to create a notification rule to stay informed about scaling events or resource changes. This helps you learn about the dynamic status of your scaling group in real time and further automates the management of scaling events.
        
        @description ## Description
        You can configure CloudMonitor system events, Message Service (MNS) queues, or MNS topics to receive notifications. When a specified type of scaling activity or resource change occurs in a scaling group, Auto Scaling sends notifications by using CloudMonitor or MNS.
        
        @param request: CreateNotificationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNotificationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_types):
            query['NotificationTypes'] = request.notification_types
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateNotificationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_notification_configuration_with_options_async(
        self,
        request: ess_20220222_models.CreateNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateNotificationConfigurationResponse:
        """
        @summary Creates a notification rule. You can call the CreateNotificationConfiguration operation to create a notification rule to stay informed about scaling events or resource changes. This helps you learn about the dynamic status of your scaling group in real time and further automates the management of scaling events.
        
        @description ## Description
        You can configure CloudMonitor system events, Message Service (MNS) queues, or MNS topics to receive notifications. When a specified type of scaling activity or resource change occurs in a scaling group, Auto Scaling sends notifications by using CloudMonitor or MNS.
        
        @param request: CreateNotificationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNotificationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_types):
            query['NotificationTypes'] = request.notification_types
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateNotificationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_notification_configuration(
        self,
        request: ess_20220222_models.CreateNotificationConfigurationRequest,
    ) -> ess_20220222_models.CreateNotificationConfigurationResponse:
        """
        @summary Creates a notification rule. You can call the CreateNotificationConfiguration operation to create a notification rule to stay informed about scaling events or resource changes. This helps you learn about the dynamic status of your scaling group in real time and further automates the management of scaling events.
        
        @description ## Description
        You can configure CloudMonitor system events, Message Service (MNS) queues, or MNS topics to receive notifications. When a specified type of scaling activity or resource change occurs in a scaling group, Auto Scaling sends notifications by using CloudMonitor or MNS.
        
        @param request: CreateNotificationConfigurationRequest
        @return: CreateNotificationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_notification_configuration_with_options(request, runtime)

    async def create_notification_configuration_async(
        self,
        request: ess_20220222_models.CreateNotificationConfigurationRequest,
    ) -> ess_20220222_models.CreateNotificationConfigurationResponse:
        """
        @summary Creates a notification rule. You can call the CreateNotificationConfiguration operation to create a notification rule to stay informed about scaling events or resource changes. This helps you learn about the dynamic status of your scaling group in real time and further automates the management of scaling events.
        
        @description ## Description
        You can configure CloudMonitor system events, Message Service (MNS) queues, or MNS topics to receive notifications. When a specified type of scaling activity or resource change occurs in a scaling group, Auto Scaling sends notifications by using CloudMonitor or MNS.
        
        @param request: CreateNotificationConfigurationRequest
        @return: CreateNotificationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_notification_configuration_with_options_async(request, runtime)

    def create_scaling_configuration_with_options(
        self,
        tmp_req: ess_20220222_models.CreateScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScalingConfigurationResponse:
        """
        @summary Creates a scaling configuration.
        
        @description Auto Scaling automatically creates Elastic Compute Service (ECS) instances based on the specified scaling configuration. ECS instances can be created in the following modes:
        InstancePatternInfos: intelligent configuration mode. In this mode, you need to only specify the number of vCPUs, memory size, instance family, and maximum price. Auto Scaling selects the instance type that has the lowest price based on the configurations to create ECS instances. This mode is available only for scaling groups that reside in virtual private clouds (VPCs). This mode reduces scale-out failures caused by insufficient inventory of instance types.
        InstanceType: In this mode, you must specify one instance type.
        InstanceTypes: In this mode, you can specify more than one instance type.
        InstanceTypeOverrides: In this mode, you can specify multiple instance types and weights for the instance types.
        Cpu and Memory: In this mode, you must specify the number of vCPUs and the memory size. Auto Scaling determines the range of available instance types based on factors such as I/O optimization requirements and zones. Then, Auto Scaling creates ECS instances by using the lowest-priced instance type. This mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        > You cannot specify InstanceType, InstanceTypes, InstanceTypeOverrides, and Cpu and Memory at the same time. You can specify InstanceType and InstancePatternInfos or specify InstanceTypes and InstancePatternInfo at the same time. If you specify InstanceType and InstancePatternInfos or specify InstanceTypes and InstancePatternInfos at the same time, Auto Scaling preferentially uses the instance types that are specified by InstanceType or InstanceTypes for scale-outs. If the instance types that are specified by InstanceType or InstanceTypes do not have sufficient inventory, Auto Scaling uses the instance types that are specified by InstancePatternInfos for scale-outs.
        
        @param tmp_req: CreateScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ess_20220222_models.CreateScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.custom_priorities):
            query['CustomPriorities'] = request.custom_priorities
        if not UtilClient.is_unset(request.data_disks):
            query['DataDisks'] = request.data_disks
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_pattern_infos):
            query['InstancePatternInfos'] = request.instance_pattern_infos
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_overrides):
            query['InstanceTypeOverrides'] = request.instance_type_overrides
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.network_interfaces):
            query['NetworkInterfaces'] = request.network_interfaces
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scheduler_options_shrink):
            query['SchedulerOptions'] = request.scheduler_options_shrink
        if not UtilClient.is_unset(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limits):
            query['SpotPriceLimits'] = request.spot_price_limits
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.system_disk_categories):
            query['SystemDiskCategories'] = request.system_disk_categories
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.image_options):
            query['ImageOptions'] = request.image_options
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_configuration_with_options_async(
        self,
        tmp_req: ess_20220222_models.CreateScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScalingConfigurationResponse:
        """
        @summary Creates a scaling configuration.
        
        @description Auto Scaling automatically creates Elastic Compute Service (ECS) instances based on the specified scaling configuration. ECS instances can be created in the following modes:
        InstancePatternInfos: intelligent configuration mode. In this mode, you need to only specify the number of vCPUs, memory size, instance family, and maximum price. Auto Scaling selects the instance type that has the lowest price based on the configurations to create ECS instances. This mode is available only for scaling groups that reside in virtual private clouds (VPCs). This mode reduces scale-out failures caused by insufficient inventory of instance types.
        InstanceType: In this mode, you must specify one instance type.
        InstanceTypes: In this mode, you can specify more than one instance type.
        InstanceTypeOverrides: In this mode, you can specify multiple instance types and weights for the instance types.
        Cpu and Memory: In this mode, you must specify the number of vCPUs and the memory size. Auto Scaling determines the range of available instance types based on factors such as I/O optimization requirements and zones. Then, Auto Scaling creates ECS instances by using the lowest-priced instance type. This mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        > You cannot specify InstanceType, InstanceTypes, InstanceTypeOverrides, and Cpu and Memory at the same time. You can specify InstanceType and InstancePatternInfos or specify InstanceTypes and InstancePatternInfo at the same time. If you specify InstanceType and InstancePatternInfos or specify InstanceTypes and InstancePatternInfos at the same time, Auto Scaling preferentially uses the instance types that are specified by InstanceType or InstanceTypes for scale-outs. If the instance types that are specified by InstanceType or InstanceTypes do not have sufficient inventory, Auto Scaling uses the instance types that are specified by InstancePatternInfos for scale-outs.
        
        @param tmp_req: CreateScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ess_20220222_models.CreateScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.custom_priorities):
            query['CustomPriorities'] = request.custom_priorities
        if not UtilClient.is_unset(request.data_disks):
            query['DataDisks'] = request.data_disks
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_pattern_infos):
            query['InstancePatternInfos'] = request.instance_pattern_infos
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.instance_type_overrides):
            query['InstanceTypeOverrides'] = request.instance_type_overrides
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_in):
            query['InternetMaxBandwidthIn'] = request.internet_max_bandwidth_in
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.network_interfaces):
            query['NetworkInterfaces'] = request.network_interfaces
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scheduler_options_shrink):
            query['SchedulerOptions'] = request.scheduler_options_shrink
        if not UtilClient.is_unset(request.security_enhancement_strategy):
            query['SecurityEnhancementStrategy'] = request.security_enhancement_strategy
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limits):
            query['SpotPriceLimits'] = request.spot_price_limits
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.system_disk_categories):
            query['SystemDiskCategories'] = request.system_disk_categories
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.image_options):
            query['ImageOptions'] = request.image_options
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scaling_configuration(
        self,
        request: ess_20220222_models.CreateScalingConfigurationRequest,
    ) -> ess_20220222_models.CreateScalingConfigurationResponse:
        """
        @summary Creates a scaling configuration.
        
        @description Auto Scaling automatically creates Elastic Compute Service (ECS) instances based on the specified scaling configuration. ECS instances can be created in the following modes:
        InstancePatternInfos: intelligent configuration mode. In this mode, you need to only specify the number of vCPUs, memory size, instance family, and maximum price. Auto Scaling selects the instance type that has the lowest price based on the configurations to create ECS instances. This mode is available only for scaling groups that reside in virtual private clouds (VPCs). This mode reduces scale-out failures caused by insufficient inventory of instance types.
        InstanceType: In this mode, you must specify one instance type.
        InstanceTypes: In this mode, you can specify more than one instance type.
        InstanceTypeOverrides: In this mode, you can specify multiple instance types and weights for the instance types.
        Cpu and Memory: In this mode, you must specify the number of vCPUs and the memory size. Auto Scaling determines the range of available instance types based on factors such as I/O optimization requirements and zones. Then, Auto Scaling creates ECS instances by using the lowest-priced instance type. This mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        > You cannot specify InstanceType, InstanceTypes, InstanceTypeOverrides, and Cpu and Memory at the same time. You can specify InstanceType and InstancePatternInfos or specify InstanceTypes and InstancePatternInfo at the same time. If you specify InstanceType and InstancePatternInfos or specify InstanceTypes and InstancePatternInfos at the same time, Auto Scaling preferentially uses the instance types that are specified by InstanceType or InstanceTypes for scale-outs. If the instance types that are specified by InstanceType or InstanceTypes do not have sufficient inventory, Auto Scaling uses the instance types that are specified by InstancePatternInfos for scale-outs.
        
        @param request: CreateScalingConfigurationRequest
        @return: CreateScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_configuration_with_options(request, runtime)

    async def create_scaling_configuration_async(
        self,
        request: ess_20220222_models.CreateScalingConfigurationRequest,
    ) -> ess_20220222_models.CreateScalingConfigurationResponse:
        """
        @summary Creates a scaling configuration.
        
        @description Auto Scaling automatically creates Elastic Compute Service (ECS) instances based on the specified scaling configuration. ECS instances can be created in the following modes:
        InstancePatternInfos: intelligent configuration mode. In this mode, you need to only specify the number of vCPUs, memory size, instance family, and maximum price. Auto Scaling selects the instance type that has the lowest price based on the configurations to create ECS instances. This mode is available only for scaling groups that reside in virtual private clouds (VPCs). This mode reduces scale-out failures caused by insufficient inventory of instance types.
        InstanceType: In this mode, you must specify one instance type.
        InstanceTypes: In this mode, you can specify more than one instance type.
        InstanceTypeOverrides: In this mode, you can specify multiple instance types and weights for the instance types.
        Cpu and Memory: In this mode, you must specify the number of vCPUs and the memory size. Auto Scaling determines the range of available instance types based on factors such as I/O optimization requirements and zones. Then, Auto Scaling creates ECS instances by using the lowest-priced instance type. This mode is available only if Scaling Policy is set to Cost Optimization Policy and no instance type is specified in the scaling configuration.
        > You cannot specify InstanceType, InstanceTypes, InstanceTypeOverrides, and Cpu and Memory at the same time. You can specify InstanceType and InstancePatternInfos or specify InstanceTypes and InstancePatternInfo at the same time. If you specify InstanceType and InstancePatternInfos or specify InstanceTypes and InstancePatternInfos at the same time, Auto Scaling preferentially uses the instance types that are specified by InstanceType or InstanceTypes for scale-outs. If the instance types that are specified by InstanceType or InstanceTypes do not have sufficient inventory, Auto Scaling uses the instance types that are specified by InstancePatternInfos for scale-outs.
        
        @param request: CreateScalingConfigurationRequest
        @return: CreateScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_configuration_with_options_async(request, runtime)

    def create_scaling_group_with_options(
        self,
        request: ess_20220222_models.CreateScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScalingGroupResponse:
        """
        @summary Creates a scaling group. You can call the CreateScalingGroup operation to automate the adjustment of computing power of a specific type based on your business requirements and scaling polices.
        
        @description A scaling group is a group of Elastic Compute Service (ECS) instances that can be used for similar purposes.
        You can create only a limited number of scaling groups in a region. To check the quota of the scaling groups, go to Quota Center.
        A scaling group does not immediately take effect after you create the scaling group. You can call the [EnableScalingGroup](https://help.aliyun.com/document_detail/25939.html) operation to enable a scaling group. You can trigger scaling events and execute scaling rules only in scaling groups that are in the Enabled state.
        If you want to attach a Classic Load Balancer (CLB, formerly known as SLB) instance and an ApsaraDB RDS instance to the scaling group that you want to create, the scaling group, the CLB instance, and the ApsaraDB RDS instance must reside in the same region. For more information, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        If you attach a CLB instance to the scaling group that you want to create, Auto Scaling will automatically add the ECS instances in the scaling group to the backend server groups of the CLB instance. You can specify the following types of server groups to add ECS instances:
        Default server group: ECS instances in this group process frontend requests. If no listeners are configured for vServer groups or primary/secondary server groups, the frontend requests are forwarded to the ECS instances in the default server group.
        vServer group: If you want to forward different requests to different backend servers, or you want to forward requests based on domain names and URLs, you can specify vServer groups.
        >  If you specify both the default server group and multiple server groups simultaneously, Auto Scaling will add the ECS instances in your scaling group to these server groups concurrently.
        The default weight of each ECS instance as a backend server is 50. If you want to attach a CLB instance to the scaling group that you want to create, make sure that the CLB instance meets the following requirements:
        The CLB instance is in the Active state. You can call the [DescribeLoadBalancers](https://help.aliyun.com/document_detail/2401696.html) operation to query the status of CLB instances.
        Health check must be enabled on all listener ports configured for the CLB instance. Otherwise, the scaling group will fail to be created.
        If you attach Application Load Balancer (ALB) or Network Load Balancer (NLB) server groups to the scaling group that you want to create, Auto Scaling will add the ECS instances in your scaling group to the ALB or NLB server groups to process the access requests forwarded by the corresponding ALB or NLB instances. You can attach multiple ALB or NLB server groups to a scaling group. Make sure that the ALB or NLB server groups belong to the same virtual private cloud (VPC). For more information, see [AttachAlbServerGroups](https://help.aliyun.com/document_detail/266800.html) or [AttachServerGroups](https://help.aliyun.com/document_detail/600559.html).
        If you attach an ApsaraDB RDS instance to the scaling group that you want to create, Auto Scaling will automatically add the private IP addresses of the ECS instances in your scaling group to the IP address whitelist of the ApsaraDB RDS instance. Before you attach an ApsaraDB RDS instance to your scaling group, make sure that the ApsaraDB RDS instance meets the following requirements:
        The ApsaraDB RDS instance is in the Running state. You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/610396.html) state to query the status of ApsaraDB RDS instances.
        The number of IP addresses in the IP address whitelist of the ApsaraDB RDS instance does not reach its upper limit. For more information, see [Configure a whitelist](https://help.aliyun.com/document_detail/43185.html).
        If you set MultiAZPolicy for the scaling group that you want to create to COST_OPTIMIZED, the following rules apply:
        If you use OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, and SpotInstancePools to specify the instance allocation mode under the cost optimization policy, Auto Scaling will prioritize the implementation of the specified instance allocation mode during scale-out events.
        If you do not specify OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, or SpotInstancePools, Auto Scaling will preferentially create instances of the lowest-priced instance type based on the cost optimization policy.
        If you set `Tags.Propagate` to true, the following rules will apply:
        Tags that you add to the scaling group cannot be propagated to existing instances in the scaling group. Tags that you add to the scaling group are propagated to only new instances.
        If you specify instance tags in the scaling configuration that is used to create instances and propagate the tags that you add to the scaling group to the instances, all tags exist at the same time.
        If the tag key that you specify in a scaling configuration and the tag key that you add to the scaling group of the scaling configuration are the same, the tag value that you specify in the scaling configuration is preferentially used.
        
        @param request: CreateScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.allocation_strategy):
            query['AllocationStrategy'] = request.allocation_strategy
        if not UtilClient.is_unset(request.az_balance):
            query['AzBalance'] = request.az_balance
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compensate_with_on_demand):
            query['CompensateWithOnDemand'] = request.compensate_with_on_demand
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.custom_policy_arn):
            query['CustomPolicyARN'] = request.custom_policy_arn
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not UtilClient.is_unset(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_types):
            query['HealthCheckTypes'] = request.health_check_types
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.lifecycle_hooks):
            query['LifecycleHooks'] = request.lifecycle_hooks
        if not UtilClient.is_unset(request.load_balancer_configs):
            query['LoadBalancerConfigs'] = request.load_balancer_configs
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_instance_lifetime):
            query['MaxInstanceLifetime'] = request.max_instance_lifetime
        if not UtilClient.is_unset(request.max_size):
            query['MaxSize'] = request.max_size
        if not UtilClient.is_unset(request.min_size):
            query['MinSize'] = request.min_size
        if not UtilClient.is_unset(request.multi_azpolicy):
            query['MultiAZPolicy'] = request.multi_azpolicy
        if not UtilClient.is_unset(request.on_demand_base_capacity):
            query['OnDemandBaseCapacity'] = request.on_demand_base_capacity
        if not UtilClient.is_unset(request.on_demand_percentage_above_base_capacity):
            query['OnDemandPercentageAboveBaseCapacity'] = request.on_demand_percentage_above_base_capacity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.removal_policies):
            query['RemovalPolicies'] = request.removal_policies
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        if not UtilClient.is_unset(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not UtilClient.is_unset(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not UtilClient.is_unset(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not UtilClient.is_unset(request.sync_alarm_rule_to_cms):
            query['SyncAlarmRuleToCms'] = request.sync_alarm_rule_to_cms
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_group_with_options_async(
        self,
        request: ess_20220222_models.CreateScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScalingGroupResponse:
        """
        @summary Creates a scaling group. You can call the CreateScalingGroup operation to automate the adjustment of computing power of a specific type based on your business requirements and scaling polices.
        
        @description A scaling group is a group of Elastic Compute Service (ECS) instances that can be used for similar purposes.
        You can create only a limited number of scaling groups in a region. To check the quota of the scaling groups, go to Quota Center.
        A scaling group does not immediately take effect after you create the scaling group. You can call the [EnableScalingGroup](https://help.aliyun.com/document_detail/25939.html) operation to enable a scaling group. You can trigger scaling events and execute scaling rules only in scaling groups that are in the Enabled state.
        If you want to attach a Classic Load Balancer (CLB, formerly known as SLB) instance and an ApsaraDB RDS instance to the scaling group that you want to create, the scaling group, the CLB instance, and the ApsaraDB RDS instance must reside in the same region. For more information, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        If you attach a CLB instance to the scaling group that you want to create, Auto Scaling will automatically add the ECS instances in the scaling group to the backend server groups of the CLB instance. You can specify the following types of server groups to add ECS instances:
        Default server group: ECS instances in this group process frontend requests. If no listeners are configured for vServer groups or primary/secondary server groups, the frontend requests are forwarded to the ECS instances in the default server group.
        vServer group: If you want to forward different requests to different backend servers, or you want to forward requests based on domain names and URLs, you can specify vServer groups.
        >  If you specify both the default server group and multiple server groups simultaneously, Auto Scaling will add the ECS instances in your scaling group to these server groups concurrently.
        The default weight of each ECS instance as a backend server is 50. If you want to attach a CLB instance to the scaling group that you want to create, make sure that the CLB instance meets the following requirements:
        The CLB instance is in the Active state. You can call the [DescribeLoadBalancers](https://help.aliyun.com/document_detail/2401696.html) operation to query the status of CLB instances.
        Health check must be enabled on all listener ports configured for the CLB instance. Otherwise, the scaling group will fail to be created.
        If you attach Application Load Balancer (ALB) or Network Load Balancer (NLB) server groups to the scaling group that you want to create, Auto Scaling will add the ECS instances in your scaling group to the ALB or NLB server groups to process the access requests forwarded by the corresponding ALB or NLB instances. You can attach multiple ALB or NLB server groups to a scaling group. Make sure that the ALB or NLB server groups belong to the same virtual private cloud (VPC). For more information, see [AttachAlbServerGroups](https://help.aliyun.com/document_detail/266800.html) or [AttachServerGroups](https://help.aliyun.com/document_detail/600559.html).
        If you attach an ApsaraDB RDS instance to the scaling group that you want to create, Auto Scaling will automatically add the private IP addresses of the ECS instances in your scaling group to the IP address whitelist of the ApsaraDB RDS instance. Before you attach an ApsaraDB RDS instance to your scaling group, make sure that the ApsaraDB RDS instance meets the following requirements:
        The ApsaraDB RDS instance is in the Running state. You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/610396.html) state to query the status of ApsaraDB RDS instances.
        The number of IP addresses in the IP address whitelist of the ApsaraDB RDS instance does not reach its upper limit. For more information, see [Configure a whitelist](https://help.aliyun.com/document_detail/43185.html).
        If you set MultiAZPolicy for the scaling group that you want to create to COST_OPTIMIZED, the following rules apply:
        If you use OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, and SpotInstancePools to specify the instance allocation mode under the cost optimization policy, Auto Scaling will prioritize the implementation of the specified instance allocation mode during scale-out events.
        If you do not specify OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, or SpotInstancePools, Auto Scaling will preferentially create instances of the lowest-priced instance type based on the cost optimization policy.
        If you set `Tags.Propagate` to true, the following rules will apply:
        Tags that you add to the scaling group cannot be propagated to existing instances in the scaling group. Tags that you add to the scaling group are propagated to only new instances.
        If you specify instance tags in the scaling configuration that is used to create instances and propagate the tags that you add to the scaling group to the instances, all tags exist at the same time.
        If the tag key that you specify in a scaling configuration and the tag key that you add to the scaling group of the scaling configuration are the same, the tag value that you specify in the scaling configuration is preferentially used.
        
        @param request: CreateScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.allocation_strategy):
            query['AllocationStrategy'] = request.allocation_strategy
        if not UtilClient.is_unset(request.az_balance):
            query['AzBalance'] = request.az_balance
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compensate_with_on_demand):
            query['CompensateWithOnDemand'] = request.compensate_with_on_demand
        if not UtilClient.is_unset(request.container_group_id):
            query['ContainerGroupId'] = request.container_group_id
        if not UtilClient.is_unset(request.custom_policy_arn):
            query['CustomPolicyARN'] = request.custom_policy_arn
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not UtilClient.is_unset(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_types):
            query['HealthCheckTypes'] = request.health_check_types
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.lifecycle_hooks):
            query['LifecycleHooks'] = request.lifecycle_hooks
        if not UtilClient.is_unset(request.load_balancer_configs):
            query['LoadBalancerConfigs'] = request.load_balancer_configs
        if not UtilClient.is_unset(request.load_balancer_ids):
            query['LoadBalancerIds'] = request.load_balancer_ids
        if not UtilClient.is_unset(request.max_instance_lifetime):
            query['MaxInstanceLifetime'] = request.max_instance_lifetime
        if not UtilClient.is_unset(request.max_size):
            query['MaxSize'] = request.max_size
        if not UtilClient.is_unset(request.min_size):
            query['MinSize'] = request.min_size
        if not UtilClient.is_unset(request.multi_azpolicy):
            query['MultiAZPolicy'] = request.multi_azpolicy
        if not UtilClient.is_unset(request.on_demand_base_capacity):
            query['OnDemandBaseCapacity'] = request.on_demand_base_capacity
        if not UtilClient.is_unset(request.on_demand_percentage_above_base_capacity):
            query['OnDemandPercentageAboveBaseCapacity'] = request.on_demand_percentage_above_base_capacity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.removal_policies):
            query['RemovalPolicies'] = request.removal_policies
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        if not UtilClient.is_unset(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not UtilClient.is_unset(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not UtilClient.is_unset(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not UtilClient.is_unset(request.sync_alarm_rule_to_cms):
            query['SyncAlarmRuleToCms'] = request.sync_alarm_rule_to_cms
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scaling_group(
        self,
        request: ess_20220222_models.CreateScalingGroupRequest,
    ) -> ess_20220222_models.CreateScalingGroupResponse:
        """
        @summary Creates a scaling group. You can call the CreateScalingGroup operation to automate the adjustment of computing power of a specific type based on your business requirements and scaling polices.
        
        @description A scaling group is a group of Elastic Compute Service (ECS) instances that can be used for similar purposes.
        You can create only a limited number of scaling groups in a region. To check the quota of the scaling groups, go to Quota Center.
        A scaling group does not immediately take effect after you create the scaling group. You can call the [EnableScalingGroup](https://help.aliyun.com/document_detail/25939.html) operation to enable a scaling group. You can trigger scaling events and execute scaling rules only in scaling groups that are in the Enabled state.
        If you want to attach a Classic Load Balancer (CLB, formerly known as SLB) instance and an ApsaraDB RDS instance to the scaling group that you want to create, the scaling group, the CLB instance, and the ApsaraDB RDS instance must reside in the same region. For more information, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        If you attach a CLB instance to the scaling group that you want to create, Auto Scaling will automatically add the ECS instances in the scaling group to the backend server groups of the CLB instance. You can specify the following types of server groups to add ECS instances:
        Default server group: ECS instances in this group process frontend requests. If no listeners are configured for vServer groups or primary/secondary server groups, the frontend requests are forwarded to the ECS instances in the default server group.
        vServer group: If you want to forward different requests to different backend servers, or you want to forward requests based on domain names and URLs, you can specify vServer groups.
        >  If you specify both the default server group and multiple server groups simultaneously, Auto Scaling will add the ECS instances in your scaling group to these server groups concurrently.
        The default weight of each ECS instance as a backend server is 50. If you want to attach a CLB instance to the scaling group that you want to create, make sure that the CLB instance meets the following requirements:
        The CLB instance is in the Active state. You can call the [DescribeLoadBalancers](https://help.aliyun.com/document_detail/2401696.html) operation to query the status of CLB instances.
        Health check must be enabled on all listener ports configured for the CLB instance. Otherwise, the scaling group will fail to be created.
        If you attach Application Load Balancer (ALB) or Network Load Balancer (NLB) server groups to the scaling group that you want to create, Auto Scaling will add the ECS instances in your scaling group to the ALB or NLB server groups to process the access requests forwarded by the corresponding ALB or NLB instances. You can attach multiple ALB or NLB server groups to a scaling group. Make sure that the ALB or NLB server groups belong to the same virtual private cloud (VPC). For more information, see [AttachAlbServerGroups](https://help.aliyun.com/document_detail/266800.html) or [AttachServerGroups](https://help.aliyun.com/document_detail/600559.html).
        If you attach an ApsaraDB RDS instance to the scaling group that you want to create, Auto Scaling will automatically add the private IP addresses of the ECS instances in your scaling group to the IP address whitelist of the ApsaraDB RDS instance. Before you attach an ApsaraDB RDS instance to your scaling group, make sure that the ApsaraDB RDS instance meets the following requirements:
        The ApsaraDB RDS instance is in the Running state. You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/610396.html) state to query the status of ApsaraDB RDS instances.
        The number of IP addresses in the IP address whitelist of the ApsaraDB RDS instance does not reach its upper limit. For more information, see [Configure a whitelist](https://help.aliyun.com/document_detail/43185.html).
        If you set MultiAZPolicy for the scaling group that you want to create to COST_OPTIMIZED, the following rules apply:
        If you use OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, and SpotInstancePools to specify the instance allocation mode under the cost optimization policy, Auto Scaling will prioritize the implementation of the specified instance allocation mode during scale-out events.
        If you do not specify OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, or SpotInstancePools, Auto Scaling will preferentially create instances of the lowest-priced instance type based on the cost optimization policy.
        If you set `Tags.Propagate` to true, the following rules will apply:
        Tags that you add to the scaling group cannot be propagated to existing instances in the scaling group. Tags that you add to the scaling group are propagated to only new instances.
        If you specify instance tags in the scaling configuration that is used to create instances and propagate the tags that you add to the scaling group to the instances, all tags exist at the same time.
        If the tag key that you specify in a scaling configuration and the tag key that you add to the scaling group of the scaling configuration are the same, the tag value that you specify in the scaling configuration is preferentially used.
        
        @param request: CreateScalingGroupRequest
        @return: CreateScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_group_with_options(request, runtime)

    async def create_scaling_group_async(
        self,
        request: ess_20220222_models.CreateScalingGroupRequest,
    ) -> ess_20220222_models.CreateScalingGroupResponse:
        """
        @summary Creates a scaling group. You can call the CreateScalingGroup operation to automate the adjustment of computing power of a specific type based on your business requirements and scaling polices.
        
        @description A scaling group is a group of Elastic Compute Service (ECS) instances that can be used for similar purposes.
        You can create only a limited number of scaling groups in a region. To check the quota of the scaling groups, go to Quota Center.
        A scaling group does not immediately take effect after you create the scaling group. You can call the [EnableScalingGroup](https://help.aliyun.com/document_detail/25939.html) operation to enable a scaling group. You can trigger scaling events and execute scaling rules only in scaling groups that are in the Enabled state.
        If you want to attach a Classic Load Balancer (CLB, formerly known as SLB) instance and an ApsaraDB RDS instance to the scaling group that you want to create, the scaling group, the CLB instance, and the ApsaraDB RDS instance must reside in the same region. For more information, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        If you attach a CLB instance to the scaling group that you want to create, Auto Scaling will automatically add the ECS instances in the scaling group to the backend server groups of the CLB instance. You can specify the following types of server groups to add ECS instances:
        Default server group: ECS instances in this group process frontend requests. If no listeners are configured for vServer groups or primary/secondary server groups, the frontend requests are forwarded to the ECS instances in the default server group.
        vServer group: If you want to forward different requests to different backend servers, or you want to forward requests based on domain names and URLs, you can specify vServer groups.
        >  If you specify both the default server group and multiple server groups simultaneously, Auto Scaling will add the ECS instances in your scaling group to these server groups concurrently.
        The default weight of each ECS instance as a backend server is 50. If you want to attach a CLB instance to the scaling group that you want to create, make sure that the CLB instance meets the following requirements:
        The CLB instance is in the Active state. You can call the [DescribeLoadBalancers](https://help.aliyun.com/document_detail/2401696.html) operation to query the status of CLB instances.
        Health check must be enabled on all listener ports configured for the CLB instance. Otherwise, the scaling group will fail to be created.
        If you attach Application Load Balancer (ALB) or Network Load Balancer (NLB) server groups to the scaling group that you want to create, Auto Scaling will add the ECS instances in your scaling group to the ALB or NLB server groups to process the access requests forwarded by the corresponding ALB or NLB instances. You can attach multiple ALB or NLB server groups to a scaling group. Make sure that the ALB or NLB server groups belong to the same virtual private cloud (VPC). For more information, see [AttachAlbServerGroups](https://help.aliyun.com/document_detail/266800.html) or [AttachServerGroups](https://help.aliyun.com/document_detail/600559.html).
        If you attach an ApsaraDB RDS instance to the scaling group that you want to create, Auto Scaling will automatically add the private IP addresses of the ECS instances in your scaling group to the IP address whitelist of the ApsaraDB RDS instance. Before you attach an ApsaraDB RDS instance to your scaling group, make sure that the ApsaraDB RDS instance meets the following requirements:
        The ApsaraDB RDS instance is in the Running state. You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/610396.html) state to query the status of ApsaraDB RDS instances.
        The number of IP addresses in the IP address whitelist of the ApsaraDB RDS instance does not reach its upper limit. For more information, see [Configure a whitelist](https://help.aliyun.com/document_detail/43185.html).
        If you set MultiAZPolicy for the scaling group that you want to create to COST_OPTIMIZED, the following rules apply:
        If you use OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, and SpotInstancePools to specify the instance allocation mode under the cost optimization policy, Auto Scaling will prioritize the implementation of the specified instance allocation mode during scale-out events.
        If you do not specify OnDemandBaseCapacity, OnDemandPercentageAboveBaseCapacity, or SpotInstancePools, Auto Scaling will preferentially create instances of the lowest-priced instance type based on the cost optimization policy.
        If you set `Tags.Propagate` to true, the following rules will apply:
        Tags that you add to the scaling group cannot be propagated to existing instances in the scaling group. Tags that you add to the scaling group are propagated to only new instances.
        If you specify instance tags in the scaling configuration that is used to create instances and propagate the tags that you add to the scaling group to the instances, all tags exist at the same time.
        If the tag key that you specify in a scaling configuration and the tag key that you add to the scaling group of the scaling configuration are the same, the tag value that you specify in the scaling configuration is preferentially used.
        
        @param request: CreateScalingGroupRequest
        @return: CreateScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_group_with_options_async(request, runtime)

    def create_scaling_rule_with_options(
        self,
        request: ess_20220222_models.CreateScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScalingRuleResponse:
        """
        @summary Creates a scaling rule. The purpose of a scaling rule varies based on its type. You can use a scaling rule to trigger a scaling activity or adjust the boundary values for a scaling group. You can call the CreateScalingRule operation to create different types of scaling rules based on your business requirements. For example, if your business requires only automatic adjustment of the boundary values for your scaling group, you can call this operation to create a predictive scaling rule.
        
        @description A scaling rule defines the specific scaling action. For example, you can use a scaling rule to define N instances to add or remove. If the execution of a scaling rule causes the total number of Elastic Compute Service (ECS) instances or elastic container instances in the scaling group to drop below the value of MinSize or to exceed the value of MaxSize, Auto Scaling adjusts the number of instances to add or remove, which ensures that the total number of instances stays within the valid range. Take note that Auto Scaling does not adjust the number of instances that you defined in the scaling rule. Examples:
        The maximum number of instances (MaxSize) that can be contained in a scaling group is 3 and the current number of instances (Total Capacity) in the scaling group is 2. In this example, the Add3 scaling rule is created to add three ECS instances to the scaling group. However, after you execute Add3, Auto Scaling adds only one ECS instance to the scaling group. In addition, the number of ECS instances to add in the Add3 scaling rule remains unchanged.
        The minimum number of instances (MinSize) that must be contained in a scaling group is 2 and the current number of instances (Total Capacity) is 3. In this example, the Remove5 scaling rule is created to remove five ECS instances from the scaling group. However, after you execute Remove5, Auto Scaling only removes one ECS instance from the scaling group. In addition, the number of ECS instances to remove in the Remove5 scaling rule remains unchanged.
        Before you call this operation, take note of the following items:
        If you set AdjustmentType to TotalCapacity, the total number of ECS instances or elastic container instances in your scaling group will be adjusted to a specified number when the scaling rule that you create by calling this operation is executed. You must set AdjustmentValue to an integer that is greater than 0.
        If you set AdjustmentType to QuantityChangeInCapacity or PercentChangeInCapacity, a positive value of AdjustmentValue specifies that a specific number of ECS instances or elastic container instances will be added to your scaling group, and a negative value of AdjustmentValue specifies that a specific number of ECS instances or elastic container instances will be removed from the scaling group.
        If you set AdjustmentType to PercentChangeInCapacity, Auto Scaling calculates the number of ECS instances or elastic container instances to add or remove by multiplying the current capacity of the scaling group (Total Capacity) by AdjustmentValue divided by 100, rounding off the result to determine the final adjustment count.
        If you specify a cooldown period for a scaling rule, the cooldown period of the scaling rule takes effect after you execute the scaling rule. If you do not specify a cooldown period for a scaling rule, the value of DefaultCooldown of the scaling group takes effect after you execute the scaling rule.
        You can create only a limited number of scaling rules for a scaling group. For more information, see [Limits](https://help.aliyun.com/document_detail/25863.html).
        The following API operations may use the unique identifier of a scaling rule (ScalingRuleAri) that is returned after you call the CreateScalingRule operation:
        ExecuteScalingRule: You can call this operation to manually execute a scaling rule. In this operation, you can set ScalingRuleAri to the unique identifier of the scaling rule that you want to execute.
        CreateScheduledTask: You can call this operation to create a scheduled task for a scaling rule. In this operation, you can set ScalingRuleAri to the unique identifier of the scaling rule for which you want to create a scheduled task.
        
        @param request: CreateScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.alarm_dimensions):
            query['AlarmDimensions'] = request.alarm_dimensions
        if not UtilClient.is_unset(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not UtilClient.is_unset(request.disable_scale_in):
            query['DisableScaleIn'] = request.disable_scale_in
        if not UtilClient.is_unset(request.estimated_instance_warmup):
            query['EstimatedInstanceWarmup'] = request.estimated_instance_warmup
        if not UtilClient.is_unset(request.initial_max_size):
            query['InitialMaxSize'] = request.initial_max_size
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.predictive_scaling_mode):
            query['PredictiveScalingMode'] = request.predictive_scaling_mode
        if not UtilClient.is_unset(request.predictive_task_buffer_time):
            query['PredictiveTaskBufferTime'] = request.predictive_task_buffer_time
        if not UtilClient.is_unset(request.predictive_value_behavior):
            query['PredictiveValueBehavior'] = request.predictive_value_behavior
        if not UtilClient.is_unset(request.predictive_value_buffer):
            query['PredictiveValueBuffer'] = request.predictive_value_buffer
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scale_in_evaluation_count):
            query['ScaleInEvaluationCount'] = request.scale_in_evaluation_count
        if not UtilClient.is_unset(request.scale_out_evaluation_count):
            query['ScaleOutEvaluationCount'] = request.scale_out_evaluation_count
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        if not UtilClient.is_unset(request.step_adjustments):
            query['StepAdjustments'] = request.step_adjustments
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_rule_with_options_async(
        self,
        request: ess_20220222_models.CreateScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScalingRuleResponse:
        """
        @summary Creates a scaling rule. The purpose of a scaling rule varies based on its type. You can use a scaling rule to trigger a scaling activity or adjust the boundary values for a scaling group. You can call the CreateScalingRule operation to create different types of scaling rules based on your business requirements. For example, if your business requires only automatic adjustment of the boundary values for your scaling group, you can call this operation to create a predictive scaling rule.
        
        @description A scaling rule defines the specific scaling action. For example, you can use a scaling rule to define N instances to add or remove. If the execution of a scaling rule causes the total number of Elastic Compute Service (ECS) instances or elastic container instances in the scaling group to drop below the value of MinSize or to exceed the value of MaxSize, Auto Scaling adjusts the number of instances to add or remove, which ensures that the total number of instances stays within the valid range. Take note that Auto Scaling does not adjust the number of instances that you defined in the scaling rule. Examples:
        The maximum number of instances (MaxSize) that can be contained in a scaling group is 3 and the current number of instances (Total Capacity) in the scaling group is 2. In this example, the Add3 scaling rule is created to add three ECS instances to the scaling group. However, after you execute Add3, Auto Scaling adds only one ECS instance to the scaling group. In addition, the number of ECS instances to add in the Add3 scaling rule remains unchanged.
        The minimum number of instances (MinSize) that must be contained in a scaling group is 2 and the current number of instances (Total Capacity) is 3. In this example, the Remove5 scaling rule is created to remove five ECS instances from the scaling group. However, after you execute Remove5, Auto Scaling only removes one ECS instance from the scaling group. In addition, the number of ECS instances to remove in the Remove5 scaling rule remains unchanged.
        Before you call this operation, take note of the following items:
        If you set AdjustmentType to TotalCapacity, the total number of ECS instances or elastic container instances in your scaling group will be adjusted to a specified number when the scaling rule that you create by calling this operation is executed. You must set AdjustmentValue to an integer that is greater than 0.
        If you set AdjustmentType to QuantityChangeInCapacity or PercentChangeInCapacity, a positive value of AdjustmentValue specifies that a specific number of ECS instances or elastic container instances will be added to your scaling group, and a negative value of AdjustmentValue specifies that a specific number of ECS instances or elastic container instances will be removed from the scaling group.
        If you set AdjustmentType to PercentChangeInCapacity, Auto Scaling calculates the number of ECS instances or elastic container instances to add or remove by multiplying the current capacity of the scaling group (Total Capacity) by AdjustmentValue divided by 100, rounding off the result to determine the final adjustment count.
        If you specify a cooldown period for a scaling rule, the cooldown period of the scaling rule takes effect after you execute the scaling rule. If you do not specify a cooldown period for a scaling rule, the value of DefaultCooldown of the scaling group takes effect after you execute the scaling rule.
        You can create only a limited number of scaling rules for a scaling group. For more information, see [Limits](https://help.aliyun.com/document_detail/25863.html).
        The following API operations may use the unique identifier of a scaling rule (ScalingRuleAri) that is returned after you call the CreateScalingRule operation:
        ExecuteScalingRule: You can call this operation to manually execute a scaling rule. In this operation, you can set ScalingRuleAri to the unique identifier of the scaling rule that you want to execute.
        CreateScheduledTask: You can call this operation to create a scheduled task for a scaling rule. In this operation, you can set ScalingRuleAri to the unique identifier of the scaling rule for which you want to create a scheduled task.
        
        @param request: CreateScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.alarm_dimensions):
            query['AlarmDimensions'] = request.alarm_dimensions
        if not UtilClient.is_unset(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not UtilClient.is_unset(request.disable_scale_in):
            query['DisableScaleIn'] = request.disable_scale_in
        if not UtilClient.is_unset(request.estimated_instance_warmup):
            query['EstimatedInstanceWarmup'] = request.estimated_instance_warmup
        if not UtilClient.is_unset(request.initial_max_size):
            query['InitialMaxSize'] = request.initial_max_size
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.predictive_scaling_mode):
            query['PredictiveScalingMode'] = request.predictive_scaling_mode
        if not UtilClient.is_unset(request.predictive_task_buffer_time):
            query['PredictiveTaskBufferTime'] = request.predictive_task_buffer_time
        if not UtilClient.is_unset(request.predictive_value_behavior):
            query['PredictiveValueBehavior'] = request.predictive_value_behavior
        if not UtilClient.is_unset(request.predictive_value_buffer):
            query['PredictiveValueBuffer'] = request.predictive_value_buffer
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scale_in_evaluation_count):
            query['ScaleInEvaluationCount'] = request.scale_in_evaluation_count
        if not UtilClient.is_unset(request.scale_out_evaluation_count):
            query['ScaleOutEvaluationCount'] = request.scale_out_evaluation_count
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        if not UtilClient.is_unset(request.step_adjustments):
            query['StepAdjustments'] = request.step_adjustments
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scaling_rule(
        self,
        request: ess_20220222_models.CreateScalingRuleRequest,
    ) -> ess_20220222_models.CreateScalingRuleResponse:
        """
        @summary Creates a scaling rule. The purpose of a scaling rule varies based on its type. You can use a scaling rule to trigger a scaling activity or adjust the boundary values for a scaling group. You can call the CreateScalingRule operation to create different types of scaling rules based on your business requirements. For example, if your business requires only automatic adjustment of the boundary values for your scaling group, you can call this operation to create a predictive scaling rule.
        
        @description A scaling rule defines the specific scaling action. For example, you can use a scaling rule to define N instances to add or remove. If the execution of a scaling rule causes the total number of Elastic Compute Service (ECS) instances or elastic container instances in the scaling group to drop below the value of MinSize or to exceed the value of MaxSize, Auto Scaling adjusts the number of instances to add or remove, which ensures that the total number of instances stays within the valid range. Take note that Auto Scaling does not adjust the number of instances that you defined in the scaling rule. Examples:
        The maximum number of instances (MaxSize) that can be contained in a scaling group is 3 and the current number of instances (Total Capacity) in the scaling group is 2. In this example, the Add3 scaling rule is created to add three ECS instances to the scaling group. However, after you execute Add3, Auto Scaling adds only one ECS instance to the scaling group. In addition, the number of ECS instances to add in the Add3 scaling rule remains unchanged.
        The minimum number of instances (MinSize) that must be contained in a scaling group is 2 and the current number of instances (Total Capacity) is 3. In this example, the Remove5 scaling rule is created to remove five ECS instances from the scaling group. However, after you execute Remove5, Auto Scaling only removes one ECS instance from the scaling group. In addition, the number of ECS instances to remove in the Remove5 scaling rule remains unchanged.
        Before you call this operation, take note of the following items:
        If you set AdjustmentType to TotalCapacity, the total number of ECS instances or elastic container instances in your scaling group will be adjusted to a specified number when the scaling rule that you create by calling this operation is executed. You must set AdjustmentValue to an integer that is greater than 0.
        If you set AdjustmentType to QuantityChangeInCapacity or PercentChangeInCapacity, a positive value of AdjustmentValue specifies that a specific number of ECS instances or elastic container instances will be added to your scaling group, and a negative value of AdjustmentValue specifies that a specific number of ECS instances or elastic container instances will be removed from the scaling group.
        If you set AdjustmentType to PercentChangeInCapacity, Auto Scaling calculates the number of ECS instances or elastic container instances to add or remove by multiplying the current capacity of the scaling group (Total Capacity) by AdjustmentValue divided by 100, rounding off the result to determine the final adjustment count.
        If you specify a cooldown period for a scaling rule, the cooldown period of the scaling rule takes effect after you execute the scaling rule. If you do not specify a cooldown period for a scaling rule, the value of DefaultCooldown of the scaling group takes effect after you execute the scaling rule.
        You can create only a limited number of scaling rules for a scaling group. For more information, see [Limits](https://help.aliyun.com/document_detail/25863.html).
        The following API operations may use the unique identifier of a scaling rule (ScalingRuleAri) that is returned after you call the CreateScalingRule operation:
        ExecuteScalingRule: You can call this operation to manually execute a scaling rule. In this operation, you can set ScalingRuleAri to the unique identifier of the scaling rule that you want to execute.
        CreateScheduledTask: You can call this operation to create a scheduled task for a scaling rule. In this operation, you can set ScalingRuleAri to the unique identifier of the scaling rule for which you want to create a scheduled task.
        
        @param request: CreateScalingRuleRequest
        @return: CreateScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_rule_with_options(request, runtime)

    async def create_scaling_rule_async(
        self,
        request: ess_20220222_models.CreateScalingRuleRequest,
    ) -> ess_20220222_models.CreateScalingRuleResponse:
        """
        @summary Creates a scaling rule. The purpose of a scaling rule varies based on its type. You can use a scaling rule to trigger a scaling activity or adjust the boundary values for a scaling group. You can call the CreateScalingRule operation to create different types of scaling rules based on your business requirements. For example, if your business requires only automatic adjustment of the boundary values for your scaling group, you can call this operation to create a predictive scaling rule.
        
        @description A scaling rule defines the specific scaling action. For example, you can use a scaling rule to define N instances to add or remove. If the execution of a scaling rule causes the total number of Elastic Compute Service (ECS) instances or elastic container instances in the scaling group to drop below the value of MinSize or to exceed the value of MaxSize, Auto Scaling adjusts the number of instances to add or remove, which ensures that the total number of instances stays within the valid range. Take note that Auto Scaling does not adjust the number of instances that you defined in the scaling rule. Examples:
        The maximum number of instances (MaxSize) that can be contained in a scaling group is 3 and the current number of instances (Total Capacity) in the scaling group is 2. In this example, the Add3 scaling rule is created to add three ECS instances to the scaling group. However, after you execute Add3, Auto Scaling adds only one ECS instance to the scaling group. In addition, the number of ECS instances to add in the Add3 scaling rule remains unchanged.
        The minimum number of instances (MinSize) that must be contained in a scaling group is 2 and the current number of instances (Total Capacity) is 3. In this example, the Remove5 scaling rule is created to remove five ECS instances from the scaling group. However, after you execute Remove5, Auto Scaling only removes one ECS instance from the scaling group. In addition, the number of ECS instances to remove in the Remove5 scaling rule remains unchanged.
        Before you call this operation, take note of the following items:
        If you set AdjustmentType to TotalCapacity, the total number of ECS instances or elastic container instances in your scaling group will be adjusted to a specified number when the scaling rule that you create by calling this operation is executed. You must set AdjustmentValue to an integer that is greater than 0.
        If you set AdjustmentType to QuantityChangeInCapacity or PercentChangeInCapacity, a positive value of AdjustmentValue specifies that a specific number of ECS instances or elastic container instances will be added to your scaling group, and a negative value of AdjustmentValue specifies that a specific number of ECS instances or elastic container instances will be removed from the scaling group.
        If you set AdjustmentType to PercentChangeInCapacity, Auto Scaling calculates the number of ECS instances or elastic container instances to add or remove by multiplying the current capacity of the scaling group (Total Capacity) by AdjustmentValue divided by 100, rounding off the result to determine the final adjustment count.
        If you specify a cooldown period for a scaling rule, the cooldown period of the scaling rule takes effect after you execute the scaling rule. If you do not specify a cooldown period for a scaling rule, the value of DefaultCooldown of the scaling group takes effect after you execute the scaling rule.
        You can create only a limited number of scaling rules for a scaling group. For more information, see [Limits](https://help.aliyun.com/document_detail/25863.html).
        The following API operations may use the unique identifier of a scaling rule (ScalingRuleAri) that is returned after you call the CreateScalingRule operation:
        ExecuteScalingRule: You can call this operation to manually execute a scaling rule. In this operation, you can set ScalingRuleAri to the unique identifier of the scaling rule that you want to execute.
        CreateScheduledTask: You can call this operation to create a scheduled task for a scaling rule. In this operation, you can set ScalingRuleAri to the unique identifier of the scaling rule for which you want to create a scheduled task.
        
        @param request: CreateScalingRuleRequest
        @return: CreateScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_rule_with_options_async(request, runtime)

    def create_scheduled_task_with_options(
        self,
        request: ess_20220222_models.CreateScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScheduledTaskResponse:
        """
        @summary Creates a scheduled task. A scheduled task is a type of scaling task that enables automatic execution of a specific scaling rule at a specified point in time. You can call the CreateScheduledTask operation to create a scheduled task to implement automatic scaling of computing resources. This ensures your business continuity and minimizes resource costs.
        
        @description    If the scaling rule of a scheduled task fails to be executed due to an ongoing scaling activity in the scaling group or because the scaling group is disabled, the scheduled task is automatically retried during the time window specified by `LaunchExpirationTime`. If the scheduled task still fails after the specified time window ends, the task is automatically skipped.
        If several scheduled tasks concurrently attempt to execute the same scaling rule within a scaling group, the following rules apply:
        Scaling groups with **Expected Number of Instances** configured: The scaling activities incurred by the scheduled tasks are parallel scaling activities. In a proximate time window, Auto Scaling can trigger several scheduled tasks and then execute multiple parallel scaling activities at the same time.
        Scaling groups with **Expected Number of Instances** not configured: The scaling activity incurred by the earliest scheduled task is executed. Considering that a scaling group allows for no more than one ongoing scaling activity simultaneously, other scheduled tasks will spontaneously invoke retries within the time window specified by `LaunchExpirationTime`. Upon completion of the first scheduled task, any retries invoked by other tasks within the time window specified by `LaunchExpirationTime` lead to continuous enforcement of the scaling rule, with each iteration generating a distinct scaling activity.
        You can use one of the following methods to specify the scaling mode:
        ScheduledAction: Specify an existing scaling rule that you want Auto Scaling to execute when the scheduled task is triggered.
        ScalingGroupId: Specify the minimum number, maximum number, or expected number of instances for the scaling group for which you create the scheduled task.
        *\
        *Note** You cannot specify ScheduledAction and ScalingGroupId at the same time.
        
        @param request: CreateScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not UtilClient.is_unset(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not UtilClient.is_unset(request.max_value):
            query['MaxValue'] = request.max_value
        if not UtilClient.is_unset(request.min_value):
            query['MinValue'] = request.min_value
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recurrence_end_time):
            query['RecurrenceEndTime'] = request.recurrence_end_time
        if not UtilClient.is_unset(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not UtilClient.is_unset(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not UtilClient.is_unset(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        if not UtilClient.is_unset(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScheduledTask',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduled_task_with_options_async(
        self,
        request: ess_20220222_models.CreateScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.CreateScheduledTaskResponse:
        """
        @summary Creates a scheduled task. A scheduled task is a type of scaling task that enables automatic execution of a specific scaling rule at a specified point in time. You can call the CreateScheduledTask operation to create a scheduled task to implement automatic scaling of computing resources. This ensures your business continuity and minimizes resource costs.
        
        @description    If the scaling rule of a scheduled task fails to be executed due to an ongoing scaling activity in the scaling group or because the scaling group is disabled, the scheduled task is automatically retried during the time window specified by `LaunchExpirationTime`. If the scheduled task still fails after the specified time window ends, the task is automatically skipped.
        If several scheduled tasks concurrently attempt to execute the same scaling rule within a scaling group, the following rules apply:
        Scaling groups with **Expected Number of Instances** configured: The scaling activities incurred by the scheduled tasks are parallel scaling activities. In a proximate time window, Auto Scaling can trigger several scheduled tasks and then execute multiple parallel scaling activities at the same time.
        Scaling groups with **Expected Number of Instances** not configured: The scaling activity incurred by the earliest scheduled task is executed. Considering that a scaling group allows for no more than one ongoing scaling activity simultaneously, other scheduled tasks will spontaneously invoke retries within the time window specified by `LaunchExpirationTime`. Upon completion of the first scheduled task, any retries invoked by other tasks within the time window specified by `LaunchExpirationTime` lead to continuous enforcement of the scaling rule, with each iteration generating a distinct scaling activity.
        You can use one of the following methods to specify the scaling mode:
        ScheduledAction: Specify an existing scaling rule that you want Auto Scaling to execute when the scheduled task is triggered.
        ScalingGroupId: Specify the minimum number, maximum number, or expected number of instances for the scaling group for which you create the scheduled task.
        *\
        *Note** You cannot specify ScheduledAction and ScalingGroupId at the same time.
        
        @param request: CreateScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not UtilClient.is_unset(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not UtilClient.is_unset(request.max_value):
            query['MaxValue'] = request.max_value
        if not UtilClient.is_unset(request.min_value):
            query['MinValue'] = request.min_value
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recurrence_end_time):
            query['RecurrenceEndTime'] = request.recurrence_end_time
        if not UtilClient.is_unset(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not UtilClient.is_unset(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not UtilClient.is_unset(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        if not UtilClient.is_unset(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScheduledTask',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.CreateScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduled_task(
        self,
        request: ess_20220222_models.CreateScheduledTaskRequest,
    ) -> ess_20220222_models.CreateScheduledTaskResponse:
        """
        @summary Creates a scheduled task. A scheduled task is a type of scaling task that enables automatic execution of a specific scaling rule at a specified point in time. You can call the CreateScheduledTask operation to create a scheduled task to implement automatic scaling of computing resources. This ensures your business continuity and minimizes resource costs.
        
        @description    If the scaling rule of a scheduled task fails to be executed due to an ongoing scaling activity in the scaling group or because the scaling group is disabled, the scheduled task is automatically retried during the time window specified by `LaunchExpirationTime`. If the scheduled task still fails after the specified time window ends, the task is automatically skipped.
        If several scheduled tasks concurrently attempt to execute the same scaling rule within a scaling group, the following rules apply:
        Scaling groups with **Expected Number of Instances** configured: The scaling activities incurred by the scheduled tasks are parallel scaling activities. In a proximate time window, Auto Scaling can trigger several scheduled tasks and then execute multiple parallel scaling activities at the same time.
        Scaling groups with **Expected Number of Instances** not configured: The scaling activity incurred by the earliest scheduled task is executed. Considering that a scaling group allows for no more than one ongoing scaling activity simultaneously, other scheduled tasks will spontaneously invoke retries within the time window specified by `LaunchExpirationTime`. Upon completion of the first scheduled task, any retries invoked by other tasks within the time window specified by `LaunchExpirationTime` lead to continuous enforcement of the scaling rule, with each iteration generating a distinct scaling activity.
        You can use one of the following methods to specify the scaling mode:
        ScheduledAction: Specify an existing scaling rule that you want Auto Scaling to execute when the scheduled task is triggered.
        ScalingGroupId: Specify the minimum number, maximum number, or expected number of instances for the scaling group for which you create the scheduled task.
        *\
        *Note** You cannot specify ScheduledAction and ScalingGroupId at the same time.
        
        @param request: CreateScheduledTaskRequest
        @return: CreateScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scheduled_task_with_options(request, runtime)

    async def create_scheduled_task_async(
        self,
        request: ess_20220222_models.CreateScheduledTaskRequest,
    ) -> ess_20220222_models.CreateScheduledTaskResponse:
        """
        @summary Creates a scheduled task. A scheduled task is a type of scaling task that enables automatic execution of a specific scaling rule at a specified point in time. You can call the CreateScheduledTask operation to create a scheduled task to implement automatic scaling of computing resources. This ensures your business continuity and minimizes resource costs.
        
        @description    If the scaling rule of a scheduled task fails to be executed due to an ongoing scaling activity in the scaling group or because the scaling group is disabled, the scheduled task is automatically retried during the time window specified by `LaunchExpirationTime`. If the scheduled task still fails after the specified time window ends, the task is automatically skipped.
        If several scheduled tasks concurrently attempt to execute the same scaling rule within a scaling group, the following rules apply:
        Scaling groups with **Expected Number of Instances** configured: The scaling activities incurred by the scheduled tasks are parallel scaling activities. In a proximate time window, Auto Scaling can trigger several scheduled tasks and then execute multiple parallel scaling activities at the same time.
        Scaling groups with **Expected Number of Instances** not configured: The scaling activity incurred by the earliest scheduled task is executed. Considering that a scaling group allows for no more than one ongoing scaling activity simultaneously, other scheduled tasks will spontaneously invoke retries within the time window specified by `LaunchExpirationTime`. Upon completion of the first scheduled task, any retries invoked by other tasks within the time window specified by `LaunchExpirationTime` lead to continuous enforcement of the scaling rule, with each iteration generating a distinct scaling activity.
        You can use one of the following methods to specify the scaling mode:
        ScheduledAction: Specify an existing scaling rule that you want Auto Scaling to execute when the scheduled task is triggered.
        ScalingGroupId: Specify the minimum number, maximum number, or expected number of instances for the scaling group for which you create the scheduled task.
        *\
        *Note** You cannot specify ScheduledAction and ScalingGroupId at the same time.
        
        @param request: CreateScheduledTaskRequest
        @return: CreateScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scheduled_task_with_options_async(request, runtime)

    def deactivate_scaling_configuration_with_options(
        self,
        request: ess_20220222_models.DeactivateScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeactivateScalingConfigurationResponse:
        """
        @summary Deactivates a scaling configuration.
        
        @description    You can call this operation to deactivate a scaling configuration only in a disabled scaling group.
        
        @param request: DeactivateScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeactivateScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactivateScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeactivateScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def deactivate_scaling_configuration_with_options_async(
        self,
        request: ess_20220222_models.DeactivateScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeactivateScalingConfigurationResponse:
        """
        @summary Deactivates a scaling configuration.
        
        @description    You can call this operation to deactivate a scaling configuration only in a disabled scaling group.
        
        @param request: DeactivateScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeactivateScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeactivateScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeactivateScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deactivate_scaling_configuration(
        self,
        request: ess_20220222_models.DeactivateScalingConfigurationRequest,
    ) -> ess_20220222_models.DeactivateScalingConfigurationResponse:
        """
        @summary Deactivates a scaling configuration.
        
        @description    You can call this operation to deactivate a scaling configuration only in a disabled scaling group.
        
        @param request: DeactivateScalingConfigurationRequest
        @return: DeactivateScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deactivate_scaling_configuration_with_options(request, runtime)

    async def deactivate_scaling_configuration_async(
        self,
        request: ess_20220222_models.DeactivateScalingConfigurationRequest,
    ) -> ess_20220222_models.DeactivateScalingConfigurationResponse:
        """
        @summary Deactivates a scaling configuration.
        
        @description    You can call this operation to deactivate a scaling configuration only in a disabled scaling group.
        
        @param request: DeactivateScalingConfigurationRequest
        @return: DeactivateScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deactivate_scaling_configuration_with_options_async(request, runtime)

    def delete_alarm_with_options(
        self,
        request: ess_20220222_models.DeleteAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteAlarmResponse:
        """
        @summary Deletes an event-triggered task. If your business pattern is unpredictable or prone to unforeseen traffic spikes, you can create event-triggered tasks by associating CloudMonitor metrics to effectively monitor fluctuations in your business workload. Upon detecting that the criteria for alerts, as specified in event-triggered tasks, are fulfilled, Auto Scaling promptly issues alerts and executes the scaling rules predefined within those tasks. This process occurs within the predefined effective time windows of the tasks, thereby facilitating the automatic increase or decrease of Elastic Compute Service (ECS) instances or elastic container instances within your scaling groups. Ultimately, this mechanism ensures the dynamic optimization of resources based on real-time workload demands. If you no longer need an event-triggered task, you can call the DeleteAlarm operation to delete it.
        
        @param request: DeleteAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alarm_with_options_async(
        self,
        request: ess_20220222_models.DeleteAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteAlarmResponse:
        """
        @summary Deletes an event-triggered task. If your business pattern is unpredictable or prone to unforeseen traffic spikes, you can create event-triggered tasks by associating CloudMonitor metrics to effectively monitor fluctuations in your business workload. Upon detecting that the criteria for alerts, as specified in event-triggered tasks, are fulfilled, Auto Scaling promptly issues alerts and executes the scaling rules predefined within those tasks. This process occurs within the predefined effective time windows of the tasks, thereby facilitating the automatic increase or decrease of Elastic Compute Service (ECS) instances or elastic container instances within your scaling groups. Ultimately, this mechanism ensures the dynamic optimization of resources based on real-time workload demands. If you no longer need an event-triggered task, you can call the DeleteAlarm operation to delete it.
        
        @param request: DeleteAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alarm(
        self,
        request: ess_20220222_models.DeleteAlarmRequest,
    ) -> ess_20220222_models.DeleteAlarmResponse:
        """
        @summary Deletes an event-triggered task. If your business pattern is unpredictable or prone to unforeseen traffic spikes, you can create event-triggered tasks by associating CloudMonitor metrics to effectively monitor fluctuations in your business workload. Upon detecting that the criteria for alerts, as specified in event-triggered tasks, are fulfilled, Auto Scaling promptly issues alerts and executes the scaling rules predefined within those tasks. This process occurs within the predefined effective time windows of the tasks, thereby facilitating the automatic increase or decrease of Elastic Compute Service (ECS) instances or elastic container instances within your scaling groups. Ultimately, this mechanism ensures the dynamic optimization of resources based on real-time workload demands. If you no longer need an event-triggered task, you can call the DeleteAlarm operation to delete it.
        
        @param request: DeleteAlarmRequest
        @return: DeleteAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_alarm_with_options(request, runtime)

    async def delete_alarm_async(
        self,
        request: ess_20220222_models.DeleteAlarmRequest,
    ) -> ess_20220222_models.DeleteAlarmResponse:
        """
        @summary Deletes an event-triggered task. If your business pattern is unpredictable or prone to unforeseen traffic spikes, you can create event-triggered tasks by associating CloudMonitor metrics to effectively monitor fluctuations in your business workload. Upon detecting that the criteria for alerts, as specified in event-triggered tasks, are fulfilled, Auto Scaling promptly issues alerts and executes the scaling rules predefined within those tasks. This process occurs within the predefined effective time windows of the tasks, thereby facilitating the automatic increase or decrease of Elastic Compute Service (ECS) instances or elastic container instances within your scaling groups. Ultimately, this mechanism ensures the dynamic optimization of resources based on real-time workload demands. If you no longer need an event-triggered task, you can call the DeleteAlarm operation to delete it.
        
        @param request: DeleteAlarmRequest
        @return: DeleteAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_alarm_with_options_async(request, runtime)

    def delete_eci_scaling_configuration_with_options(
        self,
        request: ess_20220222_models.DeleteEciScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteEciScalingConfigurationResponse:
        """
        @summary Deletes a scaling configuration of the Elastic Container Instance type. If the scaling configuration of a scaling group is in the Inactive state and the scaling group contains no elastic container instances created from the scaling configuration, you can call the DeleteEciScalingConfiguration operation to delete the scaling configuration to free up the scaling configuration quota.
        
        @description You cannot call this operation to delete a scaling configuration in the following scenarios:
        The scaling configuration is in the Active state.
        The scaling group contains elastic container instances created from the scaling configuration.
        
        @param request: DeleteEciScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_eci_scaling_configuration_with_options_async(
        self,
        request: ess_20220222_models.DeleteEciScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteEciScalingConfigurationResponse:
        """
        @summary Deletes a scaling configuration of the Elastic Container Instance type. If the scaling configuration of a scaling group is in the Inactive state and the scaling group contains no elastic container instances created from the scaling configuration, you can call the DeleteEciScalingConfiguration operation to delete the scaling configuration to free up the scaling configuration quota.
        
        @description You cannot call this operation to delete a scaling configuration in the following scenarios:
        The scaling configuration is in the Active state.
        The scaling group contains elastic container instances created from the scaling configuration.
        
        @param request: DeleteEciScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteEciScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_eci_scaling_configuration(
        self,
        request: ess_20220222_models.DeleteEciScalingConfigurationRequest,
    ) -> ess_20220222_models.DeleteEciScalingConfigurationResponse:
        """
        @summary Deletes a scaling configuration of the Elastic Container Instance type. If the scaling configuration of a scaling group is in the Inactive state and the scaling group contains no elastic container instances created from the scaling configuration, you can call the DeleteEciScalingConfiguration operation to delete the scaling configuration to free up the scaling configuration quota.
        
        @description You cannot call this operation to delete a scaling configuration in the following scenarios:
        The scaling configuration is in the Active state.
        The scaling group contains elastic container instances created from the scaling configuration.
        
        @param request: DeleteEciScalingConfigurationRequest
        @return: DeleteEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_eci_scaling_configuration_with_options(request, runtime)

    async def delete_eci_scaling_configuration_async(
        self,
        request: ess_20220222_models.DeleteEciScalingConfigurationRequest,
    ) -> ess_20220222_models.DeleteEciScalingConfigurationResponse:
        """
        @summary Deletes a scaling configuration of the Elastic Container Instance type. If the scaling configuration of a scaling group is in the Inactive state and the scaling group contains no elastic container instances created from the scaling configuration, you can call the DeleteEciScalingConfiguration operation to delete the scaling configuration to free up the scaling configuration quota.
        
        @description You cannot call this operation to delete a scaling configuration in the following scenarios:
        The scaling configuration is in the Active state.
        The scaling group contains elastic container instances created from the scaling configuration.
        
        @param request: DeleteEciScalingConfigurationRequest
        @return: DeleteEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_eci_scaling_configuration_with_options_async(request, runtime)

    def delete_lifecycle_hook_with_options(
        self,
        request: ess_20220222_models.DeleteLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteLifecycleHookResponse:
        """
        @summary Deletes a lifecycle hook. If you no longer require a lifecycle hook, you can call the DeleteLifecycleHook operation to delete it, which frees up the lifecycle hook quota.
        
        @description If you delete an effective lifecycle hook before its timeout period ends, the instances on which the lifecycle hook takes effect exits the Pending state ahead of schedule. You can use the following methods to delete a lifecycle hook:
        Include `LifecycleHookId` within your request to specify the lifecycle hook that you want to delete. In this case, `ScalingGroupId` and `LifecycleHookName` are ignored.
        Include `ScalingGroupId` and `LifecycleHookName` within your request to specify the lifecycle hook that you want to delete.
        
        @param request: DeleteLifecycleHookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLifecycleHookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteLifecycleHookResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_lifecycle_hook_with_options_async(
        self,
        request: ess_20220222_models.DeleteLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteLifecycleHookResponse:
        """
        @summary Deletes a lifecycle hook. If you no longer require a lifecycle hook, you can call the DeleteLifecycleHook operation to delete it, which frees up the lifecycle hook quota.
        
        @description If you delete an effective lifecycle hook before its timeout period ends, the instances on which the lifecycle hook takes effect exits the Pending state ahead of schedule. You can use the following methods to delete a lifecycle hook:
        Include `LifecycleHookId` within your request to specify the lifecycle hook that you want to delete. In this case, `ScalingGroupId` and `LifecycleHookName` are ignored.
        Include `ScalingGroupId` and `LifecycleHookName` within your request to specify the lifecycle hook that you want to delete.
        
        @param request: DeleteLifecycleHookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLifecycleHookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteLifecycleHookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_lifecycle_hook(
        self,
        request: ess_20220222_models.DeleteLifecycleHookRequest,
    ) -> ess_20220222_models.DeleteLifecycleHookResponse:
        """
        @summary Deletes a lifecycle hook. If you no longer require a lifecycle hook, you can call the DeleteLifecycleHook operation to delete it, which frees up the lifecycle hook quota.
        
        @description If you delete an effective lifecycle hook before its timeout period ends, the instances on which the lifecycle hook takes effect exits the Pending state ahead of schedule. You can use the following methods to delete a lifecycle hook:
        Include `LifecycleHookId` within your request to specify the lifecycle hook that you want to delete. In this case, `ScalingGroupId` and `LifecycleHookName` are ignored.
        Include `ScalingGroupId` and `LifecycleHookName` within your request to specify the lifecycle hook that you want to delete.
        
        @param request: DeleteLifecycleHookRequest
        @return: DeleteLifecycleHookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_lifecycle_hook_with_options(request, runtime)

    async def delete_lifecycle_hook_async(
        self,
        request: ess_20220222_models.DeleteLifecycleHookRequest,
    ) -> ess_20220222_models.DeleteLifecycleHookResponse:
        """
        @summary Deletes a lifecycle hook. If you no longer require a lifecycle hook, you can call the DeleteLifecycleHook operation to delete it, which frees up the lifecycle hook quota.
        
        @description If you delete an effective lifecycle hook before its timeout period ends, the instances on which the lifecycle hook takes effect exits the Pending state ahead of schedule. You can use the following methods to delete a lifecycle hook:
        Include `LifecycleHookId` within your request to specify the lifecycle hook that you want to delete. In this case, `ScalingGroupId` and `LifecycleHookName` are ignored.
        Include `ScalingGroupId` and `LifecycleHookName` within your request to specify the lifecycle hook that you want to delete.
        
        @param request: DeleteLifecycleHookRequest
        @return: DeleteLifecycleHookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_lifecycle_hook_with_options_async(request, runtime)

    def delete_notification_configuration_with_options(
        self,
        request: ess_20220222_models.DeleteNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteNotificationConfigurationResponse:
        """
        @summary Deletes event notification rules. The event notification feature facilitates efficient issue identification and event management by automatically forwarding notifications from Auto Scaling to designated endpoints such as CloudMonitor or Message Service (MNS) topics and queues. If you no longer require an event notification rule, you can call the DeleteNotificationConfiguration operation to delete it.
        
        @param request: DeleteNotificationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNotificationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteNotificationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_notification_configuration_with_options_async(
        self,
        request: ess_20220222_models.DeleteNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteNotificationConfigurationResponse:
        """
        @summary Deletes event notification rules. The event notification feature facilitates efficient issue identification and event management by automatically forwarding notifications from Auto Scaling to designated endpoints such as CloudMonitor or Message Service (MNS) topics and queues. If you no longer require an event notification rule, you can call the DeleteNotificationConfiguration operation to delete it.
        
        @param request: DeleteNotificationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNotificationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteNotificationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_notification_configuration(
        self,
        request: ess_20220222_models.DeleteNotificationConfigurationRequest,
    ) -> ess_20220222_models.DeleteNotificationConfigurationResponse:
        """
        @summary Deletes event notification rules. The event notification feature facilitates efficient issue identification and event management by automatically forwarding notifications from Auto Scaling to designated endpoints such as CloudMonitor or Message Service (MNS) topics and queues. If you no longer require an event notification rule, you can call the DeleteNotificationConfiguration operation to delete it.
        
        @param request: DeleteNotificationConfigurationRequest
        @return: DeleteNotificationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_notification_configuration_with_options(request, runtime)

    async def delete_notification_configuration_async(
        self,
        request: ess_20220222_models.DeleteNotificationConfigurationRequest,
    ) -> ess_20220222_models.DeleteNotificationConfigurationResponse:
        """
        @summary Deletes event notification rules. The event notification feature facilitates efficient issue identification and event management by automatically forwarding notifications from Auto Scaling to designated endpoints such as CloudMonitor or Message Service (MNS) topics and queues. If you no longer require an event notification rule, you can call the DeleteNotificationConfiguration operation to delete it.
        
        @param request: DeleteNotificationConfigurationRequest
        @return: DeleteNotificationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_notification_configuration_with_options_async(request, runtime)

    def delete_scaling_configuration_with_options(
        self,
        request: ess_20220222_models.DeleteScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScalingConfigurationResponse:
        """
        @summary Deletes a scaling configuration that is used to create Elastic Compute Service (ECS) instances.
        
        @description You cannot delete a scaling configuration in one of the following scenarios:
        The scaling configuration in your scaling group is in the Active state.
        The scaling group contains ECS instances that were created based on the scaling configuration.
        
        @param request: DeleteScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_configuration_with_options_async(
        self,
        request: ess_20220222_models.DeleteScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScalingConfigurationResponse:
        """
        @summary Deletes a scaling configuration that is used to create Elastic Compute Service (ECS) instances.
        
        @description You cannot delete a scaling configuration in one of the following scenarios:
        The scaling configuration in your scaling group is in the Active state.
        The scaling group contains ECS instances that were created based on the scaling configuration.
        
        @param request: DeleteScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scaling_configuration(
        self,
        request: ess_20220222_models.DeleteScalingConfigurationRequest,
    ) -> ess_20220222_models.DeleteScalingConfigurationResponse:
        """
        @summary Deletes a scaling configuration that is used to create Elastic Compute Service (ECS) instances.
        
        @description You cannot delete a scaling configuration in one of the following scenarios:
        The scaling configuration in your scaling group is in the Active state.
        The scaling group contains ECS instances that were created based on the scaling configuration.
        
        @param request: DeleteScalingConfigurationRequest
        @return: DeleteScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_configuration_with_options(request, runtime)

    async def delete_scaling_configuration_async(
        self,
        request: ess_20220222_models.DeleteScalingConfigurationRequest,
    ) -> ess_20220222_models.DeleteScalingConfigurationResponse:
        """
        @summary Deletes a scaling configuration that is used to create Elastic Compute Service (ECS) instances.
        
        @description You cannot delete a scaling configuration in one of the following scenarios:
        The scaling configuration in your scaling group is in the Active state.
        The scaling group contains ECS instances that were created based on the scaling configuration.
        
        @param request: DeleteScalingConfigurationRequest
        @return: DeleteScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scaling_configuration_with_options_async(request, runtime)

    def delete_scaling_group_with_options(
        self,
        request: ess_20220222_models.DeleteScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScalingGroupResponse:
        """
        @summary Deletes a scaling group. If you want to enable policy-based automatic addition or removal of instances of a specific type to meet evolving business requirements, you can create scaling groups to manage your computing power with ease. The computing power refers to the instances that provide the computing capability. If you no longer require a scaling group, you can call the DeleteScalingGroup operation to delete it to free up the scaling group quota.
        
        @description Before you call the DeleteScalingGroup operation, take note of the following items:
        If you delete a scaling group, the scaling configurations, scaling rules, scaling activities, and scaling requests related to the scaling group are also deleted.
        If you delete a scaling group, the scheduled tasks and event-triggered tasks of the scaling group are not deleted. The Server Load Balancer (SLB) instances and ApsaraDB RDS instances that are attached to the scaling group are also not deleted.
        If the scaling group that you want to delete contains ECS instances or elastic container instances that are in the In Service state, Auto Scaling stops the instances and then removes all manually added instances from the scaling group or releases all automatically created instances in the scaling group before the scaling group is deleted.
        *\
        *Note** Before you delete a scaling group, make sure that the Deletion Protection feature is disabled. If you have enabled the Deletion Protection feature for a scaling group, disable the feature on the Modify Scaling Group page before you delete the scaling group.
        If you do not disable the Deletion Protection feature for a scaling group, you cannot delete the scaling group by using the Auto Scaling console or calling this operation. The Deletion Protection feature is an effective measure to safeguard scaling groups against unintended deletion.
        Prior to deleting a scaling group, make sure that your ECS instances within the scaling group are safeguarded against unintended release. Even if you have already enabled the Release Protection feature for the ECS instances, you must manually put these ECS instances into the Protected state. Doing so guarantees that the ECS instances will not be forcibly released during the deletion process of the scaling group, providing an extra layer of security.
        *\
        *Note** Before you delete a scaling group, we recommend that you enable the Deletion Protection feature for ECS instances that you want to retain. This action guarantees that the ECS instances are not forcibly released after you delete the scaling group. For more information, see [SetInstancesProtection](https://help.aliyun.com/document_detail/459342.html).
        
        @param request: DeleteScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete):
            query['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_group_with_options_async(
        self,
        request: ess_20220222_models.DeleteScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScalingGroupResponse:
        """
        @summary Deletes a scaling group. If you want to enable policy-based automatic addition or removal of instances of a specific type to meet evolving business requirements, you can create scaling groups to manage your computing power with ease. The computing power refers to the instances that provide the computing capability. If you no longer require a scaling group, you can call the DeleteScalingGroup operation to delete it to free up the scaling group quota.
        
        @description Before you call the DeleteScalingGroup operation, take note of the following items:
        If you delete a scaling group, the scaling configurations, scaling rules, scaling activities, and scaling requests related to the scaling group are also deleted.
        If you delete a scaling group, the scheduled tasks and event-triggered tasks of the scaling group are not deleted. The Server Load Balancer (SLB) instances and ApsaraDB RDS instances that are attached to the scaling group are also not deleted.
        If the scaling group that you want to delete contains ECS instances or elastic container instances that are in the In Service state, Auto Scaling stops the instances and then removes all manually added instances from the scaling group or releases all automatically created instances in the scaling group before the scaling group is deleted.
        *\
        *Note** Before you delete a scaling group, make sure that the Deletion Protection feature is disabled. If you have enabled the Deletion Protection feature for a scaling group, disable the feature on the Modify Scaling Group page before you delete the scaling group.
        If you do not disable the Deletion Protection feature for a scaling group, you cannot delete the scaling group by using the Auto Scaling console or calling this operation. The Deletion Protection feature is an effective measure to safeguard scaling groups against unintended deletion.
        Prior to deleting a scaling group, make sure that your ECS instances within the scaling group are safeguarded against unintended release. Even if you have already enabled the Release Protection feature for the ECS instances, you must manually put these ECS instances into the Protected state. Doing so guarantees that the ECS instances will not be forcibly released during the deletion process of the scaling group, providing an extra layer of security.
        *\
        *Note** Before you delete a scaling group, we recommend that you enable the Deletion Protection feature for ECS instances that you want to retain. This action guarantees that the ECS instances are not forcibly released after you delete the scaling group. For more information, see [SetInstancesProtection](https://help.aliyun.com/document_detail/459342.html).
        
        @param request: DeleteScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete):
            query['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scaling_group(
        self,
        request: ess_20220222_models.DeleteScalingGroupRequest,
    ) -> ess_20220222_models.DeleteScalingGroupResponse:
        """
        @summary Deletes a scaling group. If you want to enable policy-based automatic addition or removal of instances of a specific type to meet evolving business requirements, you can create scaling groups to manage your computing power with ease. The computing power refers to the instances that provide the computing capability. If you no longer require a scaling group, you can call the DeleteScalingGroup operation to delete it to free up the scaling group quota.
        
        @description Before you call the DeleteScalingGroup operation, take note of the following items:
        If you delete a scaling group, the scaling configurations, scaling rules, scaling activities, and scaling requests related to the scaling group are also deleted.
        If you delete a scaling group, the scheduled tasks and event-triggered tasks of the scaling group are not deleted. The Server Load Balancer (SLB) instances and ApsaraDB RDS instances that are attached to the scaling group are also not deleted.
        If the scaling group that you want to delete contains ECS instances or elastic container instances that are in the In Service state, Auto Scaling stops the instances and then removes all manually added instances from the scaling group or releases all automatically created instances in the scaling group before the scaling group is deleted.
        *\
        *Note** Before you delete a scaling group, make sure that the Deletion Protection feature is disabled. If you have enabled the Deletion Protection feature for a scaling group, disable the feature on the Modify Scaling Group page before you delete the scaling group.
        If you do not disable the Deletion Protection feature for a scaling group, you cannot delete the scaling group by using the Auto Scaling console or calling this operation. The Deletion Protection feature is an effective measure to safeguard scaling groups against unintended deletion.
        Prior to deleting a scaling group, make sure that your ECS instances within the scaling group are safeguarded against unintended release. Even if you have already enabled the Release Protection feature for the ECS instances, you must manually put these ECS instances into the Protected state. Doing so guarantees that the ECS instances will not be forcibly released during the deletion process of the scaling group, providing an extra layer of security.
        *\
        *Note** Before you delete a scaling group, we recommend that you enable the Deletion Protection feature for ECS instances that you want to retain. This action guarantees that the ECS instances are not forcibly released after you delete the scaling group. For more information, see [SetInstancesProtection](https://help.aliyun.com/document_detail/459342.html).
        
        @param request: DeleteScalingGroupRequest
        @return: DeleteScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_group_with_options(request, runtime)

    async def delete_scaling_group_async(
        self,
        request: ess_20220222_models.DeleteScalingGroupRequest,
    ) -> ess_20220222_models.DeleteScalingGroupResponse:
        """
        @summary Deletes a scaling group. If you want to enable policy-based automatic addition or removal of instances of a specific type to meet evolving business requirements, you can create scaling groups to manage your computing power with ease. The computing power refers to the instances that provide the computing capability. If you no longer require a scaling group, you can call the DeleteScalingGroup operation to delete it to free up the scaling group quota.
        
        @description Before you call the DeleteScalingGroup operation, take note of the following items:
        If you delete a scaling group, the scaling configurations, scaling rules, scaling activities, and scaling requests related to the scaling group are also deleted.
        If you delete a scaling group, the scheduled tasks and event-triggered tasks of the scaling group are not deleted. The Server Load Balancer (SLB) instances and ApsaraDB RDS instances that are attached to the scaling group are also not deleted.
        If the scaling group that you want to delete contains ECS instances or elastic container instances that are in the In Service state, Auto Scaling stops the instances and then removes all manually added instances from the scaling group or releases all automatically created instances in the scaling group before the scaling group is deleted.
        *\
        *Note** Before you delete a scaling group, make sure that the Deletion Protection feature is disabled. If you have enabled the Deletion Protection feature for a scaling group, disable the feature on the Modify Scaling Group page before you delete the scaling group.
        If you do not disable the Deletion Protection feature for a scaling group, you cannot delete the scaling group by using the Auto Scaling console or calling this operation. The Deletion Protection feature is an effective measure to safeguard scaling groups against unintended deletion.
        Prior to deleting a scaling group, make sure that your ECS instances within the scaling group are safeguarded against unintended release. Even if you have already enabled the Release Protection feature for the ECS instances, you must manually put these ECS instances into the Protected state. Doing so guarantees that the ECS instances will not be forcibly released during the deletion process of the scaling group, providing an extra layer of security.
        *\
        *Note** Before you delete a scaling group, we recommend that you enable the Deletion Protection feature for ECS instances that you want to retain. This action guarantees that the ECS instances are not forcibly released after you delete the scaling group. For more information, see [SetInstancesProtection](https://help.aliyun.com/document_detail/459342.html).
        
        @param request: DeleteScalingGroupRequest
        @return: DeleteScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scaling_group_with_options_async(request, runtime)

    def delete_scaling_rule_with_options(
        self,
        request: ess_20220222_models.DeleteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScalingRuleResponse:
        """
        @summary Deletes a scaling rule.
        
        @param request: DeleteScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_rule_with_options_async(
        self,
        request: ess_20220222_models.DeleteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScalingRuleResponse:
        """
        @summary Deletes a scaling rule.
        
        @param request: DeleteScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scaling_rule(
        self,
        request: ess_20220222_models.DeleteScalingRuleRequest,
    ) -> ess_20220222_models.DeleteScalingRuleResponse:
        """
        @summary Deletes a scaling rule.
        
        @param request: DeleteScalingRuleRequest
        @return: DeleteScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_rule_with_options(request, runtime)

    async def delete_scaling_rule_async(
        self,
        request: ess_20220222_models.DeleteScalingRuleRequest,
    ) -> ess_20220222_models.DeleteScalingRuleResponse:
        """
        @summary Deletes a scaling rule.
        
        @param request: DeleteScalingRuleRequest
        @return: DeleteScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scaling_rule_with_options_async(request, runtime)

    def delete_scheduled_task_with_options(
        self,
        request: ess_20220222_models.DeleteScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScheduledTaskResponse:
        """
        @summary Deletes scheduled tasks. For workloads with predictable patterns, you can create scheduled tasks to align with your business requirements and optimize resource utilization for cost savings. These tasks automatically ensure that sufficient computing resources are provisioned in anticipation of peak hours and efficiently release unused resources during off-peak hours, thereby streamlining operational efficiency and reducing expenses. If you no longer require a scheduled task, you can call the DeleteScheduledTask operation to delete it.
        
        @param request: DeleteScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScheduledTask',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheduled_task_with_options_async(
        self,
        request: ess_20220222_models.DeleteScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DeleteScheduledTaskResponse:
        """
        @summary Deletes scheduled tasks. For workloads with predictable patterns, you can create scheduled tasks to align with your business requirements and optimize resource utilization for cost savings. These tasks automatically ensure that sufficient computing resources are provisioned in anticipation of peak hours and efficiently release unused resources during off-peak hours, thereby streamlining operational efficiency and reducing expenses. If you no longer require a scheduled task, you can call the DeleteScheduledTask operation to delete it.
        
        @param request: DeleteScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScheduledTask',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DeleteScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheduled_task(
        self,
        request: ess_20220222_models.DeleteScheduledTaskRequest,
    ) -> ess_20220222_models.DeleteScheduledTaskResponse:
        """
        @summary Deletes scheduled tasks. For workloads with predictable patterns, you can create scheduled tasks to align with your business requirements and optimize resource utilization for cost savings. These tasks automatically ensure that sufficient computing resources are provisioned in anticipation of peak hours and efficiently release unused resources during off-peak hours, thereby streamlining operational efficiency and reducing expenses. If you no longer require a scheduled task, you can call the DeleteScheduledTask operation to delete it.
        
        @param request: DeleteScheduledTaskRequest
        @return: DeleteScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scheduled_task_with_options(request, runtime)

    async def delete_scheduled_task_async(
        self,
        request: ess_20220222_models.DeleteScheduledTaskRequest,
    ) -> ess_20220222_models.DeleteScheduledTaskResponse:
        """
        @summary Deletes scheduled tasks. For workloads with predictable patterns, you can create scheduled tasks to align with your business requirements and optimize resource utilization for cost savings. These tasks automatically ensure that sufficient computing resources are provisioned in anticipation of peak hours and efficiently release unused resources during off-peak hours, thereby streamlining operational efficiency and reducing expenses. If you no longer require a scheduled task, you can call the DeleteScheduledTask operation to delete it.
        
        @param request: DeleteScheduledTaskRequest
        @return: DeleteScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scheduled_task_with_options_async(request, runtime)

    def describe_alarms_with_options(
        self,
        request: ess_20220222_models.DescribeAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeAlarmsResponse:
        """
        @summary Queries event-triggered tasks. You can call the DescribeAlarms operation to learn about the configurations of event-triggered tasks and keep updated on monitoring data changes. This helps you troubleshoot system resource issues at the earliest opportunity and ensures system stability and reliability.
        
        @param request: DescribeAlarmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlarmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarms',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeAlarmsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alarms_with_options_async(
        self,
        request: ess_20220222_models.DescribeAlarmsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeAlarmsResponse:
        """
        @summary Queries event-triggered tasks. You can call the DescribeAlarms operation to learn about the configurations of event-triggered tasks and keep updated on monitoring data changes. This helps you troubleshoot system resource issues at the earliest opportunity and ensures system stability and reliability.
        
        @param request: DescribeAlarmsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlarmsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlarms',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeAlarmsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alarms(
        self,
        request: ess_20220222_models.DescribeAlarmsRequest,
    ) -> ess_20220222_models.DescribeAlarmsResponse:
        """
        @summary Queries event-triggered tasks. You can call the DescribeAlarms operation to learn about the configurations of event-triggered tasks and keep updated on monitoring data changes. This helps you troubleshoot system resource issues at the earliest opportunity and ensures system stability and reliability.
        
        @param request: DescribeAlarmsRequest
        @return: DescribeAlarmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alarms_with_options(request, runtime)

    async def describe_alarms_async(
        self,
        request: ess_20220222_models.DescribeAlarmsRequest,
    ) -> ess_20220222_models.DescribeAlarmsResponse:
        """
        @summary Queries event-triggered tasks. You can call the DescribeAlarms operation to learn about the configurations of event-triggered tasks and keep updated on monitoring data changes. This helps you troubleshoot system resource issues at the earliest opportunity and ensures system stability and reliability.
        
        @param request: DescribeAlarmsRequest
        @return: DescribeAlarmsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alarms_with_options_async(request, runtime)

    def describe_alert_configuration_with_options(
        self,
        request: ess_20220222_models.DescribeAlertConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeAlertConfigurationResponse:
        """
        @summary Queries the status of scaling activities that prompt text message or email notifications.
        
        @param request: DescribeAlertConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeAlertConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_configuration_with_options_async(
        self,
        request: ess_20220222_models.DescribeAlertConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeAlertConfigurationResponse:
        """
        @summary Queries the status of scaling activities that prompt text message or email notifications.
        
        @param request: DescribeAlertConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAlertConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAlertConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeAlertConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_configuration(
        self,
        request: ess_20220222_models.DescribeAlertConfigurationRequest,
    ) -> ess_20220222_models.DescribeAlertConfigurationResponse:
        """
        @summary Queries the status of scaling activities that prompt text message or email notifications.
        
        @param request: DescribeAlertConfigurationRequest
        @return: DescribeAlertConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_configuration_with_options(request, runtime)

    async def describe_alert_configuration_async(
        self,
        request: ess_20220222_models.DescribeAlertConfigurationRequest,
    ) -> ess_20220222_models.DescribeAlertConfigurationResponse:
        """
        @summary Queries the status of scaling activities that prompt text message or email notifications.
        
        @param request: DescribeAlertConfigurationRequest
        @return: DescribeAlertConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_configuration_with_options_async(request, runtime)

    def describe_eci_scaling_configuration_detail_with_options(
        self,
        request: ess_20220222_models.DescribeEciScalingConfigurationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeEciScalingConfigurationDetailResponse:
        """
        @summary Queries the details of a scaling configuration. You can query a scaling configuration by its ID to learn about its details such as the temporary storage size, number of IPv6 addresses, and bandwidth of the elastic IP address (EIP). The scaling configuration details can be obtained as a YAML file.
        
        @param request: DescribeEciScalingConfigurationDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEciScalingConfigurationDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_format):
            query['OutputFormat'] = request.output_format
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEciScalingConfigurationDetail',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeEciScalingConfigurationDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_eci_scaling_configuration_detail_with_options_async(
        self,
        request: ess_20220222_models.DescribeEciScalingConfigurationDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeEciScalingConfigurationDetailResponse:
        """
        @summary Queries the details of a scaling configuration. You can query a scaling configuration by its ID to learn about its details such as the temporary storage size, number of IPv6 addresses, and bandwidth of the elastic IP address (EIP). The scaling configuration details can be obtained as a YAML file.
        
        @param request: DescribeEciScalingConfigurationDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEciScalingConfigurationDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_format):
            query['OutputFormat'] = request.output_format
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEciScalingConfigurationDetail',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeEciScalingConfigurationDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_eci_scaling_configuration_detail(
        self,
        request: ess_20220222_models.DescribeEciScalingConfigurationDetailRequest,
    ) -> ess_20220222_models.DescribeEciScalingConfigurationDetailResponse:
        """
        @summary Queries the details of a scaling configuration. You can query a scaling configuration by its ID to learn about its details such as the temporary storage size, number of IPv6 addresses, and bandwidth of the elastic IP address (EIP). The scaling configuration details can be obtained as a YAML file.
        
        @param request: DescribeEciScalingConfigurationDetailRequest
        @return: DescribeEciScalingConfigurationDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_eci_scaling_configuration_detail_with_options(request, runtime)

    async def describe_eci_scaling_configuration_detail_async(
        self,
        request: ess_20220222_models.DescribeEciScalingConfigurationDetailRequest,
    ) -> ess_20220222_models.DescribeEciScalingConfigurationDetailResponse:
        """
        @summary Queries the details of a scaling configuration. You can query a scaling configuration by its ID to learn about its details such as the temporary storage size, number of IPv6 addresses, and bandwidth of the elastic IP address (EIP). The scaling configuration details can be obtained as a YAML file.
        
        @param request: DescribeEciScalingConfigurationDetailRequest
        @return: DescribeEciScalingConfigurationDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_eci_scaling_configuration_detail_with_options_async(request, runtime)

    def describe_eci_scaling_configurations_with_options(
        self,
        request: ess_20220222_models.DescribeEciScalingConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeEciScalingConfigurationsResponse:
        """
        @summary Queries scaling configurations of the Elastic Container Instance type to learn the scaling configuration details. This allows you to select an appropriate template when you create elastic container instances.
        
        @param request: DescribeEciScalingConfigurationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEciScalingConfigurationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_configuration_ids):
            query['ScalingConfigurationIds'] = request.scaling_configuration_ids
        if not UtilClient.is_unset(request.scaling_configuration_names):
            query['ScalingConfigurationNames'] = request.scaling_configuration_names
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEciScalingConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeEciScalingConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_eci_scaling_configurations_with_options_async(
        self,
        request: ess_20220222_models.DescribeEciScalingConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeEciScalingConfigurationsResponse:
        """
        @summary Queries scaling configurations of the Elastic Container Instance type to learn the scaling configuration details. This allows you to select an appropriate template when you create elastic container instances.
        
        @param request: DescribeEciScalingConfigurationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEciScalingConfigurationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_configuration_ids):
            query['ScalingConfigurationIds'] = request.scaling_configuration_ids
        if not UtilClient.is_unset(request.scaling_configuration_names):
            query['ScalingConfigurationNames'] = request.scaling_configuration_names
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEciScalingConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeEciScalingConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_eci_scaling_configurations(
        self,
        request: ess_20220222_models.DescribeEciScalingConfigurationsRequest,
    ) -> ess_20220222_models.DescribeEciScalingConfigurationsResponse:
        """
        @summary Queries scaling configurations of the Elastic Container Instance type to learn the scaling configuration details. This allows you to select an appropriate template when you create elastic container instances.
        
        @param request: DescribeEciScalingConfigurationsRequest
        @return: DescribeEciScalingConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_eci_scaling_configurations_with_options(request, runtime)

    async def describe_eci_scaling_configurations_async(
        self,
        request: ess_20220222_models.DescribeEciScalingConfigurationsRequest,
    ) -> ess_20220222_models.DescribeEciScalingConfigurationsResponse:
        """
        @summary Queries scaling configurations of the Elastic Container Instance type to learn the scaling configuration details. This allows you to select an appropriate template when you create elastic container instances.
        
        @param request: DescribeEciScalingConfigurationsRequest
        @return: DescribeEciScalingConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_eci_scaling_configurations_with_options_async(request, runtime)

    def describe_lifecycle_actions_with_options(
        self,
        request: ess_20220222_models.DescribeLifecycleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeLifecycleActionsResponse:
        """
        @summary Queries the details of a lifecycle hook. If you want to query the details of a lifecycle hook, you can call the DescribeLifecycleActions operation. For example, you can query the execution status and ID of a lifecycle hook, along with the Elastic Compute Service (ECS) instances on which the lifecycle hook takes effect. When you call this operation, you can specify parameters such as ScalingActivityId, LifecycleActionToken, and MaxResults to query the details of a lifecycle hook.
        
        @description If a scaling activity is executed and a lifecycle hook is created for the scaling activity, the lifecycle hook triggers a lifecycle action. A lifecycle action can be in one of the following states:
        If a lifecycle action is in the Pending state, Elastic Compute Service (ECS) instances are waiting to be added to a scaling group or waiting to be removed from a scaling group.
        If a lifecycle action is in the Timeout state, the lifecycle hook that triggers the lifecycle action expires and ECS instances are added to or removed from a scaling group.
        If a lifecycle action is in the Completed state, you manually end the lifecycle hook that triggers the lifecycle action ahead of schedule.
        If you do not specify the action to perform, such as execute a specific OOS template, after a lifecycle hook ends, you can call this operation to obtain the token of the lifecycle action that corresponds to the lifecycle hook. Then, you can specify a custom action to perform after the lifecycle hook ends.
        
        @param request: DescribeLifecycleActionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLifecycleActionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_action_status):
            query['LifecycleActionStatus'] = request.lifecycle_action_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecycleActions',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLifecycleActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lifecycle_actions_with_options_async(
        self,
        request: ess_20220222_models.DescribeLifecycleActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeLifecycleActionsResponse:
        """
        @summary Queries the details of a lifecycle hook. If you want to query the details of a lifecycle hook, you can call the DescribeLifecycleActions operation. For example, you can query the execution status and ID of a lifecycle hook, along with the Elastic Compute Service (ECS) instances on which the lifecycle hook takes effect. When you call this operation, you can specify parameters such as ScalingActivityId, LifecycleActionToken, and MaxResults to query the details of a lifecycle hook.
        
        @description If a scaling activity is executed and a lifecycle hook is created for the scaling activity, the lifecycle hook triggers a lifecycle action. A lifecycle action can be in one of the following states:
        If a lifecycle action is in the Pending state, Elastic Compute Service (ECS) instances are waiting to be added to a scaling group or waiting to be removed from a scaling group.
        If a lifecycle action is in the Timeout state, the lifecycle hook that triggers the lifecycle action expires and ECS instances are added to or removed from a scaling group.
        If a lifecycle action is in the Completed state, you manually end the lifecycle hook that triggers the lifecycle action ahead of schedule.
        If you do not specify the action to perform, such as execute a specific OOS template, after a lifecycle hook ends, you can call this operation to obtain the token of the lifecycle action that corresponds to the lifecycle hook. Then, you can specify a custom action to perform after the lifecycle hook ends.
        
        @param request: DescribeLifecycleActionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLifecycleActionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_action_status):
            query['LifecycleActionStatus'] = request.lifecycle_action_status
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecycleActions',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLifecycleActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lifecycle_actions(
        self,
        request: ess_20220222_models.DescribeLifecycleActionsRequest,
    ) -> ess_20220222_models.DescribeLifecycleActionsResponse:
        """
        @summary Queries the details of a lifecycle hook. If you want to query the details of a lifecycle hook, you can call the DescribeLifecycleActions operation. For example, you can query the execution status and ID of a lifecycle hook, along with the Elastic Compute Service (ECS) instances on which the lifecycle hook takes effect. When you call this operation, you can specify parameters such as ScalingActivityId, LifecycleActionToken, and MaxResults to query the details of a lifecycle hook.
        
        @description If a scaling activity is executed and a lifecycle hook is created for the scaling activity, the lifecycle hook triggers a lifecycle action. A lifecycle action can be in one of the following states:
        If a lifecycle action is in the Pending state, Elastic Compute Service (ECS) instances are waiting to be added to a scaling group or waiting to be removed from a scaling group.
        If a lifecycle action is in the Timeout state, the lifecycle hook that triggers the lifecycle action expires and ECS instances are added to or removed from a scaling group.
        If a lifecycle action is in the Completed state, you manually end the lifecycle hook that triggers the lifecycle action ahead of schedule.
        If you do not specify the action to perform, such as execute a specific OOS template, after a lifecycle hook ends, you can call this operation to obtain the token of the lifecycle action that corresponds to the lifecycle hook. Then, you can specify a custom action to perform after the lifecycle hook ends.
        
        @param request: DescribeLifecycleActionsRequest
        @return: DescribeLifecycleActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_lifecycle_actions_with_options(request, runtime)

    async def describe_lifecycle_actions_async(
        self,
        request: ess_20220222_models.DescribeLifecycleActionsRequest,
    ) -> ess_20220222_models.DescribeLifecycleActionsResponse:
        """
        @summary Queries the details of a lifecycle hook. If you want to query the details of a lifecycle hook, you can call the DescribeLifecycleActions operation. For example, you can query the execution status and ID of a lifecycle hook, along with the Elastic Compute Service (ECS) instances on which the lifecycle hook takes effect. When you call this operation, you can specify parameters such as ScalingActivityId, LifecycleActionToken, and MaxResults to query the details of a lifecycle hook.
        
        @description If a scaling activity is executed and a lifecycle hook is created for the scaling activity, the lifecycle hook triggers a lifecycle action. A lifecycle action can be in one of the following states:
        If a lifecycle action is in the Pending state, Elastic Compute Service (ECS) instances are waiting to be added to a scaling group or waiting to be removed from a scaling group.
        If a lifecycle action is in the Timeout state, the lifecycle hook that triggers the lifecycle action expires and ECS instances are added to or removed from a scaling group.
        If a lifecycle action is in the Completed state, you manually end the lifecycle hook that triggers the lifecycle action ahead of schedule.
        If you do not specify the action to perform, such as execute a specific OOS template, after a lifecycle hook ends, you can call this operation to obtain the token of the lifecycle action that corresponds to the lifecycle hook. Then, you can specify a custom action to perform after the lifecycle hook ends.
        
        @param request: DescribeLifecycleActionsRequest
        @return: DescribeLifecycleActionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_lifecycle_actions_with_options_async(request, runtime)

    def describe_lifecycle_hooks_with_options(
        self,
        request: ess_20220222_models.DescribeLifecycleHooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeLifecycleHooksResponse:
        """
        @summary Queries lifecycle hooks. If you want to check whether the configurations of your lifecycle hooks are correct or you want to query the details of multiple lifecycle hooks at the same time, you can call the DescribeLifecycleHooks operation. You can specify lifecycle hook IDs or scaling group IDs when you call this operation. This operation returns details such as the default actions, scaling activities, Alibaba Cloud Resource Names (ARNs) of notification recipients, and timeout periods of lifecycle hooks.
        
        @description You can use one of the following methods to query lifecycle hooks:
        Specify a list of lifecycle hook IDs by using the LifecycleHookIds parameter. In this case, you do not need to specify the ScalingGroupId and LifecycleHookName parameters.
        Specify the scaling group ID by using the ScalingGroupId parameter.
        Specify the scaling group ID by using the ScalingGroupId parameter and the lifecycle hook name by using the LifecycleHookName parameter at the same time.
        
        @param request: DescribeLifecycleHooksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLifecycleHooksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_hook_ids):
            query['LifecycleHookIds'] = request.lifecycle_hook_ids
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecycleHooks',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLifecycleHooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_lifecycle_hooks_with_options_async(
        self,
        request: ess_20220222_models.DescribeLifecycleHooksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeLifecycleHooksResponse:
        """
        @summary Queries lifecycle hooks. If you want to check whether the configurations of your lifecycle hooks are correct or you want to query the details of multiple lifecycle hooks at the same time, you can call the DescribeLifecycleHooks operation. You can specify lifecycle hook IDs or scaling group IDs when you call this operation. This operation returns details such as the default actions, scaling activities, Alibaba Cloud Resource Names (ARNs) of notification recipients, and timeout periods of lifecycle hooks.
        
        @description You can use one of the following methods to query lifecycle hooks:
        Specify a list of lifecycle hook IDs by using the LifecycleHookIds parameter. In this case, you do not need to specify the ScalingGroupId and LifecycleHookName parameters.
        Specify the scaling group ID by using the ScalingGroupId parameter.
        Specify the scaling group ID by using the ScalingGroupId parameter and the lifecycle hook name by using the LifecycleHookName parameter at the same time.
        
        @param request: DescribeLifecycleHooksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLifecycleHooksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lifecycle_hook_ids):
            query['LifecycleHookIds'] = request.lifecycle_hook_ids
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLifecycleHooks',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLifecycleHooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_lifecycle_hooks(
        self,
        request: ess_20220222_models.DescribeLifecycleHooksRequest,
    ) -> ess_20220222_models.DescribeLifecycleHooksResponse:
        """
        @summary Queries lifecycle hooks. If you want to check whether the configurations of your lifecycle hooks are correct or you want to query the details of multiple lifecycle hooks at the same time, you can call the DescribeLifecycleHooks operation. You can specify lifecycle hook IDs or scaling group IDs when you call this operation. This operation returns details such as the default actions, scaling activities, Alibaba Cloud Resource Names (ARNs) of notification recipients, and timeout periods of lifecycle hooks.
        
        @description You can use one of the following methods to query lifecycle hooks:
        Specify a list of lifecycle hook IDs by using the LifecycleHookIds parameter. In this case, you do not need to specify the ScalingGroupId and LifecycleHookName parameters.
        Specify the scaling group ID by using the ScalingGroupId parameter.
        Specify the scaling group ID by using the ScalingGroupId parameter and the lifecycle hook name by using the LifecycleHookName parameter at the same time.
        
        @param request: DescribeLifecycleHooksRequest
        @return: DescribeLifecycleHooksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_lifecycle_hooks_with_options(request, runtime)

    async def describe_lifecycle_hooks_async(
        self,
        request: ess_20220222_models.DescribeLifecycleHooksRequest,
    ) -> ess_20220222_models.DescribeLifecycleHooksResponse:
        """
        @summary Queries lifecycle hooks. If you want to check whether the configurations of your lifecycle hooks are correct or you want to query the details of multiple lifecycle hooks at the same time, you can call the DescribeLifecycleHooks operation. You can specify lifecycle hook IDs or scaling group IDs when you call this operation. This operation returns details such as the default actions, scaling activities, Alibaba Cloud Resource Names (ARNs) of notification recipients, and timeout periods of lifecycle hooks.
        
        @description You can use one of the following methods to query lifecycle hooks:
        Specify a list of lifecycle hook IDs by using the LifecycleHookIds parameter. In this case, you do not need to specify the ScalingGroupId and LifecycleHookName parameters.
        Specify the scaling group ID by using the ScalingGroupId parameter.
        Specify the scaling group ID by using the ScalingGroupId parameter and the lifecycle hook name by using the LifecycleHookName parameter at the same time.
        
        @param request: DescribeLifecycleHooksRequest
        @return: DescribeLifecycleHooksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_lifecycle_hooks_with_options_async(request, runtime)

    def describe_limitation_with_options(
        self,
        request: ess_20220222_models.DescribeLimitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeLimitationResponse:
        """
        @summary Queries resource quotas. You can call the DescribeLimitation operation to query the upper limits on resources such as scheduled tasks that can be created in a scaling group, load balancers that can be attached to a scaling group, instances that can be contained in a scaling group, and scaling configurations that can be created in a scaling group.
        
        @param request: DescribeLimitationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLimitationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLimitation',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLimitationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_limitation_with_options_async(
        self,
        request: ess_20220222_models.DescribeLimitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeLimitationResponse:
        """
        @summary Queries resource quotas. You can call the DescribeLimitation operation to query the upper limits on resources such as scheduled tasks that can be created in a scaling group, load balancers that can be attached to a scaling group, instances that can be contained in a scaling group, and scaling configurations that can be created in a scaling group.
        
        @param request: DescribeLimitationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLimitationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLimitation',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeLimitationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_limitation(
        self,
        request: ess_20220222_models.DescribeLimitationRequest,
    ) -> ess_20220222_models.DescribeLimitationResponse:
        """
        @summary Queries resource quotas. You can call the DescribeLimitation operation to query the upper limits on resources such as scheduled tasks that can be created in a scaling group, load balancers that can be attached to a scaling group, instances that can be contained in a scaling group, and scaling configurations that can be created in a scaling group.
        
        @param request: DescribeLimitationRequest
        @return: DescribeLimitationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_limitation_with_options(request, runtime)

    async def describe_limitation_async(
        self,
        request: ess_20220222_models.DescribeLimitationRequest,
    ) -> ess_20220222_models.DescribeLimitationResponse:
        """
        @summary Queries resource quotas. You can call the DescribeLimitation operation to query the upper limits on resources such as scheduled tasks that can be created in a scaling group, load balancers that can be attached to a scaling group, instances that can be contained in a scaling group, and scaling configurations that can be created in a scaling group.
        
        @param request: DescribeLimitationRequest
        @return: DescribeLimitationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_limitation_with_options_async(request, runtime)

    def describe_notification_configurations_with_options(
        self,
        request: ess_20220222_models.DescribeNotificationConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeNotificationConfigurationsResponse:
        """
        @summary Queries notifications. If you want to learn about a notification regarding the status of a scaling event or resource changes, you can call the DescribeNotificationConfigurations operation. This operation enables you to retrieve notification details, analyze resource change data, and refine scaling policies to efficiently utilize resources and fulfill business needs.
        
        @param request: DescribeNotificationConfigurationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNotificationConfigurationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNotificationConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeNotificationConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_notification_configurations_with_options_async(
        self,
        request: ess_20220222_models.DescribeNotificationConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeNotificationConfigurationsResponse:
        """
        @summary Queries notifications. If you want to learn about a notification regarding the status of a scaling event or resource changes, you can call the DescribeNotificationConfigurations operation. This operation enables you to retrieve notification details, analyze resource change data, and refine scaling policies to efficiently utilize resources and fulfill business needs.
        
        @param request: DescribeNotificationConfigurationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNotificationConfigurationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNotificationConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeNotificationConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_notification_configurations(
        self,
        request: ess_20220222_models.DescribeNotificationConfigurationsRequest,
    ) -> ess_20220222_models.DescribeNotificationConfigurationsResponse:
        """
        @summary Queries notifications. If you want to learn about a notification regarding the status of a scaling event or resource changes, you can call the DescribeNotificationConfigurations operation. This operation enables you to retrieve notification details, analyze resource change data, and refine scaling policies to efficiently utilize resources and fulfill business needs.
        
        @param request: DescribeNotificationConfigurationsRequest
        @return: DescribeNotificationConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_notification_configurations_with_options(request, runtime)

    async def describe_notification_configurations_async(
        self,
        request: ess_20220222_models.DescribeNotificationConfigurationsRequest,
    ) -> ess_20220222_models.DescribeNotificationConfigurationsResponse:
        """
        @summary Queries notifications. If you want to learn about a notification regarding the status of a scaling event or resource changes, you can call the DescribeNotificationConfigurations operation. This operation enables you to retrieve notification details, analyze resource change data, and refine scaling policies to efficiently utilize resources and fulfill business needs.
        
        @param request: DescribeNotificationConfigurationsRequest
        @return: DescribeNotificationConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_notification_configurations_with_options_async(request, runtime)

    def describe_notification_types_with_options(
        self,
        request: ess_20220222_models.DescribeNotificationTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeNotificationTypesResponse:
        """
        @summary Queries notification types. You can call the DescribeNotificationTypes operation to query the types of notifications on scaling events or resource changes occurred in your scaling groups. Notifications are triggered in scenarios such as successful scale-out events, successful scale-in events, expiration of scheduled tasks, and partially successful scale-out events.
        
        @param request: DescribeNotificationTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNotificationTypesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNotificationTypes',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeNotificationTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_notification_types_with_options_async(
        self,
        request: ess_20220222_models.DescribeNotificationTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeNotificationTypesResponse:
        """
        @summary Queries notification types. You can call the DescribeNotificationTypes operation to query the types of notifications on scaling events or resource changes occurred in your scaling groups. Notifications are triggered in scenarios such as successful scale-out events, successful scale-in events, expiration of scheduled tasks, and partially successful scale-out events.
        
        @param request: DescribeNotificationTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNotificationTypesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNotificationTypes',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeNotificationTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_notification_types(
        self,
        request: ess_20220222_models.DescribeNotificationTypesRequest,
    ) -> ess_20220222_models.DescribeNotificationTypesResponse:
        """
        @summary Queries notification types. You can call the DescribeNotificationTypes operation to query the types of notifications on scaling events or resource changes occurred in your scaling groups. Notifications are triggered in scenarios such as successful scale-out events, successful scale-in events, expiration of scheduled tasks, and partially successful scale-out events.
        
        @param request: DescribeNotificationTypesRequest
        @return: DescribeNotificationTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_notification_types_with_options(request, runtime)

    async def describe_notification_types_async(
        self,
        request: ess_20220222_models.DescribeNotificationTypesRequest,
    ) -> ess_20220222_models.DescribeNotificationTypesResponse:
        """
        @summary Queries notification types. You can call the DescribeNotificationTypes operation to query the types of notifications on scaling events or resource changes occurred in your scaling groups. Notifications are triggered in scenarios such as successful scale-out events, successful scale-in events, expiration of scheduled tasks, and partially successful scale-out events.
        
        @param request: DescribeNotificationTypesRequest
        @return: DescribeNotificationTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_notification_types_with_options_async(request, runtime)

    def describe_pattern_types_with_options(
        self,
        request: ess_20220222_models.DescribePatternTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribePatternTypesResponse:
        """
        @summary Filters instance types that meet your business requirements. If you create a scaling configuration by opting for the Specify Instance Type approach, you can call the DescribePatternTypes operation. This operation is designed to sift through and identify instance types that fulfill your specific business needs. It does so by examining the number of vCPUs, memory size, instance family level, and maximum budgeted expense that you specify within the scaling configuration settings.
        
        @param request: DescribePatternTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePatternTypesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePatternTypes',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribePatternTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pattern_types_with_options_async(
        self,
        request: ess_20220222_models.DescribePatternTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribePatternTypesResponse:
        """
        @summary Filters instance types that meet your business requirements. If you create a scaling configuration by opting for the Specify Instance Type approach, you can call the DescribePatternTypes operation. This operation is designed to sift through and identify instance types that fulfill your specific business needs. It does so by examining the number of vCPUs, memory size, instance family level, and maximum budgeted expense that you specify within the scaling configuration settings.
        
        @param request: DescribePatternTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePatternTypesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePatternTypes',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribePatternTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pattern_types(
        self,
        request: ess_20220222_models.DescribePatternTypesRequest,
    ) -> ess_20220222_models.DescribePatternTypesResponse:
        """
        @summary Filters instance types that meet your business requirements. If you create a scaling configuration by opting for the Specify Instance Type approach, you can call the DescribePatternTypes operation. This operation is designed to sift through and identify instance types that fulfill your specific business needs. It does so by examining the number of vCPUs, memory size, instance family level, and maximum budgeted expense that you specify within the scaling configuration settings.
        
        @param request: DescribePatternTypesRequest
        @return: DescribePatternTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pattern_types_with_options(request, runtime)

    async def describe_pattern_types_async(
        self,
        request: ess_20220222_models.DescribePatternTypesRequest,
    ) -> ess_20220222_models.DescribePatternTypesResponse:
        """
        @summary Filters instance types that meet your business requirements. If you create a scaling configuration by opting for the Specify Instance Type approach, you can call the DescribePatternTypes operation. This operation is designed to sift through and identify instance types that fulfill your specific business needs. It does so by examining the number of vCPUs, memory size, instance family level, and maximum budgeted expense that you specify within the scaling configuration settings.
        
        @param request: DescribePatternTypesRequest
        @return: DescribePatternTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pattern_types_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ess_20220222_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeRegionsResponse:
        """
        @summary Queries regions. Before you activate Auto Scaling, you can call the DescribeRegions operation to query the regions where Auto Scaling is officially launched. This preliminary step facilitates the strategic selection of both the optimal region and availability zones for activating Auto Scaling, thereby guaranteeing the finest access speeds and operational efficiency within your chosen geographical area.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ess_20220222_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeRegionsResponse:
        """
        @summary Queries regions. Before you activate Auto Scaling, you can call the DescribeRegions operation to query the regions where Auto Scaling is officially launched. This preliminary step facilitates the strategic selection of both the optimal region and availability zones for activating Auto Scaling, thereby guaranteeing the finest access speeds and operational efficiency within your chosen geographical area.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: ess_20220222_models.DescribeRegionsRequest,
    ) -> ess_20220222_models.DescribeRegionsResponse:
        """
        @summary Queries regions. Before you activate Auto Scaling, you can call the DescribeRegions operation to query the regions where Auto Scaling is officially launched. This preliminary step facilitates the strategic selection of both the optimal region and availability zones for activating Auto Scaling, thereby guaranteeing the finest access speeds and operational efficiency within your chosen geographical area.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ess_20220222_models.DescribeRegionsRequest,
    ) -> ess_20220222_models.DescribeRegionsResponse:
        """
        @summary Queries regions. Before you activate Auto Scaling, you can call the DescribeRegions operation to query the regions where Auto Scaling is officially launched. This preliminary step facilitates the strategic selection of both the optimal region and availability zones for activating Auto Scaling, thereby guaranteeing the finest access speeds and operational efficiency within your chosen geographical area.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_scaling_activities_with_options(
        self,
        request: ess_20220222_models.DescribeScalingActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingActivitiesResponse:
        """
        @summary Queries scaling activities.
        
        @description You can specify a scaling group ID to query all scaling activities in the scaling group.
        You can filter query results based on the status of scaling activities.
        You can query scaling activities that are executed in the previous 30 days.
        
        @param request: DescribeScalingActivitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingActivitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_activity_ids):
            query['ScalingActivityIds'] = request.scaling_activity_ids
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.status_code):
            query['StatusCode'] = request.status_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingActivities',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingActivitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_activities_with_options_async(
        self,
        request: ess_20220222_models.DescribeScalingActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingActivitiesResponse:
        """
        @summary Queries scaling activities.
        
        @description You can specify a scaling group ID to query all scaling activities in the scaling group.
        You can filter query results based on the status of scaling activities.
        You can query scaling activities that are executed in the previous 30 days.
        
        @param request: DescribeScalingActivitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingActivitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_activity_ids):
            query['ScalingActivityIds'] = request.scaling_activity_ids
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.status_code):
            query['StatusCode'] = request.status_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingActivities',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingActivitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_activities(
        self,
        request: ess_20220222_models.DescribeScalingActivitiesRequest,
    ) -> ess_20220222_models.DescribeScalingActivitiesResponse:
        """
        @summary Queries scaling activities.
        
        @description You can specify a scaling group ID to query all scaling activities in the scaling group.
        You can filter query results based on the status of scaling activities.
        You can query scaling activities that are executed in the previous 30 days.
        
        @param request: DescribeScalingActivitiesRequest
        @return: DescribeScalingActivitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_activities_with_options(request, runtime)

    async def describe_scaling_activities_async(
        self,
        request: ess_20220222_models.DescribeScalingActivitiesRequest,
    ) -> ess_20220222_models.DescribeScalingActivitiesResponse:
        """
        @summary Queries scaling activities.
        
        @description You can specify a scaling group ID to query all scaling activities in the scaling group.
        You can filter query results based on the status of scaling activities.
        You can query scaling activities that are executed in the previous 30 days.
        
        @param request: DescribeScalingActivitiesRequest
        @return: DescribeScalingActivitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_activities_with_options_async(request, runtime)

    def describe_scaling_activity_detail_with_options(
        self,
        request: ess_20220222_models.DescribeScalingActivityDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingActivityDetailResponse:
        """
        @summary Queries the details of a scaling activity. The DescribeScalingActivityDetail operation enables you to access and monitor the details of a scaling activity, which is beneficial for troubleshooting and performance analysis purposes.
        
        @param request: DescribeScalingActivityDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingActivityDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingActivityDetail',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingActivityDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_activity_detail_with_options_async(
        self,
        request: ess_20220222_models.DescribeScalingActivityDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingActivityDetailResponse:
        """
        @summary Queries the details of a scaling activity. The DescribeScalingActivityDetail operation enables you to access and monitor the details of a scaling activity, which is beneficial for troubleshooting and performance analysis purposes.
        
        @param request: DescribeScalingActivityDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingActivityDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingActivityDetail',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingActivityDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_activity_detail(
        self,
        request: ess_20220222_models.DescribeScalingActivityDetailRequest,
    ) -> ess_20220222_models.DescribeScalingActivityDetailResponse:
        """
        @summary Queries the details of a scaling activity. The DescribeScalingActivityDetail operation enables you to access and monitor the details of a scaling activity, which is beneficial for troubleshooting and performance analysis purposes.
        
        @param request: DescribeScalingActivityDetailRequest
        @return: DescribeScalingActivityDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_activity_detail_with_options(request, runtime)

    async def describe_scaling_activity_detail_async(
        self,
        request: ess_20220222_models.DescribeScalingActivityDetailRequest,
    ) -> ess_20220222_models.DescribeScalingActivityDetailResponse:
        """
        @summary Queries the details of a scaling activity. The DescribeScalingActivityDetail operation enables you to access and monitor the details of a scaling activity, which is beneficial for troubleshooting and performance analysis purposes.
        
        @param request: DescribeScalingActivityDetailRequest
        @return: DescribeScalingActivityDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_activity_detail_with_options_async(request, runtime)

    def describe_scaling_configurations_with_options(
        self,
        request: ess_20220222_models.DescribeScalingConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingConfigurationsResponse:
        """
        @summary Queries scaling configurations.
        
        @param request: DescribeScalingConfigurationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingConfigurationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_configuration_ids):
            query['ScalingConfigurationIds'] = request.scaling_configuration_ids
        if not UtilClient.is_unset(request.scaling_configuration_names):
            query['ScalingConfigurationNames'] = request.scaling_configuration_names
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_configurations_with_options_async(
        self,
        request: ess_20220222_models.DescribeScalingConfigurationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingConfigurationsResponse:
        """
        @summary Queries scaling configurations.
        
        @param request: DescribeScalingConfigurationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingConfigurationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_configuration_ids):
            query['ScalingConfigurationIds'] = request.scaling_configuration_ids
        if not UtilClient.is_unset(request.scaling_configuration_names):
            query['ScalingConfigurationNames'] = request.scaling_configuration_names
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingConfigurations',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_configurations(
        self,
        request: ess_20220222_models.DescribeScalingConfigurationsRequest,
    ) -> ess_20220222_models.DescribeScalingConfigurationsResponse:
        """
        @summary Queries scaling configurations.
        
        @param request: DescribeScalingConfigurationsRequest
        @return: DescribeScalingConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_configurations_with_options(request, runtime)

    async def describe_scaling_configurations_async(
        self,
        request: ess_20220222_models.DescribeScalingConfigurationsRequest,
    ) -> ess_20220222_models.DescribeScalingConfigurationsResponse:
        """
        @summary Queries scaling configurations.
        
        @param request: DescribeScalingConfigurationsRequest
        @return: DescribeScalingConfigurationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_configurations_with_options_async(request, runtime)

    def describe_scaling_group_detail_with_options(
        self,
        request: ess_20220222_models.DescribeScalingGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingGroupDetailResponse:
        """
        @summary Queries a scaling group. You can call the DescribeScalingGroupDetail operation to query the basic information, instances, and scaling configurations of a scaling group. If you set OutputFormat to yaml, the output is a Kubernetes Deployment file in the YAML format.
        
        @param request: DescribeScalingGroupDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingGroupDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_format):
            query['OutputFormat'] = request.output_format
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingGroupDetail',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingGroupDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_group_detail_with_options_async(
        self,
        request: ess_20220222_models.DescribeScalingGroupDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingGroupDetailResponse:
        """
        @summary Queries a scaling group. You can call the DescribeScalingGroupDetail operation to query the basic information, instances, and scaling configurations of a scaling group. If you set OutputFormat to yaml, the output is a Kubernetes Deployment file in the YAML format.
        
        @param request: DescribeScalingGroupDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingGroupDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.output_format):
            query['OutputFormat'] = request.output_format
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingGroupDetail',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingGroupDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_group_detail(
        self,
        request: ess_20220222_models.DescribeScalingGroupDetailRequest,
    ) -> ess_20220222_models.DescribeScalingGroupDetailResponse:
        """
        @summary Queries a scaling group. You can call the DescribeScalingGroupDetail operation to query the basic information, instances, and scaling configurations of a scaling group. If you set OutputFormat to yaml, the output is a Kubernetes Deployment file in the YAML format.
        
        @param request: DescribeScalingGroupDetailRequest
        @return: DescribeScalingGroupDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_group_detail_with_options(request, runtime)

    async def describe_scaling_group_detail_async(
        self,
        request: ess_20220222_models.DescribeScalingGroupDetailRequest,
    ) -> ess_20220222_models.DescribeScalingGroupDetailResponse:
        """
        @summary Queries a scaling group. You can call the DescribeScalingGroupDetail operation to query the basic information, instances, and scaling configurations of a scaling group. If you set OutputFormat to yaml, the output is a Kubernetes Deployment file in the YAML format.
        
        @param request: DescribeScalingGroupDetailRequest
        @return: DescribeScalingGroupDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_group_detail_with_options_async(request, runtime)

    def describe_scaling_groups_with_options(
        self,
        request: ess_20220222_models.DescribeScalingGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingGroupsResponse:
        """
        @summary Queries scaling groups. If you want to query the basic information, instances, and scaling configurations of a scaling group, you can call the DescribeScalingGroups operation.
        
        @param request: DescribeScalingGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_ids):
            query['ScalingGroupIds'] = request.scaling_group_ids
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.scaling_group_names):
            query['ScalingGroupNames'] = request.scaling_group_names
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_groups_with_options_async(
        self,
        request: ess_20220222_models.DescribeScalingGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingGroupsResponse:
        """
        @summary Queries scaling groups. If you want to query the basic information, instances, and scaling configurations of a scaling group, you can call the DescribeScalingGroups operation.
        
        @param request: DescribeScalingGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_ids):
            query['ScalingGroupIds'] = request.scaling_group_ids
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.scaling_group_names):
            query['ScalingGroupNames'] = request.scaling_group_names
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_groups(
        self,
        request: ess_20220222_models.DescribeScalingGroupsRequest,
    ) -> ess_20220222_models.DescribeScalingGroupsResponse:
        """
        @summary Queries scaling groups. If you want to query the basic information, instances, and scaling configurations of a scaling group, you can call the DescribeScalingGroups operation.
        
        @param request: DescribeScalingGroupsRequest
        @return: DescribeScalingGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_groups_with_options(request, runtime)

    async def describe_scaling_groups_async(
        self,
        request: ess_20220222_models.DescribeScalingGroupsRequest,
    ) -> ess_20220222_models.DescribeScalingGroupsResponse:
        """
        @summary Queries scaling groups. If you want to query the basic information, instances, and scaling configurations of a scaling group, you can call the DescribeScalingGroups operation.
        
        @param request: DescribeScalingGroupsRequest
        @return: DescribeScalingGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_groups_with_options_async(request, runtime)

    def describe_scaling_instances_with_options(
        self,
        request: ess_20220222_models.DescribeScalingInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingInstancesResponse:
        """
        @summary Queries the Elastic Compute Service (ECS) instances in a scaling group. If you want to flexibly filter ECS instances that meet the specified criteria and query the instance details, you can call the DescribeScalingInstances operation. This operation enables you to input custom parameters for precise query of ECS instances, helping you gain a clear understanding of the instance details and optimize scaling configurations.
        
        @param request: DescribeScalingInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creation_type):
            query['CreationType'] = request.creation_type
        if not UtilClient.is_unset(request.creation_types):
            query['CreationTypes'] = request.creation_types
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lifecycle_state):
            query['LifecycleState'] = request.lifecycle_state
        if not UtilClient.is_unset(request.lifecycle_states):
            query['LifecycleStates'] = request.lifecycle_states
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_instances_with_options_async(
        self,
        request: ess_20220222_models.DescribeScalingInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingInstancesResponse:
        """
        @summary Queries the Elastic Compute Service (ECS) instances in a scaling group. If you want to flexibly filter ECS instances that meet the specified criteria and query the instance details, you can call the DescribeScalingInstances operation. This operation enables you to input custom parameters for precise query of ECS instances, helping you gain a clear understanding of the instance details and optimize scaling configurations.
        
        @param request: DescribeScalingInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.creation_type):
            query['CreationType'] = request.creation_type
        if not UtilClient.is_unset(request.creation_types):
            query['CreationTypes'] = request.creation_types
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lifecycle_state):
            query['LifecycleState'] = request.lifecycle_state
        if not UtilClient.is_unset(request.lifecycle_states):
            query['LifecycleStates'] = request.lifecycle_states
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_instances(
        self,
        request: ess_20220222_models.DescribeScalingInstancesRequest,
    ) -> ess_20220222_models.DescribeScalingInstancesResponse:
        """
        @summary Queries the Elastic Compute Service (ECS) instances in a scaling group. If you want to flexibly filter ECS instances that meet the specified criteria and query the instance details, you can call the DescribeScalingInstances operation. This operation enables you to input custom parameters for precise query of ECS instances, helping you gain a clear understanding of the instance details and optimize scaling configurations.
        
        @param request: DescribeScalingInstancesRequest
        @return: DescribeScalingInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_instances_with_options(request, runtime)

    async def describe_scaling_instances_async(
        self,
        request: ess_20220222_models.DescribeScalingInstancesRequest,
    ) -> ess_20220222_models.DescribeScalingInstancesResponse:
        """
        @summary Queries the Elastic Compute Service (ECS) instances in a scaling group. If you want to flexibly filter ECS instances that meet the specified criteria and query the instance details, you can call the DescribeScalingInstances operation. This operation enables you to input custom parameters for precise query of ECS instances, helping you gain a clear understanding of the instance details and optimize scaling configurations.
        
        @param request: DescribeScalingInstancesRequest
        @return: DescribeScalingInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_instances_with_options_async(request, runtime)

    def describe_scaling_rules_with_options(
        self,
        request: ess_20220222_models.DescribeScalingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingRulesResponse:
        """
        @summary Queries all scaling rules in a scaling group.
        
        @description You can specify a scaling group ID to query all scaling rules in the scaling group. You can also specify the scaling rule ID, name, unique identifier, and type in the request parameters as filter conditions.
        
        @param request: DescribeScalingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_rule_aris):
            query['ScalingRuleAris'] = request.scaling_rule_aris
        if not UtilClient.is_unset(request.scaling_rule_ids):
            query['ScalingRuleIds'] = request.scaling_rule_ids
        if not UtilClient.is_unset(request.scaling_rule_names):
            query['ScalingRuleNames'] = request.scaling_rule_names
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        if not UtilClient.is_unset(request.show_alarm_rules):
            query['ShowAlarmRules'] = request.show_alarm_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingRules',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_rules_with_options_async(
        self,
        request: ess_20220222_models.DescribeScalingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScalingRulesResponse:
        """
        @summary Queries all scaling rules in a scaling group.
        
        @description You can specify a scaling group ID to query all scaling rules in the scaling group. You can also specify the scaling rule ID, name, unique identifier, and type in the request parameters as filter conditions.
        
        @param request: DescribeScalingRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScalingRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_rule_aris):
            query['ScalingRuleAris'] = request.scaling_rule_aris
        if not UtilClient.is_unset(request.scaling_rule_ids):
            query['ScalingRuleIds'] = request.scaling_rule_ids
        if not UtilClient.is_unset(request.scaling_rule_names):
            query['ScalingRuleNames'] = request.scaling_rule_names
        if not UtilClient.is_unset(request.scaling_rule_type):
            query['ScalingRuleType'] = request.scaling_rule_type
        if not UtilClient.is_unset(request.show_alarm_rules):
            query['ShowAlarmRules'] = request.show_alarm_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScalingRules',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scaling_rules(
        self,
        request: ess_20220222_models.DescribeScalingRulesRequest,
    ) -> ess_20220222_models.DescribeScalingRulesResponse:
        """
        @summary Queries all scaling rules in a scaling group.
        
        @description You can specify a scaling group ID to query all scaling rules in the scaling group. You can also specify the scaling rule ID, name, unique identifier, and type in the request parameters as filter conditions.
        
        @param request: DescribeScalingRulesRequest
        @return: DescribeScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_rules_with_options(request, runtime)

    async def describe_scaling_rules_async(
        self,
        request: ess_20220222_models.DescribeScalingRulesRequest,
    ) -> ess_20220222_models.DescribeScalingRulesResponse:
        """
        @summary Queries all scaling rules in a scaling group.
        
        @description You can specify a scaling group ID to query all scaling rules in the scaling group. You can also specify the scaling rule ID, name, unique identifier, and type in the request parameters as filter conditions.
        
        @param request: DescribeScalingRulesRequest
        @return: DescribeScalingRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_rules_with_options_async(request, runtime)

    def describe_scheduled_tasks_with_options(
        self,
        request: ess_20220222_models.DescribeScheduledTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScheduledTasksResponse:
        """
        @summary Queries scheduled tasks. A scheduled task is a predefined task that triggers the automatic execution of a scaling rule at the specified point in time. It ensures an automatic scaling of computing resources to fulfill your business demands at a minimum cost. After you create a scheduled task, you can call the DescribeScheduledTasks operation to query the details of the task, such as the execution time point and the scaling group ID. You can also call this operation to query the total number of existing scheduled tasks.
        
        @description You can query scheduled tasks by scaling rule, task ID, or task name.
        
        @param request: DescribeScheduledTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScheduledTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not UtilClient.is_unset(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scheduled_actions):
            query['ScheduledActions'] = request.scheduled_actions
        if not UtilClient.is_unset(request.scheduled_task_ids):
            query['ScheduledTaskIds'] = request.scheduled_task_ids
        if not UtilClient.is_unset(request.scheduled_task_names):
            query['ScheduledTaskNames'] = request.scheduled_task_names
        if not UtilClient.is_unset(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScheduledTasks',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScheduledTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scheduled_tasks_with_options_async(
        self,
        request: ess_20220222_models.DescribeScheduledTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DescribeScheduledTasksResponse:
        """
        @summary Queries scheduled tasks. A scheduled task is a predefined task that triggers the automatic execution of a scaling rule at the specified point in time. It ensures an automatic scaling of computing resources to fulfill your business demands at a minimum cost. After you create a scheduled task, you can call the DescribeScheduledTasks operation to query the details of the task, such as the execution time point and the scaling group ID. You can also call this operation to query the total number of existing scheduled tasks.
        
        @description You can query scheduled tasks by scaling rule, task ID, or task name.
        
        @param request: DescribeScheduledTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeScheduledTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not UtilClient.is_unset(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scheduled_actions):
            query['ScheduledActions'] = request.scheduled_actions
        if not UtilClient.is_unset(request.scheduled_task_ids):
            query['ScheduledTaskIds'] = request.scheduled_task_ids
        if not UtilClient.is_unset(request.scheduled_task_names):
            query['ScheduledTaskNames'] = request.scheduled_task_names
        if not UtilClient.is_unset(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeScheduledTasks',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DescribeScheduledTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_scheduled_tasks(
        self,
        request: ess_20220222_models.DescribeScheduledTasksRequest,
    ) -> ess_20220222_models.DescribeScheduledTasksResponse:
        """
        @summary Queries scheduled tasks. A scheduled task is a predefined task that triggers the automatic execution of a scaling rule at the specified point in time. It ensures an automatic scaling of computing resources to fulfill your business demands at a minimum cost. After you create a scheduled task, you can call the DescribeScheduledTasks operation to query the details of the task, such as the execution time point and the scaling group ID. You can also call this operation to query the total number of existing scheduled tasks.
        
        @description You can query scheduled tasks by scaling rule, task ID, or task name.
        
        @param request: DescribeScheduledTasksRequest
        @return: DescribeScheduledTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_scheduled_tasks_with_options(request, runtime)

    async def describe_scheduled_tasks_async(
        self,
        request: ess_20220222_models.DescribeScheduledTasksRequest,
    ) -> ess_20220222_models.DescribeScheduledTasksResponse:
        """
        @summary Queries scheduled tasks. A scheduled task is a predefined task that triggers the automatic execution of a scaling rule at the specified point in time. It ensures an automatic scaling of computing resources to fulfill your business demands at a minimum cost. After you create a scheduled task, you can call the DescribeScheduledTasks operation to query the details of the task, such as the execution time point and the scaling group ID. You can also call this operation to query the total number of existing scheduled tasks.
        
        @description You can query scheduled tasks by scaling rule, task ID, or task name.
        
        @param request: DescribeScheduledTasksRequest
        @return: DescribeScheduledTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_scheduled_tasks_with_options_async(request, runtime)

    def detach_alb_server_groups_with_options(
        self,
        request: ess_20220222_models.DetachAlbServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachAlbServerGroupsResponse:
        """
        @summary Disassociates one or more Application Load Balancer (ALB) server groups from a scaling group.
        
        @param request: DetachAlbServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachAlbServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachAlbServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachAlbServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_alb_server_groups_with_options_async(
        self,
        request: ess_20220222_models.DetachAlbServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachAlbServerGroupsResponse:
        """
        @summary Disassociates one or more Application Load Balancer (ALB) server groups from a scaling group.
        
        @param request: DetachAlbServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachAlbServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alb_server_groups):
            query['AlbServerGroups'] = request.alb_server_groups
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachAlbServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachAlbServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_alb_server_groups(
        self,
        request: ess_20220222_models.DetachAlbServerGroupsRequest,
    ) -> ess_20220222_models.DetachAlbServerGroupsResponse:
        """
        @summary Disassociates one or more Application Load Balancer (ALB) server groups from a scaling group.
        
        @param request: DetachAlbServerGroupsRequest
        @return: DetachAlbServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_alb_server_groups_with_options(request, runtime)

    async def detach_alb_server_groups_async(
        self,
        request: ess_20220222_models.DetachAlbServerGroupsRequest,
    ) -> ess_20220222_models.DetachAlbServerGroupsResponse:
        """
        @summary Disassociates one or more Application Load Balancer (ALB) server groups from a scaling group.
        
        @param request: DetachAlbServerGroupsRequest
        @return: DetachAlbServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_alb_server_groups_with_options_async(request, runtime)

    def detach_dbinstances_with_options(
        self,
        request: ess_20220222_models.DetachDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachDBInstancesResponse:
        """
        @summary Disassociates one or more ApsaraDB RDS instances from a scaling group.
        
        @param request: DetachDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_security_group):
            query['RemoveSecurityGroup'] = request.remove_security_group
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDBInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_dbinstances_with_options_async(
        self,
        request: ess_20220222_models.DetachDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachDBInstancesResponse:
        """
        @summary Disassociates one or more ApsaraDB RDS instances from a scaling group.
        
        @param request: DetachDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstances):
            query['DBInstances'] = request.dbinstances
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_security_group):
            query['RemoveSecurityGroup'] = request.remove_security_group
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDBInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_dbinstances(
        self,
        request: ess_20220222_models.DetachDBInstancesRequest,
    ) -> ess_20220222_models.DetachDBInstancesResponse:
        """
        @summary Disassociates one or more ApsaraDB RDS instances from a scaling group.
        
        @param request: DetachDBInstancesRequest
        @return: DetachDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_dbinstances_with_options(request, runtime)

    async def detach_dbinstances_async(
        self,
        request: ess_20220222_models.DetachDBInstancesRequest,
    ) -> ess_20220222_models.DetachDBInstancesResponse:
        """
        @summary Disassociates one or more ApsaraDB RDS instances from a scaling group.
        
        @param request: DetachDBInstancesRequest
        @return: DetachDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_dbinstances_with_options_async(request, runtime)

    def detach_instances_with_options(
        self,
        request: ess_20220222_models.DetachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachInstancesResponse:
        """
        @summary Removes instances from a scaling group. If an enabled scaling group has no ongoing scaling activities, you can call the DetachInstances operation to remove one or more Elastic Compute Service (ECS) instances, elastic container instances, or Alibaba Cloud-hosted third-party instances from the scaling group.
        
        @description    Before you call the DetachInstances operation, make sure that the following conditions are met:
        The specified scaling group is enabled.
        The specified scaling group does not have any ongoing scaling activities.
        *\
        *Note** If the specified scaling group does not have any ongoing scaling activities, the operation can bypass the cooldown period of the scaling group and immediately trigger scaling activities.
        Before you call this operation, take note of the following items:
        The ECS instances, elastic container instances, or Alibaba Cloud-hosted third-party instances that are removed from a scaling group by using this operation can run independently. If needed, you can call the [AttachInstances](https://help.aliyun.com/document_detail/25954.html) operation to re-add these instances to a scaling group.
        The ECS instances, elastic container instances, or Alibaba Cloud-hosted third-party instances that are removed from a scaling group by using this operation are not stopped or released.
        A successful call only means that Auto Scaling accepts your request. Scaling activities can be triggered as expected, but their successful execution is not guaranteed. You can query the status of a scaling activity based on the ScalingActivityId response parameter.
        The removal of ECS instances, elastic container instances, or Alibaba Cloud-hosted third-party instances must not result in the overall number of instances within the specified scaling group falling below the minimum capacity threshold (MinSize); otherwise, an error will be reported.
        
        @param request: DetachInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.decrease_desired_capacity):
            query['DecreaseDesiredCapacity'] = request.decrease_desired_capacity
        if not UtilClient.is_unset(request.detach_option):
            query['DetachOption'] = request.detach_option
        if not UtilClient.is_unset(request.ignore_invalid_instance):
            query['IgnoreInvalidInstance'] = request.ignore_invalid_instance
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lifecycle_hook):
            query['LifecycleHook'] = request.lifecycle_hook
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_instances_with_options_async(
        self,
        request: ess_20220222_models.DetachInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachInstancesResponse:
        """
        @summary Removes instances from a scaling group. If an enabled scaling group has no ongoing scaling activities, you can call the DetachInstances operation to remove one or more Elastic Compute Service (ECS) instances, elastic container instances, or Alibaba Cloud-hosted third-party instances from the scaling group.
        
        @description    Before you call the DetachInstances operation, make sure that the following conditions are met:
        The specified scaling group is enabled.
        The specified scaling group does not have any ongoing scaling activities.
        *\
        *Note** If the specified scaling group does not have any ongoing scaling activities, the operation can bypass the cooldown period of the scaling group and immediately trigger scaling activities.
        Before you call this operation, take note of the following items:
        The ECS instances, elastic container instances, or Alibaba Cloud-hosted third-party instances that are removed from a scaling group by using this operation can run independently. If needed, you can call the [AttachInstances](https://help.aliyun.com/document_detail/25954.html) operation to re-add these instances to a scaling group.
        The ECS instances, elastic container instances, or Alibaba Cloud-hosted third-party instances that are removed from a scaling group by using this operation are not stopped or released.
        A successful call only means that Auto Scaling accepts your request. Scaling activities can be triggered as expected, but their successful execution is not guaranteed. You can query the status of a scaling activity based on the ScalingActivityId response parameter.
        The removal of ECS instances, elastic container instances, or Alibaba Cloud-hosted third-party instances must not result in the overall number of instances within the specified scaling group falling below the minimum capacity threshold (MinSize); otherwise, an error will be reported.
        
        @param request: DetachInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.decrease_desired_capacity):
            query['DecreaseDesiredCapacity'] = request.decrease_desired_capacity
        if not UtilClient.is_unset(request.detach_option):
            query['DetachOption'] = request.detach_option
        if not UtilClient.is_unset(request.ignore_invalid_instance):
            query['IgnoreInvalidInstance'] = request.ignore_invalid_instance
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.lifecycle_hook):
            query['LifecycleHook'] = request.lifecycle_hook
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_instances(
        self,
        request: ess_20220222_models.DetachInstancesRequest,
    ) -> ess_20220222_models.DetachInstancesResponse:
        """
        @summary Removes instances from a scaling group. If an enabled scaling group has no ongoing scaling activities, you can call the DetachInstances operation to remove one or more Elastic Compute Service (ECS) instances, elastic container instances, or Alibaba Cloud-hosted third-party instances from the scaling group.
        
        @description    Before you call the DetachInstances operation, make sure that the following conditions are met:
        The specified scaling group is enabled.
        The specified scaling group does not have any ongoing scaling activities.
        *\
        *Note** If the specified scaling group does not have any ongoing scaling activities, the operation can bypass the cooldown period of the scaling group and immediately trigger scaling activities.
        Before you call this operation, take note of the following items:
        The ECS instances, elastic container instances, or Alibaba Cloud-hosted third-party instances that are removed from a scaling group by using this operation can run independently. If needed, you can call the [AttachInstances](https://help.aliyun.com/document_detail/25954.html) operation to re-add these instances to a scaling group.
        The ECS instances, elastic container instances, or Alibaba Cloud-hosted third-party instances that are removed from a scaling group by using this operation are not stopped or released.
        A successful call only means that Auto Scaling accepts your request. Scaling activities can be triggered as expected, but their successful execution is not guaranteed. You can query the status of a scaling activity based on the ScalingActivityId response parameter.
        The removal of ECS instances, elastic container instances, or Alibaba Cloud-hosted third-party instances must not result in the overall number of instances within the specified scaling group falling below the minimum capacity threshold (MinSize); otherwise, an error will be reported.
        
        @param request: DetachInstancesRequest
        @return: DetachInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_instances_with_options(request, runtime)

    async def detach_instances_async(
        self,
        request: ess_20220222_models.DetachInstancesRequest,
    ) -> ess_20220222_models.DetachInstancesResponse:
        """
        @summary Removes instances from a scaling group. If an enabled scaling group has no ongoing scaling activities, you can call the DetachInstances operation to remove one or more Elastic Compute Service (ECS) instances, elastic container instances, or Alibaba Cloud-hosted third-party instances from the scaling group.
        
        @description    Before you call the DetachInstances operation, make sure that the following conditions are met:
        The specified scaling group is enabled.
        The specified scaling group does not have any ongoing scaling activities.
        *\
        *Note** If the specified scaling group does not have any ongoing scaling activities, the operation can bypass the cooldown period of the scaling group and immediately trigger scaling activities.
        Before you call this operation, take note of the following items:
        The ECS instances, elastic container instances, or Alibaba Cloud-hosted third-party instances that are removed from a scaling group by using this operation can run independently. If needed, you can call the [AttachInstances](https://help.aliyun.com/document_detail/25954.html) operation to re-add these instances to a scaling group.
        The ECS instances, elastic container instances, or Alibaba Cloud-hosted third-party instances that are removed from a scaling group by using this operation are not stopped or released.
        A successful call only means that Auto Scaling accepts your request. Scaling activities can be triggered as expected, but their successful execution is not guaranteed. You can query the status of a scaling activity based on the ScalingActivityId response parameter.
        The removal of ECS instances, elastic container instances, or Alibaba Cloud-hosted third-party instances must not result in the overall number of instances within the specified scaling group falling below the minimum capacity threshold (MinSize); otherwise, an error will be reported.
        
        @param request: DetachInstancesRequest
        @return: DetachInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_instances_with_options_async(request, runtime)

    def detach_load_balancers_with_options(
        self,
        request: ess_20220222_models.DetachLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachLoadBalancersResponse:
        """
        @summary Detaches Classic Load Balancer (CLB, formerly known as Server Load Balancer or SLB) instances from a scaling group. If the current CLB instance no longer meets your business requirements, you can call the DetachLoadBalancers operation to detach it from your scaling group. When you call this operation, you can use ScalingGroupId, LoadBalancer.N, and ForceDetach to specify one or more CLB instances to detach. You can also determine whether to call this operation asynchronously and whether to remove the Elastic Compute Service (ECS) instances acting as backend servers from the backend server groups of the CLB instance. You can call this operation to detach only CLB instances from a scaling group.
        
        @param request: DetachLoadBalancersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.load_balancers):
            query['LoadBalancers'] = request.load_balancers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachLoadBalancers',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_load_balancers_with_options_async(
        self,
        request: ess_20220222_models.DetachLoadBalancersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachLoadBalancersResponse:
        """
        @summary Detaches Classic Load Balancer (CLB, formerly known as Server Load Balancer or SLB) instances from a scaling group. If the current CLB instance no longer meets your business requirements, you can call the DetachLoadBalancers operation to detach it from your scaling group. When you call this operation, you can use ScalingGroupId, LoadBalancer.N, and ForceDetach to specify one or more CLB instances to detach. You can also determine whether to call this operation asynchronously and whether to remove the Elastic Compute Service (ECS) instances acting as backend servers from the backend server groups of the CLB instance. You can call this operation to detach only CLB instances from a scaling group.
        
        @param request: DetachLoadBalancersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachLoadBalancersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.load_balancers):
            query['LoadBalancers'] = request.load_balancers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachLoadBalancers',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachLoadBalancersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_load_balancers(
        self,
        request: ess_20220222_models.DetachLoadBalancersRequest,
    ) -> ess_20220222_models.DetachLoadBalancersResponse:
        """
        @summary Detaches Classic Load Balancer (CLB, formerly known as Server Load Balancer or SLB) instances from a scaling group. If the current CLB instance no longer meets your business requirements, you can call the DetachLoadBalancers operation to detach it from your scaling group. When you call this operation, you can use ScalingGroupId, LoadBalancer.N, and ForceDetach to specify one or more CLB instances to detach. You can also determine whether to call this operation asynchronously and whether to remove the Elastic Compute Service (ECS) instances acting as backend servers from the backend server groups of the CLB instance. You can call this operation to detach only CLB instances from a scaling group.
        
        @param request: DetachLoadBalancersRequest
        @return: DetachLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_load_balancers_with_options(request, runtime)

    async def detach_load_balancers_async(
        self,
        request: ess_20220222_models.DetachLoadBalancersRequest,
    ) -> ess_20220222_models.DetachLoadBalancersResponse:
        """
        @summary Detaches Classic Load Balancer (CLB, formerly known as Server Load Balancer or SLB) instances from a scaling group. If the current CLB instance no longer meets your business requirements, you can call the DetachLoadBalancers operation to detach it from your scaling group. When you call this operation, you can use ScalingGroupId, LoadBalancer.N, and ForceDetach to specify one or more CLB instances to detach. You can also determine whether to call this operation asynchronously and whether to remove the Elastic Compute Service (ECS) instances acting as backend servers from the backend server groups of the CLB instance. You can call this operation to detach only CLB instances from a scaling group.
        
        @param request: DetachLoadBalancersRequest
        @return: DetachLoadBalancersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_load_balancers_with_options_async(request, runtime)

    def detach_server_groups_with_options(
        self,
        request: ess_20220222_models.DetachServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachServerGroupsResponse:
        """
        @summary Detach server groups from a scaling group. To seamlessly adjust the number of instances in response to changes in your business workload or to maintain the uninterrupted accessibility of your application, you can call the DetachServerGroups operation. By detaching Application Load Balancer (ALB) or Network Load Balancer (NLB) server groups from your scaling group, this operation enables Auto Scaling to automatically tailor your computing capacity to your business needs. Furthermore, it optimizes traffic routing by dynamically allocating incoming requests based on current workload patterns, which significantly improves the stability and performance of your application.
        
        @param request: DetachServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_server_groups_with_options_async(
        self,
        request: ess_20220222_models.DetachServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachServerGroupsResponse:
        """
        @summary Detach server groups from a scaling group. To seamlessly adjust the number of instances in response to changes in your business workload or to maintain the uninterrupted accessibility of your application, you can call the DetachServerGroups operation. By detaching Application Load Balancer (ALB) or Network Load Balancer (NLB) server groups from your scaling group, this operation enables Auto Scaling to automatically tailor your computing capacity to your business needs. Furthermore, it optimizes traffic routing by dynamically allocating incoming requests based on current workload patterns, which significantly improves the stability and performance of your application.
        
        @param request: DetachServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.server_groups):
            query['ServerGroups'] = request.server_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_server_groups(
        self,
        request: ess_20220222_models.DetachServerGroupsRequest,
    ) -> ess_20220222_models.DetachServerGroupsResponse:
        """
        @summary Detach server groups from a scaling group. To seamlessly adjust the number of instances in response to changes in your business workload or to maintain the uninterrupted accessibility of your application, you can call the DetachServerGroups operation. By detaching Application Load Balancer (ALB) or Network Load Balancer (NLB) server groups from your scaling group, this operation enables Auto Scaling to automatically tailor your computing capacity to your business needs. Furthermore, it optimizes traffic routing by dynamically allocating incoming requests based on current workload patterns, which significantly improves the stability and performance of your application.
        
        @param request: DetachServerGroupsRequest
        @return: DetachServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_server_groups_with_options(request, runtime)

    async def detach_server_groups_async(
        self,
        request: ess_20220222_models.DetachServerGroupsRequest,
    ) -> ess_20220222_models.DetachServerGroupsResponse:
        """
        @summary Detach server groups from a scaling group. To seamlessly adjust the number of instances in response to changes in your business workload or to maintain the uninterrupted accessibility of your application, you can call the DetachServerGroups operation. By detaching Application Load Balancer (ALB) or Network Load Balancer (NLB) server groups from your scaling group, this operation enables Auto Scaling to automatically tailor your computing capacity to your business needs. Furthermore, it optimizes traffic routing by dynamically allocating incoming requests based on current workload patterns, which significantly improves the stability and performance of your application.
        
        @param request: DetachServerGroupsRequest
        @return: DetachServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_server_groups_with_options_async(request, runtime)

    def detach_vserver_groups_with_options(
        self,
        request: ess_20220222_models.DetachVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachVServerGroupsResponse:
        """
        @summary Detaches vServer groups from a scaling group. Auto Scaling supports the attachment of load balancers to scaling groups to improve service performance. If the load balancer currently attached to your scaling group is no longer needed to distribute the access traffic to the instances in your scaling group, you can call the DetachVServerGroups operation to detach one or more vServer groups of this load balancer from the scaling group.
        
        @description    When you call the DetachVServerGroups operation, you must use the following parameters to specify the vServer groups that you want to detach from your scaling group:
        LoadBalancerId: the ID of the load balancer
        VServerGroupId: the ID of the vServer group
        Port: the port number of the vServer group
        When the vServer group specified by the request parameters matches that attached to your scaling group, this operation yields a favorable result. Otherwise, the request is ignored and no error is reported.
        Before you call this operation, you must make sure that the load balancer has ceased routing the access traffic to the instances in the scaling group. Failure to do so may lead to service requests being dropped or lost during the detachment process.
        
        @param request: DetachVServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachVServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachVServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachVServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_vserver_groups_with_options_async(
        self,
        request: ess_20220222_models.DetachVServerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DetachVServerGroupsResponse:
        """
        @summary Detaches vServer groups from a scaling group. Auto Scaling supports the attachment of load balancers to scaling groups to improve service performance. If the load balancer currently attached to your scaling group is no longer needed to distribute the access traffic to the instances in your scaling group, you can call the DetachVServerGroups operation to detach one or more vServer groups of this load balancer from the scaling group.
        
        @description    When you call the DetachVServerGroups operation, you must use the following parameters to specify the vServer groups that you want to detach from your scaling group:
        LoadBalancerId: the ID of the load balancer
        VServerGroupId: the ID of the vServer group
        Port: the port number of the vServer group
        When the vServer group specified by the request parameters matches that attached to your scaling group, this operation yields a favorable result. Otherwise, the request is ignored and no error is reported.
        Before you call this operation, you must make sure that the load balancer has ceased routing the access traffic to the instances in the scaling group. Failure to do so may lead to service requests being dropped or lost during the detachment process.
        
        @param request: DetachVServerGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachVServerGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.force_detach):
            query['ForceDetach'] = request.force_detach
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.vserver_groups):
            query['VServerGroups'] = request.vserver_groups
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachVServerGroups',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DetachVServerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_vserver_groups(
        self,
        request: ess_20220222_models.DetachVServerGroupsRequest,
    ) -> ess_20220222_models.DetachVServerGroupsResponse:
        """
        @summary Detaches vServer groups from a scaling group. Auto Scaling supports the attachment of load balancers to scaling groups to improve service performance. If the load balancer currently attached to your scaling group is no longer needed to distribute the access traffic to the instances in your scaling group, you can call the DetachVServerGroups operation to detach one or more vServer groups of this load balancer from the scaling group.
        
        @description    When you call the DetachVServerGroups operation, you must use the following parameters to specify the vServer groups that you want to detach from your scaling group:
        LoadBalancerId: the ID of the load balancer
        VServerGroupId: the ID of the vServer group
        Port: the port number of the vServer group
        When the vServer group specified by the request parameters matches that attached to your scaling group, this operation yields a favorable result. Otherwise, the request is ignored and no error is reported.
        Before you call this operation, you must make sure that the load balancer has ceased routing the access traffic to the instances in the scaling group. Failure to do so may lead to service requests being dropped or lost during the detachment process.
        
        @param request: DetachVServerGroupsRequest
        @return: DetachVServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_vserver_groups_with_options(request, runtime)

    async def detach_vserver_groups_async(
        self,
        request: ess_20220222_models.DetachVServerGroupsRequest,
    ) -> ess_20220222_models.DetachVServerGroupsResponse:
        """
        @summary Detaches vServer groups from a scaling group. Auto Scaling supports the attachment of load balancers to scaling groups to improve service performance. If the load balancer currently attached to your scaling group is no longer needed to distribute the access traffic to the instances in your scaling group, you can call the DetachVServerGroups operation to detach one or more vServer groups of this load balancer from the scaling group.
        
        @description    When you call the DetachVServerGroups operation, you must use the following parameters to specify the vServer groups that you want to detach from your scaling group:
        LoadBalancerId: the ID of the load balancer
        VServerGroupId: the ID of the vServer group
        Port: the port number of the vServer group
        When the vServer group specified by the request parameters matches that attached to your scaling group, this operation yields a favorable result. Otherwise, the request is ignored and no error is reported.
        Before you call this operation, you must make sure that the load balancer has ceased routing the access traffic to the instances in the scaling group. Failure to do so may lead to service requests being dropped or lost during the detachment process.
        
        @param request: DetachVServerGroupsRequest
        @return: DetachVServerGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_vserver_groups_with_options_async(request, runtime)

    def disable_alarm_with_options(
        self,
        request: ess_20220222_models.DisableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DisableAlarmResponse:
        """
        @summary Disables an event-triggered task. If your business pattern is unpredictable or prone to unforeseen traffic spikes, you can create event-triggered tasks by associating CloudMonitor metrics to effectively monitor fluctuations in your business workload. Upon detecting that the criteria for alerts, as specified in event-triggered tasks, are fulfilled, Auto Scaling promptly issues alerts and executes the scaling rules predefined within those tasks. This process occurs within the predefined effective time windows of the tasks, thereby facilitating the automatic increase or decrease of Elastic Compute Service (ECS) instances or elastic container instances within your scaling groups. Ultimately, this mechanism ensures the dynamic optimization of resources based on real-time workload demands. If you currently do not need an event-triggered task, you can call the DisableAlarm operation to disable it.
        
        @description Before you disable an event-triggered task, make sure that the task is in the `Normal`, `Alert`, or `Insufficient Data` state.
        
        @param request: DisableAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DisableAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_alarm_with_options_async(
        self,
        request: ess_20220222_models.DisableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DisableAlarmResponse:
        """
        @summary Disables an event-triggered task. If your business pattern is unpredictable or prone to unforeseen traffic spikes, you can create event-triggered tasks by associating CloudMonitor metrics to effectively monitor fluctuations in your business workload. Upon detecting that the criteria for alerts, as specified in event-triggered tasks, are fulfilled, Auto Scaling promptly issues alerts and executes the scaling rules predefined within those tasks. This process occurs within the predefined effective time windows of the tasks, thereby facilitating the automatic increase or decrease of Elastic Compute Service (ECS) instances or elastic container instances within your scaling groups. Ultimately, this mechanism ensures the dynamic optimization of resources based on real-time workload demands. If you currently do not need an event-triggered task, you can call the DisableAlarm operation to disable it.
        
        @description Before you disable an event-triggered task, make sure that the task is in the `Normal`, `Alert`, or `Insufficient Data` state.
        
        @param request: DisableAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DisableAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_alarm(
        self,
        request: ess_20220222_models.DisableAlarmRequest,
    ) -> ess_20220222_models.DisableAlarmResponse:
        """
        @summary Disables an event-triggered task. If your business pattern is unpredictable or prone to unforeseen traffic spikes, you can create event-triggered tasks by associating CloudMonitor metrics to effectively monitor fluctuations in your business workload. Upon detecting that the criteria for alerts, as specified in event-triggered tasks, are fulfilled, Auto Scaling promptly issues alerts and executes the scaling rules predefined within those tasks. This process occurs within the predefined effective time windows of the tasks, thereby facilitating the automatic increase or decrease of Elastic Compute Service (ECS) instances or elastic container instances within your scaling groups. Ultimately, this mechanism ensures the dynamic optimization of resources based on real-time workload demands. If you currently do not need an event-triggered task, you can call the DisableAlarm operation to disable it.
        
        @description Before you disable an event-triggered task, make sure that the task is in the `Normal`, `Alert`, or `Insufficient Data` state.
        
        @param request: DisableAlarmRequest
        @return: DisableAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_alarm_with_options(request, runtime)

    async def disable_alarm_async(
        self,
        request: ess_20220222_models.DisableAlarmRequest,
    ) -> ess_20220222_models.DisableAlarmResponse:
        """
        @summary Disables an event-triggered task. If your business pattern is unpredictable or prone to unforeseen traffic spikes, you can create event-triggered tasks by associating CloudMonitor metrics to effectively monitor fluctuations in your business workload. Upon detecting that the criteria for alerts, as specified in event-triggered tasks, are fulfilled, Auto Scaling promptly issues alerts and executes the scaling rules predefined within those tasks. This process occurs within the predefined effective time windows of the tasks, thereby facilitating the automatic increase or decrease of Elastic Compute Service (ECS) instances or elastic container instances within your scaling groups. Ultimately, this mechanism ensures the dynamic optimization of resources based on real-time workload demands. If you currently do not need an event-triggered task, you can call the DisableAlarm operation to disable it.
        
        @description Before you disable an event-triggered task, make sure that the task is in the `Normal`, `Alert`, or `Insufficient Data` state.
        
        @param request: DisableAlarmRequest
        @return: DisableAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_alarm_with_options_async(request, runtime)

    def disable_scaling_group_with_options(
        self,
        request: ess_20220222_models.DisableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DisableScalingGroupResponse:
        """
        @summary Disables a scaling group. If you temporarily do not require a scaling group that is in the Enabled state, you can call the DisableScalingGroup operation to disable it.
        
        @description Before you call this operation to disable a scaling group, take note of the following items:
        If scaling activities are being executed in the specified scaling group when you call this operation, these activities will continue until they are complete. However, scaling activities that are triggered after this operation is called will be rejected.
        This operation can be called only when the scaling group is in the Active state.
        
        @param request: DisableScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DisableScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_scaling_group_with_options_async(
        self,
        request: ess_20220222_models.DisableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.DisableScalingGroupResponse:
        """
        @summary Disables a scaling group. If you temporarily do not require a scaling group that is in the Enabled state, you can call the DisableScalingGroup operation to disable it.
        
        @description Before you call this operation to disable a scaling group, take note of the following items:
        If scaling activities are being executed in the specified scaling group when you call this operation, these activities will continue until they are complete. However, scaling activities that are triggered after this operation is called will be rejected.
        This operation can be called only when the scaling group is in the Active state.
        
        @param request: DisableScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.DisableScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_scaling_group(
        self,
        request: ess_20220222_models.DisableScalingGroupRequest,
    ) -> ess_20220222_models.DisableScalingGroupResponse:
        """
        @summary Disables a scaling group. If you temporarily do not require a scaling group that is in the Enabled state, you can call the DisableScalingGroup operation to disable it.
        
        @description Before you call this operation to disable a scaling group, take note of the following items:
        If scaling activities are being executed in the specified scaling group when you call this operation, these activities will continue until they are complete. However, scaling activities that are triggered after this operation is called will be rejected.
        This operation can be called only when the scaling group is in the Active state.
        
        @param request: DisableScalingGroupRequest
        @return: DisableScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_scaling_group_with_options(request, runtime)

    async def disable_scaling_group_async(
        self,
        request: ess_20220222_models.DisableScalingGroupRequest,
    ) -> ess_20220222_models.DisableScalingGroupResponse:
        """
        @summary Disables a scaling group. If you temporarily do not require a scaling group that is in the Enabled state, you can call the DisableScalingGroup operation to disable it.
        
        @description Before you call this operation to disable a scaling group, take note of the following items:
        If scaling activities are being executed in the specified scaling group when you call this operation, these activities will continue until they are complete. However, scaling activities that are triggered after this operation is called will be rejected.
        This operation can be called only when the scaling group is in the Active state.
        
        @param request: DisableScalingGroupRequest
        @return: DisableScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_scaling_group_with_options_async(request, runtime)

    def enable_alarm_with_options(
        self,
        request: ess_20220222_models.EnableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.EnableAlarmResponse:
        """
        @summary Enables an event-triggered task. If your business pattern is unpredictable or prone to unforeseen traffic spikes, you can create event-triggered tasks by associating CloudMonitor metrics to effectively monitor fluctuations in your business workload. Upon detecting that the criteria for alerts, as specified in event-triggered tasks, are fulfilled, Auto Scaling promptly issues alerts and executes the scaling rules predefined within those tasks. This process occurs within the predefined effective time windows of the tasks, thereby facilitating the automatic increase or decrease of Elastic Compute Service (ECS) instances or elastic container instances within your scaling groups. Ultimately, this mechanism ensures the dynamic optimization of resources based on real-time workload demands. If you want to reuse an event-triggered task that is in the Disabled state, you can call the EnableAlarm operation to enable it.
        
        @param request: EnableAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnableAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_alarm_with_options_async(
        self,
        request: ess_20220222_models.EnableAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.EnableAlarmResponse:
        """
        @summary Enables an event-triggered task. If your business pattern is unpredictable or prone to unforeseen traffic spikes, you can create event-triggered tasks by associating CloudMonitor metrics to effectively monitor fluctuations in your business workload. Upon detecting that the criteria for alerts, as specified in event-triggered tasks, are fulfilled, Auto Scaling promptly issues alerts and executes the scaling rules predefined within those tasks. This process occurs within the predefined effective time windows of the tasks, thereby facilitating the automatic increase or decrease of Elastic Compute Service (ECS) instances or elastic container instances within your scaling groups. Ultimately, this mechanism ensures the dynamic optimization of resources based on real-time workload demands. If you want to reuse an event-triggered task that is in the Disabled state, you can call the EnableAlarm operation to enable it.
        
        @param request: EnableAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnableAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_alarm(
        self,
        request: ess_20220222_models.EnableAlarmRequest,
    ) -> ess_20220222_models.EnableAlarmResponse:
        """
        @summary Enables an event-triggered task. If your business pattern is unpredictable or prone to unforeseen traffic spikes, you can create event-triggered tasks by associating CloudMonitor metrics to effectively monitor fluctuations in your business workload. Upon detecting that the criteria for alerts, as specified in event-triggered tasks, are fulfilled, Auto Scaling promptly issues alerts and executes the scaling rules predefined within those tasks. This process occurs within the predefined effective time windows of the tasks, thereby facilitating the automatic increase or decrease of Elastic Compute Service (ECS) instances or elastic container instances within your scaling groups. Ultimately, this mechanism ensures the dynamic optimization of resources based on real-time workload demands. If you want to reuse an event-triggered task that is in the Disabled state, you can call the EnableAlarm operation to enable it.
        
        @param request: EnableAlarmRequest
        @return: EnableAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_alarm_with_options(request, runtime)

    async def enable_alarm_async(
        self,
        request: ess_20220222_models.EnableAlarmRequest,
    ) -> ess_20220222_models.EnableAlarmResponse:
        """
        @summary Enables an event-triggered task. If your business pattern is unpredictable or prone to unforeseen traffic spikes, you can create event-triggered tasks by associating CloudMonitor metrics to effectively monitor fluctuations in your business workload. Upon detecting that the criteria for alerts, as specified in event-triggered tasks, are fulfilled, Auto Scaling promptly issues alerts and executes the scaling rules predefined within those tasks. This process occurs within the predefined effective time windows of the tasks, thereby facilitating the automatic increase or decrease of Elastic Compute Service (ECS) instances or elastic container instances within your scaling groups. Ultimately, this mechanism ensures the dynamic optimization of resources based on real-time workload demands. If you want to reuse an event-triggered task that is in the Disabled state, you can call the EnableAlarm operation to enable it.
        
        @param request: EnableAlarmRequest
        @return: EnableAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_alarm_with_options_async(request, runtime)

    def enable_scaling_group_with_options(
        self,
        request: ess_20220222_models.EnableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.EnableScalingGroupResponse:
        """
        @summary Enables a scaling group. If a scaling group is in the Disabled state and contains an instance configuration source such as a launch template or a scaling configuration, you can call the EnableScalingGroup operation to enable the scaling group. This operation permits Auto Scaling to dynamically adjust the computing power (also known as the number of instances) in the scaling group based on your business requirements.
        
        @description    You can call this operation to enable a scaling group only if the scaling group is in the Inactive state and contains an instance configuration source such as a launch temple or a scaling configuration. The instance configuration source can also be the Elastic Compute Service (ECS) instance that you specified when you created the scaling group. If the preceding requirements are not met, the operation will fail.
        *\
        *Note** A scaling group can have only one active instance configuration source at a time. When you call this operation to enable a scaling group, you can specify a scaling configuration or a launch template for the scaling group. If the scaling group already have an instance configuration source defined prior to your calling, the scaling configuration or launch template specified within your request will supersede the existing scaling configuration or launch template.
        If you specify InstanceId.N to add to the scaling group within your request, Auto Scaling will check whether the addition of InstanceId.N will cause the total number of ECS instances in the scaling group to fall outside the boundaries specified by MinSize and MaxSize after you call this operation.
        If the call results in the total number of ECS instances dropping below the value of MinSize, Auto Scaling proactively creates pay-as-you-go ECS instances to ensure that the total number reaches the minimum threshold. For example, if you set MinSize to 5 when you created a scaling group and include InstanceId.N within your request to add two ECS instances when you attempt to enable the scaling group, Auto Scaling creates three more ECS instances in the scaling group after the two ECS instances are added.
        If the call results in the total number of ECS instances exceeding the value of MaxSize, the operation fails.
        
        @param request: EnableScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.load_balancer_weights):
            query['LoadBalancerWeights'] = request.load_balancer_weights
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnableScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_scaling_group_with_options_async(
        self,
        request: ess_20220222_models.EnableScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.EnableScalingGroupResponse:
        """
        @summary Enables a scaling group. If a scaling group is in the Disabled state and contains an instance configuration source such as a launch template or a scaling configuration, you can call the EnableScalingGroup operation to enable the scaling group. This operation permits Auto Scaling to dynamically adjust the computing power (also known as the number of instances) in the scaling group based on your business requirements.
        
        @description    You can call this operation to enable a scaling group only if the scaling group is in the Inactive state and contains an instance configuration source such as a launch temple or a scaling configuration. The instance configuration source can also be the Elastic Compute Service (ECS) instance that you specified when you created the scaling group. If the preceding requirements are not met, the operation will fail.
        *\
        *Note** A scaling group can have only one active instance configuration source at a time. When you call this operation to enable a scaling group, you can specify a scaling configuration or a launch template for the scaling group. If the scaling group already have an instance configuration source defined prior to your calling, the scaling configuration or launch template specified within your request will supersede the existing scaling configuration or launch template.
        If you specify InstanceId.N to add to the scaling group within your request, Auto Scaling will check whether the addition of InstanceId.N will cause the total number of ECS instances in the scaling group to fall outside the boundaries specified by MinSize and MaxSize after you call this operation.
        If the call results in the total number of ECS instances dropping below the value of MinSize, Auto Scaling proactively creates pay-as-you-go ECS instances to ensure that the total number reaches the minimum threshold. For example, if you set MinSize to 5 when you created a scaling group and include InstanceId.N within your request to add two ECS instances when you attempt to enable the scaling group, Auto Scaling creates three more ECS instances in the scaling group after the two ECS instances are added.
        If the call results in the total number of ECS instances exceeding the value of MaxSize, the operation fails.
        
        @param request: EnableScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.load_balancer_weights):
            query['LoadBalancerWeights'] = request.load_balancer_weights
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnableScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_scaling_group(
        self,
        request: ess_20220222_models.EnableScalingGroupRequest,
    ) -> ess_20220222_models.EnableScalingGroupResponse:
        """
        @summary Enables a scaling group. If a scaling group is in the Disabled state and contains an instance configuration source such as a launch template or a scaling configuration, you can call the EnableScalingGroup operation to enable the scaling group. This operation permits Auto Scaling to dynamically adjust the computing power (also known as the number of instances) in the scaling group based on your business requirements.
        
        @description    You can call this operation to enable a scaling group only if the scaling group is in the Inactive state and contains an instance configuration source such as a launch temple or a scaling configuration. The instance configuration source can also be the Elastic Compute Service (ECS) instance that you specified when you created the scaling group. If the preceding requirements are not met, the operation will fail.
        *\
        *Note** A scaling group can have only one active instance configuration source at a time. When you call this operation to enable a scaling group, you can specify a scaling configuration or a launch template for the scaling group. If the scaling group already have an instance configuration source defined prior to your calling, the scaling configuration or launch template specified within your request will supersede the existing scaling configuration or launch template.
        If you specify InstanceId.N to add to the scaling group within your request, Auto Scaling will check whether the addition of InstanceId.N will cause the total number of ECS instances in the scaling group to fall outside the boundaries specified by MinSize and MaxSize after you call this operation.
        If the call results in the total number of ECS instances dropping below the value of MinSize, Auto Scaling proactively creates pay-as-you-go ECS instances to ensure that the total number reaches the minimum threshold. For example, if you set MinSize to 5 when you created a scaling group and include InstanceId.N within your request to add two ECS instances when you attempt to enable the scaling group, Auto Scaling creates three more ECS instances in the scaling group after the two ECS instances are added.
        If the call results in the total number of ECS instances exceeding the value of MaxSize, the operation fails.
        
        @param request: EnableScalingGroupRequest
        @return: EnableScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_scaling_group_with_options(request, runtime)

    async def enable_scaling_group_async(
        self,
        request: ess_20220222_models.EnableScalingGroupRequest,
    ) -> ess_20220222_models.EnableScalingGroupResponse:
        """
        @summary Enables a scaling group. If a scaling group is in the Disabled state and contains an instance configuration source such as a launch template or a scaling configuration, you can call the EnableScalingGroup operation to enable the scaling group. This operation permits Auto Scaling to dynamically adjust the computing power (also known as the number of instances) in the scaling group based on your business requirements.
        
        @description    You can call this operation to enable a scaling group only if the scaling group is in the Inactive state and contains an instance configuration source such as a launch temple or a scaling configuration. The instance configuration source can also be the Elastic Compute Service (ECS) instance that you specified when you created the scaling group. If the preceding requirements are not met, the operation will fail.
        *\
        *Note** A scaling group can have only one active instance configuration source at a time. When you call this operation to enable a scaling group, you can specify a scaling configuration or a launch template for the scaling group. If the scaling group already have an instance configuration source defined prior to your calling, the scaling configuration or launch template specified within your request will supersede the existing scaling configuration or launch template.
        If you specify InstanceId.N to add to the scaling group within your request, Auto Scaling will check whether the addition of InstanceId.N will cause the total number of ECS instances in the scaling group to fall outside the boundaries specified by MinSize and MaxSize after you call this operation.
        If the call results in the total number of ECS instances dropping below the value of MinSize, Auto Scaling proactively creates pay-as-you-go ECS instances to ensure that the total number reaches the minimum threshold. For example, if you set MinSize to 5 when you created a scaling group and include InstanceId.N within your request to add two ECS instances when you attempt to enable the scaling group, Auto Scaling creates three more ECS instances in the scaling group after the two ECS instances are added.
        If the call results in the total number of ECS instances exceeding the value of MaxSize, the operation fails.
        
        @param request: EnableScalingGroupRequest
        @return: EnableScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_scaling_group_with_options_async(request, runtime)

    def enter_standby_with_options(
        self,
        request: ess_20220222_models.EnterStandbyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.EnterStandbyResponse:
        """
        @summary Puts an Elastic Compute Service (ECS) instance into the Standby state.
        
        @description ## Description
        If you call the operation to put an ECS instance in a scaling group that is associated with a Classic Load Balancer (CLB) instance into the Standby state, the weight of the ECS instance as a backend server of the CLB instance is set to 0.
        You can remove an instance that is in the Standby state from a scaling group, and then release the instance.
        ECS instances that are in the Standby state are not removed from the scaling group during scale-in activities triggered by event-triggered tasks.
        If Auto Scaling considers an ECS instance that is in the Standby state unhealthy, for example, the ECS instance is being stopped or being restarted, Auto Scaling does not update the health status of the ECS instance or trigger scale-in activities to remove the ECS instance from the scaling group. Auto Scaling updates the health status of the ECS instance only when the ECS instance is no longer in the Standby state.
        
        @param request: EnterStandbyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterStandbyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnterStandby',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnterStandbyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enter_standby_with_options_async(
        self,
        request: ess_20220222_models.EnterStandbyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.EnterStandbyResponse:
        """
        @summary Puts an Elastic Compute Service (ECS) instance into the Standby state.
        
        @description ## Description
        If you call the operation to put an ECS instance in a scaling group that is associated with a Classic Load Balancer (CLB) instance into the Standby state, the weight of the ECS instance as a backend server of the CLB instance is set to 0.
        You can remove an instance that is in the Standby state from a scaling group, and then release the instance.
        ECS instances that are in the Standby state are not removed from the scaling group during scale-in activities triggered by event-triggered tasks.
        If Auto Scaling considers an ECS instance that is in the Standby state unhealthy, for example, the ECS instance is being stopped or being restarted, Auto Scaling does not update the health status of the ECS instance or trigger scale-in activities to remove the ECS instance from the scaling group. Auto Scaling updates the health status of the ECS instance only when the ECS instance is no longer in the Standby state.
        
        @param request: EnterStandbyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnterStandbyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnterStandby',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.EnterStandbyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enter_standby(
        self,
        request: ess_20220222_models.EnterStandbyRequest,
    ) -> ess_20220222_models.EnterStandbyResponse:
        """
        @summary Puts an Elastic Compute Service (ECS) instance into the Standby state.
        
        @description ## Description
        If you call the operation to put an ECS instance in a scaling group that is associated with a Classic Load Balancer (CLB) instance into the Standby state, the weight of the ECS instance as a backend server of the CLB instance is set to 0.
        You can remove an instance that is in the Standby state from a scaling group, and then release the instance.
        ECS instances that are in the Standby state are not removed from the scaling group during scale-in activities triggered by event-triggered tasks.
        If Auto Scaling considers an ECS instance that is in the Standby state unhealthy, for example, the ECS instance is being stopped or being restarted, Auto Scaling does not update the health status of the ECS instance or trigger scale-in activities to remove the ECS instance from the scaling group. Auto Scaling updates the health status of the ECS instance only when the ECS instance is no longer in the Standby state.
        
        @param request: EnterStandbyRequest
        @return: EnterStandbyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enter_standby_with_options(request, runtime)

    async def enter_standby_async(
        self,
        request: ess_20220222_models.EnterStandbyRequest,
    ) -> ess_20220222_models.EnterStandbyResponse:
        """
        @summary Puts an Elastic Compute Service (ECS) instance into the Standby state.
        
        @description ## Description
        If you call the operation to put an ECS instance in a scaling group that is associated with a Classic Load Balancer (CLB) instance into the Standby state, the weight of the ECS instance as a backend server of the CLB instance is set to 0.
        You can remove an instance that is in the Standby state from a scaling group, and then release the instance.
        ECS instances that are in the Standby state are not removed from the scaling group during scale-in activities triggered by event-triggered tasks.
        If Auto Scaling considers an ECS instance that is in the Standby state unhealthy, for example, the ECS instance is being stopped or being restarted, Auto Scaling does not update the health status of the ECS instance or trigger scale-in activities to remove the ECS instance from the scaling group. Auto Scaling updates the health status of the ECS instance only when the ECS instance is no longer in the Standby state.
        
        @param request: EnterStandbyRequest
        @return: EnterStandbyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enter_standby_with_options_async(request, runtime)

    def execute_scaling_rule_with_options(
        self,
        request: ess_20220222_models.ExecuteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ExecuteScalingRuleResponse:
        """
        @summary Executes a scaling rule. To adjust the number of Elastic Compute Service (ECS) instances or elastic container instances, you can manually execute a scaling rule or enable Auto Scaling to execute a scaling rule. You can call the ExecuteScalingRule operation to execute simple scaling rules or step scaling rules. Auto Scaling automatically executes target tracking scaling rules and predictive scaling rules on your behalf without requiring explicit execution calls.
        
        @description Before you call this operation, take note of the following items:
        The scaling group is in the Active state.
        No scaling activities in the scaling group are in progress.
        If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the ScalingActivityId parameter in the response.
        If the addition of a specified number of Elastic Compute Service (ECS) instances to a scaling group causes the total number of ECS instances in the scaling group to exceed the maximum number of instances allowed, Auto Scaling adds only a specific number of ECS instances to ensure that the total number of instances is equal to the maximum number of instances.
        If the removal of a specified number of ECS instances from a scaling group causes the total number of ECS instances in the scaling group to drop below the minimum number of instances allowed, Auto Scaling removes only a specific number of ECS instances to ensure that the total number of instances is equal to the minimum number of instances.
        You can specify only a limited number of ECS instances in each adjustment. For more information, see the description of the AdjustmentValue parameter in the CreateScalingRule topic.
        
        @param request: ExecuteScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.breach_threshold):
            query['BreachThreshold'] = request.breach_threshold
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.metric_value):
            query['MetricValue'] = request.metric_value
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_rule_ari):
            query['ScalingRuleAri'] = request.scaling_rule_ari
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ExecuteScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_scaling_rule_with_options_async(
        self,
        request: ess_20220222_models.ExecuteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ExecuteScalingRuleResponse:
        """
        @summary Executes a scaling rule. To adjust the number of Elastic Compute Service (ECS) instances or elastic container instances, you can manually execute a scaling rule or enable Auto Scaling to execute a scaling rule. You can call the ExecuteScalingRule operation to execute simple scaling rules or step scaling rules. Auto Scaling automatically executes target tracking scaling rules and predictive scaling rules on your behalf without requiring explicit execution calls.
        
        @description Before you call this operation, take note of the following items:
        The scaling group is in the Active state.
        No scaling activities in the scaling group are in progress.
        If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the ScalingActivityId parameter in the response.
        If the addition of a specified number of Elastic Compute Service (ECS) instances to a scaling group causes the total number of ECS instances in the scaling group to exceed the maximum number of instances allowed, Auto Scaling adds only a specific number of ECS instances to ensure that the total number of instances is equal to the maximum number of instances.
        If the removal of a specified number of ECS instances from a scaling group causes the total number of ECS instances in the scaling group to drop below the minimum number of instances allowed, Auto Scaling removes only a specific number of ECS instances to ensure that the total number of instances is equal to the minimum number of instances.
        You can specify only a limited number of ECS instances in each adjustment. For more information, see the description of the AdjustmentValue parameter in the CreateScalingRule topic.
        
        @param request: ExecuteScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.breach_threshold):
            query['BreachThreshold'] = request.breach_threshold
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.metric_value):
            query['MetricValue'] = request.metric_value
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_rule_ari):
            query['ScalingRuleAri'] = request.scaling_rule_ari
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ExecuteScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_scaling_rule(
        self,
        request: ess_20220222_models.ExecuteScalingRuleRequest,
    ) -> ess_20220222_models.ExecuteScalingRuleResponse:
        """
        @summary Executes a scaling rule. To adjust the number of Elastic Compute Service (ECS) instances or elastic container instances, you can manually execute a scaling rule or enable Auto Scaling to execute a scaling rule. You can call the ExecuteScalingRule operation to execute simple scaling rules or step scaling rules. Auto Scaling automatically executes target tracking scaling rules and predictive scaling rules on your behalf without requiring explicit execution calls.
        
        @description Before you call this operation, take note of the following items:
        The scaling group is in the Active state.
        No scaling activities in the scaling group are in progress.
        If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the ScalingActivityId parameter in the response.
        If the addition of a specified number of Elastic Compute Service (ECS) instances to a scaling group causes the total number of ECS instances in the scaling group to exceed the maximum number of instances allowed, Auto Scaling adds only a specific number of ECS instances to ensure that the total number of instances is equal to the maximum number of instances.
        If the removal of a specified number of ECS instances from a scaling group causes the total number of ECS instances in the scaling group to drop below the minimum number of instances allowed, Auto Scaling removes only a specific number of ECS instances to ensure that the total number of instances is equal to the minimum number of instances.
        You can specify only a limited number of ECS instances in each adjustment. For more information, see the description of the AdjustmentValue parameter in the CreateScalingRule topic.
        
        @param request: ExecuteScalingRuleRequest
        @return: ExecuteScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_scaling_rule_with_options(request, runtime)

    async def execute_scaling_rule_async(
        self,
        request: ess_20220222_models.ExecuteScalingRuleRequest,
    ) -> ess_20220222_models.ExecuteScalingRuleResponse:
        """
        @summary Executes a scaling rule. To adjust the number of Elastic Compute Service (ECS) instances or elastic container instances, you can manually execute a scaling rule or enable Auto Scaling to execute a scaling rule. You can call the ExecuteScalingRule operation to execute simple scaling rules or step scaling rules. Auto Scaling automatically executes target tracking scaling rules and predictive scaling rules on your behalf without requiring explicit execution calls.
        
        @description Before you call this operation, take note of the following items:
        The scaling group is in the Active state.
        No scaling activities in the scaling group are in progress.
        If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities even before the cooldown time expires.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity by using the value of the ScalingActivityId parameter in the response.
        If the addition of a specified number of Elastic Compute Service (ECS) instances to a scaling group causes the total number of ECS instances in the scaling group to exceed the maximum number of instances allowed, Auto Scaling adds only a specific number of ECS instances to ensure that the total number of instances is equal to the maximum number of instances.
        If the removal of a specified number of ECS instances from a scaling group causes the total number of ECS instances in the scaling group to drop below the minimum number of instances allowed, Auto Scaling removes only a specific number of ECS instances to ensure that the total number of instances is equal to the minimum number of instances.
        You can specify only a limited number of ECS instances in each adjustment. For more information, see the description of the AdjustmentValue parameter in the CreateScalingRule topic.
        
        @param request: ExecuteScalingRuleRequest
        @return: ExecuteScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_scaling_rule_with_options_async(request, runtime)

    def exit_standby_with_options(
        self,
        request: ess_20220222_models.ExitStandbyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ExitStandbyResponse:
        """
        @summary Removes an instance from the Standby state. When a scale-in event is triggered in a scaling group, Auto Scaling does not remove Elastic Compute Service (ECS) instances or elastic container instances that are in the Standby state from the scaling group. If you want to restart the instances that are in the Standby state, you can call the ExitStandby operation to remove the instances from the Standby state and put them into the In Service state.
        
        @description After ECS instances or elastic container instances are removed from the Standby state, the following rules apply:
        The ECS instances or elastic container instances enter the In Service state.
        The default weight of each ECS instance or elastic container instance as a backend server of the attached load balancer is 50.
        If you stop or restart the ECS instances or elastic container instances, the health check status of the instances will be updated.
        When a scale-in event is triggered, Auto Scaling may remove the ECS instances or elastic container instances from the scaling group.
        
        @param request: ExitStandbyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExitStandbyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExitStandby',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ExitStandbyResponse(),
            self.call_api(params, req, runtime)
        )

    async def exit_standby_with_options_async(
        self,
        request: ess_20220222_models.ExitStandbyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ExitStandbyResponse:
        """
        @summary Removes an instance from the Standby state. When a scale-in event is triggered in a scaling group, Auto Scaling does not remove Elastic Compute Service (ECS) instances or elastic container instances that are in the Standby state from the scaling group. If you want to restart the instances that are in the Standby state, you can call the ExitStandby operation to remove the instances from the Standby state and put them into the In Service state.
        
        @description After ECS instances or elastic container instances are removed from the Standby state, the following rules apply:
        The ECS instances or elastic container instances enter the In Service state.
        The default weight of each ECS instance or elastic container instance as a backend server of the attached load balancer is 50.
        If you stop or restart the ECS instances or elastic container instances, the health check status of the instances will be updated.
        When a scale-in event is triggered, Auto Scaling may remove the ECS instances or elastic container instances from the scaling group.
        
        @param request: ExitStandbyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExitStandbyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.async_):
            query['Async'] = request.async_
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExitStandby',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ExitStandbyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exit_standby(
        self,
        request: ess_20220222_models.ExitStandbyRequest,
    ) -> ess_20220222_models.ExitStandbyResponse:
        """
        @summary Removes an instance from the Standby state. When a scale-in event is triggered in a scaling group, Auto Scaling does not remove Elastic Compute Service (ECS) instances or elastic container instances that are in the Standby state from the scaling group. If you want to restart the instances that are in the Standby state, you can call the ExitStandby operation to remove the instances from the Standby state and put them into the In Service state.
        
        @description After ECS instances or elastic container instances are removed from the Standby state, the following rules apply:
        The ECS instances or elastic container instances enter the In Service state.
        The default weight of each ECS instance or elastic container instance as a backend server of the attached load balancer is 50.
        If you stop or restart the ECS instances or elastic container instances, the health check status of the instances will be updated.
        When a scale-in event is triggered, Auto Scaling may remove the ECS instances or elastic container instances from the scaling group.
        
        @param request: ExitStandbyRequest
        @return: ExitStandbyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.exit_standby_with_options(request, runtime)

    async def exit_standby_async(
        self,
        request: ess_20220222_models.ExitStandbyRequest,
    ) -> ess_20220222_models.ExitStandbyResponse:
        """
        @summary Removes an instance from the Standby state. When a scale-in event is triggered in a scaling group, Auto Scaling does not remove Elastic Compute Service (ECS) instances or elastic container instances that are in the Standby state from the scaling group. If you want to restart the instances that are in the Standby state, you can call the ExitStandby operation to remove the instances from the Standby state and put them into the In Service state.
        
        @description After ECS instances or elastic container instances are removed from the Standby state, the following rules apply:
        The ECS instances or elastic container instances enter the In Service state.
        The default weight of each ECS instance or elastic container instance as a backend server of the attached load balancer is 50.
        If you stop or restart the ECS instances or elastic container instances, the health check status of the instances will be updated.
        When a scale-in event is triggered, Auto Scaling may remove the ECS instances or elastic container instances from the scaling group.
        
        @param request: ExitStandbyRequest
        @return: ExitStandbyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.exit_standby_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: ess_20220222_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ListTagKeysResponse:
        """
        @summary Queries the tag keys added to Auto Scaling resources. Querying tag keys facilitates easier classification, identification, and monitoring of your Auto Scaling resources, thereby enhancing the flexibility and convenience of your resource management processes.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: ess_20220222_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ListTagKeysResponse:
        """
        @summary Queries the tag keys added to Auto Scaling resources. Querying tag keys facilitates easier classification, identification, and monitoring of your Auto Scaling resources, thereby enhancing the flexibility and convenience of your resource management processes.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: ess_20220222_models.ListTagKeysRequest,
    ) -> ess_20220222_models.ListTagKeysResponse:
        """
        @summary Queries the tag keys added to Auto Scaling resources. Querying tag keys facilitates easier classification, identification, and monitoring of your Auto Scaling resources, thereby enhancing the flexibility and convenience of your resource management processes.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: ess_20220222_models.ListTagKeysRequest,
    ) -> ess_20220222_models.ListTagKeysResponse:
        """
        @summary Queries the tag keys added to Auto Scaling resources. Querying tag keys facilitates easier classification, identification, and monitoring of your Auto Scaling resources, thereby enhancing the flexibility and convenience of your resource management processes.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ess_20220222_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ListTagResourcesResponse:
        """
        @summary Queries tags. You can call the ListTagResources operation to query tags that are added to Auto Scaling resources, thereby clarifying resource utilization and facilitating efficient management. This operation aids in the automation of resource categorization and permission management processes.
        
        @description    Specify at least one of the following request parameters: `ResourceIds` and `Tags`. `Tags.Key` and `Tags.Value` are used to specify the query objects.
        If you provide both `ResourceIds` and `Tags` in your request, the response will exclusively include Auto Scaling resources that satisfy the criteria set by these parameters, ensuring targeted and precise information retrieval.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ess_20220222_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ListTagResourcesResponse:
        """
        @summary Queries tags. You can call the ListTagResources operation to query tags that are added to Auto Scaling resources, thereby clarifying resource utilization and facilitating efficient management. This operation aids in the automation of resource categorization and permission management processes.
        
        @description    Specify at least one of the following request parameters: `ResourceIds` and `Tags`. `Tags.Key` and `Tags.Value` are used to specify the query objects.
        If you provide both `ResourceIds` and `Tags` in your request, the response will exclusively include Auto Scaling resources that satisfy the criteria set by these parameters, ensuring targeted and precise information retrieval.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: ess_20220222_models.ListTagResourcesRequest,
    ) -> ess_20220222_models.ListTagResourcesResponse:
        """
        @summary Queries tags. You can call the ListTagResources operation to query tags that are added to Auto Scaling resources, thereby clarifying resource utilization and facilitating efficient management. This operation aids in the automation of resource categorization and permission management processes.
        
        @description    Specify at least one of the following request parameters: `ResourceIds` and `Tags`. `Tags.Key` and `Tags.Value` are used to specify the query objects.
        If you provide both `ResourceIds` and `Tags` in your request, the response will exclusively include Auto Scaling resources that satisfy the criteria set by these parameters, ensuring targeted and precise information retrieval.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ess_20220222_models.ListTagResourcesRequest,
    ) -> ess_20220222_models.ListTagResourcesResponse:
        """
        @summary Queries tags. You can call the ListTagResources operation to query tags that are added to Auto Scaling resources, thereby clarifying resource utilization and facilitating efficient management. This operation aids in the automation of resource categorization and permission management processes.
        
        @description    Specify at least one of the following request parameters: `ResourceIds` and `Tags`. `Tags.Key` and `Tags.Value` are used to specify the query objects.
        If you provide both `ResourceIds` and `Tags` in your request, the response will exclusively include Auto Scaling resources that satisfy the criteria set by these parameters, ensuring targeted and precise information retrieval.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: ess_20220222_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ListTagValuesResponse:
        """
        @summary Queries the tag keys associated with Auto Scaling resources to facilitate a deeper comprehension of those resources. By doing so, you can categorize and manage your Auto Scaling resources more efficiently.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: ess_20220222_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ListTagValuesResponse:
        """
        @summary Queries the tag keys associated with Auto Scaling resources to facilitate a deeper comprehension of those resources. By doing so, you can categorize and manage your Auto Scaling resources more efficiently.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: ess_20220222_models.ListTagValuesRequest,
    ) -> ess_20220222_models.ListTagValuesResponse:
        """
        @summary Queries the tag keys associated with Auto Scaling resources to facilitate a deeper comprehension of those resources. By doing so, you can categorize and manage your Auto Scaling resources more efficiently.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: ess_20220222_models.ListTagValuesRequest,
    ) -> ess_20220222_models.ListTagValuesResponse:
        """
        @summary Queries the tag keys associated with Auto Scaling resources to facilitate a deeper comprehension of those resources. By doing so, you can categorize and manage your Auto Scaling resources more efficiently.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def modify_alarm_with_options(
        self,
        request: ess_20220222_models.ModifyAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyAlarmResponse:
        """
        @summary Modifies an event-triggered task.
        
        @description    If you set the MetricType parameter to custom, you must report your custom metrics to CloudMonitor before you can create event-triggered tasks by using the custom metrics. For more information, see [Custom monitoring event-triggered tasks](https://help.aliyun.com/document_detail/74861.html).
        When you create an event-triggered task, you must specify the MetricName, DimensionKey, and DimensionValue parameters to determine the range of statistics that you want to aggregate for the metrics of the scaling group. For example, you can specify the user_id and scaling_group dimensions for an event-triggered task to aggregate monitoring data of all Elastic Compute Service (ECS) instances or elastic container instances in a scaling group within an Alibaba Cloud account.
        If you set the MetricType parameter to custom, the valid values are your custom metrics.
        For information about the metrics that are supported if you set the MetricType parameter to system, see[ Event-triggered task for system monitoring](https://help.aliyun.com/document_detail/74854.html).
        > The user_id and scaling_group dimensions are automatically populated. You need to only specify the device and state dimensions. For more information, see the `DimensionKey` and `DimensionValue` parameters in the "Request parameters" section of this topic.
        
        @param request: ModifyAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_actions):
            query['AlarmActions'] = request.alarm_actions
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective):
            query['Effective'] = request.effective
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.expressions):
            query['Expressions'] = request.expressions
        if not UtilClient.is_unset(request.expressions_logic_operator):
            query['ExpressionsLogicOperator'] = request.expressions_logic_operator
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.statistics):
            query['Statistics'] = request.statistics
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_alarm_with_options_async(
        self,
        request: ess_20220222_models.ModifyAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyAlarmResponse:
        """
        @summary Modifies an event-triggered task.
        
        @description    If you set the MetricType parameter to custom, you must report your custom metrics to CloudMonitor before you can create event-triggered tasks by using the custom metrics. For more information, see [Custom monitoring event-triggered tasks](https://help.aliyun.com/document_detail/74861.html).
        When you create an event-triggered task, you must specify the MetricName, DimensionKey, and DimensionValue parameters to determine the range of statistics that you want to aggregate for the metrics of the scaling group. For example, you can specify the user_id and scaling_group dimensions for an event-triggered task to aggregate monitoring data of all Elastic Compute Service (ECS) instances or elastic container instances in a scaling group within an Alibaba Cloud account.
        If you set the MetricType parameter to custom, the valid values are your custom metrics.
        For information about the metrics that are supported if you set the MetricType parameter to system, see[ Event-triggered task for system monitoring](https://help.aliyun.com/document_detail/74854.html).
        > The user_id and scaling_group dimensions are automatically populated. You need to only specify the device and state dimensions. For more information, see the `DimensionKey` and `DimensionValue` parameters in the "Request parameters" section of this topic.
        
        @param request: ModifyAlarmRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAlarmResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_actions):
            query['AlarmActions'] = request.alarm_actions
        if not UtilClient.is_unset(request.alarm_task_id):
            query['AlarmTaskId'] = request.alarm_task_id
        if not UtilClient.is_unset(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.effective):
            query['Effective'] = request.effective
        if not UtilClient.is_unset(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not UtilClient.is_unset(request.expressions):
            query['Expressions'] = request.expressions
        if not UtilClient.is_unset(request.expressions_logic_operator):
            query['ExpressionsLogicOperator'] = request.expressions_logic_operator
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.statistics):
            query['Statistics'] = request.statistics
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAlarm',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_alarm(
        self,
        request: ess_20220222_models.ModifyAlarmRequest,
    ) -> ess_20220222_models.ModifyAlarmResponse:
        """
        @summary Modifies an event-triggered task.
        
        @description    If you set the MetricType parameter to custom, you must report your custom metrics to CloudMonitor before you can create event-triggered tasks by using the custom metrics. For more information, see [Custom monitoring event-triggered tasks](https://help.aliyun.com/document_detail/74861.html).
        When you create an event-triggered task, you must specify the MetricName, DimensionKey, and DimensionValue parameters to determine the range of statistics that you want to aggregate for the metrics of the scaling group. For example, you can specify the user_id and scaling_group dimensions for an event-triggered task to aggregate monitoring data of all Elastic Compute Service (ECS) instances or elastic container instances in a scaling group within an Alibaba Cloud account.
        If you set the MetricType parameter to custom, the valid values are your custom metrics.
        For information about the metrics that are supported if you set the MetricType parameter to system, see[ Event-triggered task for system monitoring](https://help.aliyun.com/document_detail/74854.html).
        > The user_id and scaling_group dimensions are automatically populated. You need to only specify the device and state dimensions. For more information, see the `DimensionKey` and `DimensionValue` parameters in the "Request parameters" section of this topic.
        
        @param request: ModifyAlarmRequest
        @return: ModifyAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_alarm_with_options(request, runtime)

    async def modify_alarm_async(
        self,
        request: ess_20220222_models.ModifyAlarmRequest,
    ) -> ess_20220222_models.ModifyAlarmResponse:
        """
        @summary Modifies an event-triggered task.
        
        @description    If you set the MetricType parameter to custom, you must report your custom metrics to CloudMonitor before you can create event-triggered tasks by using the custom metrics. For more information, see [Custom monitoring event-triggered tasks](https://help.aliyun.com/document_detail/74861.html).
        When you create an event-triggered task, you must specify the MetricName, DimensionKey, and DimensionValue parameters to determine the range of statistics that you want to aggregate for the metrics of the scaling group. For example, you can specify the user_id and scaling_group dimensions for an event-triggered task to aggregate monitoring data of all Elastic Compute Service (ECS) instances or elastic container instances in a scaling group within an Alibaba Cloud account.
        If you set the MetricType parameter to custom, the valid values are your custom metrics.
        For information about the metrics that are supported if you set the MetricType parameter to system, see[ Event-triggered task for system monitoring](https://help.aliyun.com/document_detail/74854.html).
        > The user_id and scaling_group dimensions are automatically populated. You need to only specify the device and state dimensions. For more information, see the `DimensionKey` and `DimensionValue` parameters in the "Request parameters" section of this topic.
        
        @param request: ModifyAlarmRequest
        @return: ModifyAlarmResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_alarm_with_options_async(request, runtime)

    def modify_alert_configuration_with_options(
        self,
        request: ess_20220222_models.ModifyAlertConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyAlertConfigurationResponse:
        """
        @summary Sets the status of scaling activities that prompt text message or email notifications.
        
        @param request: ModifyAlertConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAlertConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scale_statuses):
            query['ScaleStatuses'] = request.scale_statuses
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAlertConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyAlertConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_alert_configuration_with_options_async(
        self,
        request: ess_20220222_models.ModifyAlertConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyAlertConfigurationResponse:
        """
        @summary Sets the status of scaling activities that prompt text message or email notifications.
        
        @param request: ModifyAlertConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAlertConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scale_statuses):
            query['ScaleStatuses'] = request.scale_statuses
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAlertConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyAlertConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_alert_configuration(
        self,
        request: ess_20220222_models.ModifyAlertConfigurationRequest,
    ) -> ess_20220222_models.ModifyAlertConfigurationResponse:
        """
        @summary Sets the status of scaling activities that prompt text message or email notifications.
        
        @param request: ModifyAlertConfigurationRequest
        @return: ModifyAlertConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_alert_configuration_with_options(request, runtime)

    async def modify_alert_configuration_async(
        self,
        request: ess_20220222_models.ModifyAlertConfigurationRequest,
    ) -> ess_20220222_models.ModifyAlertConfigurationResponse:
        """
        @summary Sets the status of scaling activities that prompt text message or email notifications.
        
        @param request: ModifyAlertConfigurationRequest
        @return: ModifyAlertConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_alert_configuration_with_options_async(request, runtime)

    def modify_eci_scaling_configuration_with_options(
        self,
        request: ess_20220222_models.ModifyEciScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyEciScalingConfigurationResponse:
        """
        @summary Modifies a scaling configuration for a scaling group that contains elastic container instances.
        
        @description If you want to change the name of a scaling configuration in a scaling group, make sure that the new name is unique within the scaling group.
        
        @param request: ModifyEciScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not UtilClient.is_unset(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not UtilClient.is_unset(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not UtilClient.is_unset(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not UtilClient.is_unset(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not UtilClient.is_unset(request.containers):
            query['Containers'] = request.containers
        if not UtilClient.is_unset(request.containers_update_type):
            query['ContainersUpdateType'] = request.containers_update_type
        if not UtilClient.is_unset(request.cost_optimization):
            query['CostOptimization'] = request.cost_optimization
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not UtilClient.is_unset(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not UtilClient.is_unset(request.data_cache_bucket):
            query['DataCacheBucket'] = request.data_cache_bucket
        if not UtilClient.is_unset(request.data_cache_bursting_enabled):
            query['DataCacheBurstingEnabled'] = request.data_cache_bursting_enabled
        if not UtilClient.is_unset(request.data_cache_pl):
            query['DataCachePL'] = request.data_cache_pl
        if not UtilClient.is_unset(request.data_cache_provisioned_iops):
            query['DataCacheProvisionedIops'] = request.data_cache_provisioned_iops
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dns_config_name_servers):
            query['DnsConfigNameServers'] = request.dns_config_name_servers
        if not UtilClient.is_unset(request.dns_config_options):
            query['DnsConfigOptions'] = request.dns_config_options
        if not UtilClient.is_unset(request.dns_config_searchs):
            query['DnsConfigSearchs'] = request.dns_config_searchs
        if not UtilClient.is_unset(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not UtilClient.is_unset(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.host_aliases):
            query['HostAliases'] = request.host_aliases
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not UtilClient.is_unset(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not UtilClient.is_unset(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not UtilClient.is_unset(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.ntp_servers):
            query['NtpServers'] = request.ntp_servers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.security_context_sys_ctls):
            query['SecurityContextSysCtls'] = request.security_context_sys_ctls
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.volumes):
            query['Volumes'] = request.volumes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyEciScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_eci_scaling_configuration_with_options_async(
        self,
        request: ess_20220222_models.ModifyEciScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyEciScalingConfigurationResponse:
        """
        @summary Modifies a scaling configuration for a scaling group that contains elastic container instances.
        
        @description If you want to change the name of a scaling configuration in a scaling group, make sure that the new name is unique within the scaling group.
        
        @param request: ModifyEciScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyEciScalingConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acr_registry_infos):
            query['AcrRegistryInfos'] = request.acr_registry_infos
        if not UtilClient.is_unset(request.active_deadline_seconds):
            query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        if not UtilClient.is_unset(request.auto_create_eip):
            query['AutoCreateEip'] = request.auto_create_eip
        if not UtilClient.is_unset(request.auto_match_image_cache):
            query['AutoMatchImageCache'] = request.auto_match_image_cache
        if not UtilClient.is_unset(request.container_group_name):
            query['ContainerGroupName'] = request.container_group_name
        if not UtilClient.is_unset(request.containers):
            query['Containers'] = request.containers
        if not UtilClient.is_unset(request.containers_update_type):
            query['ContainersUpdateType'] = request.containers_update_type
        if not UtilClient.is_unset(request.cost_optimization):
            query['CostOptimization'] = request.cost_optimization
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.cpu_options_core):
            query['CpuOptionsCore'] = request.cpu_options_core
        if not UtilClient.is_unset(request.cpu_options_threads_per_core):
            query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        if not UtilClient.is_unset(request.data_cache_bucket):
            query['DataCacheBucket'] = request.data_cache_bucket
        if not UtilClient.is_unset(request.data_cache_bursting_enabled):
            query['DataCacheBurstingEnabled'] = request.data_cache_bursting_enabled
        if not UtilClient.is_unset(request.data_cache_pl):
            query['DataCachePL'] = request.data_cache_pl
        if not UtilClient.is_unset(request.data_cache_provisioned_iops):
            query['DataCacheProvisionedIops'] = request.data_cache_provisioned_iops
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dns_config_name_servers):
            query['DnsConfigNameServers'] = request.dns_config_name_servers
        if not UtilClient.is_unset(request.dns_config_options):
            query['DnsConfigOptions'] = request.dns_config_options
        if not UtilClient.is_unset(request.dns_config_searchs):
            query['DnsConfigSearchs'] = request.dns_config_searchs
        if not UtilClient.is_unset(request.dns_policy):
            query['DnsPolicy'] = request.dns_policy
        if not UtilClient.is_unset(request.egress_bandwidth):
            query['EgressBandwidth'] = request.egress_bandwidth
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.enable_sls):
            query['EnableSls'] = request.enable_sls
        if not UtilClient.is_unset(request.ephemeral_storage):
            query['EphemeralStorage'] = request.ephemeral_storage
        if not UtilClient.is_unset(request.host_aliases):
            query['HostAliases'] = request.host_aliases
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.image_registry_credentials):
            query['ImageRegistryCredentials'] = request.image_registry_credentials
        if not UtilClient.is_unset(request.image_snapshot_id):
            query['ImageSnapshotId'] = request.image_snapshot_id
        if not UtilClient.is_unset(request.ingress_bandwidth):
            query['IngressBandwidth'] = request.ingress_bandwidth
        if not UtilClient.is_unset(request.init_containers):
            query['InitContainers'] = request.init_containers
        if not UtilClient.is_unset(request.instance_family_level):
            query['InstanceFamilyLevel'] = request.instance_family_level
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.ntp_servers):
            query['NtpServers'] = request.ntp_servers
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.restart_policy):
            query['RestartPolicy'] = request.restart_policy
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.security_context_sys_ctls):
            query['SecurityContextSysCtls'] = request.security_context_sys_ctls
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.spot_price_limit):
            query['SpotPriceLimit'] = request.spot_price_limit
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.termination_grace_period_seconds):
            query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        if not UtilClient.is_unset(request.volumes):
            query['Volumes'] = request.volumes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyEciScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyEciScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_eci_scaling_configuration(
        self,
        request: ess_20220222_models.ModifyEciScalingConfigurationRequest,
    ) -> ess_20220222_models.ModifyEciScalingConfigurationResponse:
        """
        @summary Modifies a scaling configuration for a scaling group that contains elastic container instances.
        
        @description If you want to change the name of a scaling configuration in a scaling group, make sure that the new name is unique within the scaling group.
        
        @param request: ModifyEciScalingConfigurationRequest
        @return: ModifyEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_eci_scaling_configuration_with_options(request, runtime)

    async def modify_eci_scaling_configuration_async(
        self,
        request: ess_20220222_models.ModifyEciScalingConfigurationRequest,
    ) -> ess_20220222_models.ModifyEciScalingConfigurationResponse:
        """
        @summary Modifies a scaling configuration for a scaling group that contains elastic container instances.
        
        @description If you want to change the name of a scaling configuration in a scaling group, make sure that the new name is unique within the scaling group.
        
        @param request: ModifyEciScalingConfigurationRequest
        @return: ModifyEciScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_eci_scaling_configuration_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: ess_20220222_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyInstanceAttributeResponse:
        """
        @summary Modifies the attributes of an Elastic Compute Service (ECS) instance in a scaling group. You can call the ModifyInstanceAttribute operation to modify the lifecycle management attribute of a manually added ECS instance in a scaling group.
        
        @param request: ModifyInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entrusted):
            query['Entrusted'] = request.entrusted
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAttribute',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: ess_20220222_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyInstanceAttributeResponse:
        """
        @summary Modifies the attributes of an Elastic Compute Service (ECS) instance in a scaling group. You can call the ModifyInstanceAttribute operation to modify the lifecycle management attribute of a manually added ECS instance in a scaling group.
        
        @param request: ModifyInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entrusted):
            query['Entrusted'] = request.entrusted
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAttribute',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: ess_20220222_models.ModifyInstanceAttributeRequest,
    ) -> ess_20220222_models.ModifyInstanceAttributeResponse:
        """
        @summary Modifies the attributes of an Elastic Compute Service (ECS) instance in a scaling group. You can call the ModifyInstanceAttribute operation to modify the lifecycle management attribute of a manually added ECS instance in a scaling group.
        
        @param request: ModifyInstanceAttributeRequest
        @return: ModifyInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: ess_20220222_models.ModifyInstanceAttributeRequest,
    ) -> ess_20220222_models.ModifyInstanceAttributeResponse:
        """
        @summary Modifies the attributes of an Elastic Compute Service (ECS) instance in a scaling group. You can call the ModifyInstanceAttribute operation to modify the lifecycle management attribute of a manually added ECS instance in a scaling group.
        
        @param request: ModifyInstanceAttributeRequest
        @return: ModifyInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_lifecycle_hook_with_options(
        self,
        request: ess_20220222_models.ModifyLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyLifecycleHookResponse:
        """
        @summary Modifies a lifecycle hook. If an existing lifecycle hook does not meet your business requirements anymore, you can call the ModifyLifecycleHook operation to modify the information such as the scaling event, timeout period, and default action of the lifecycle hook. Before you modify a lifecycle hook, you can locate the lifecycle hook by its ID, name, or scaling group.
        
        @description You can use one of the following methods to locate the lifecycle hook that you want to modify:
        Specify LifecycleHookId. In this case, ScalingGroupId and LifecycleHookName are ignored.
        Specify ScalingGroupId and LifecycleHookName. Each lifecycle hook within a scaling group has a unique name.
        
        @param request: ModifyLifecycleHookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLifecycleHookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_result):
            query['DefaultResult'] = request.default_result
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['HeartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.lifecycle_hook_status):
            query['LifecycleHookStatus'] = request.lifecycle_hook_status
        if not UtilClient.is_unset(request.lifecycle_transition):
            query['LifecycleTransition'] = request.lifecycle_transition
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_metadata):
            query['NotificationMetadata'] = request.notification_metadata
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyLifecycleHookResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_lifecycle_hook_with_options_async(
        self,
        request: ess_20220222_models.ModifyLifecycleHookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyLifecycleHookResponse:
        """
        @summary Modifies a lifecycle hook. If an existing lifecycle hook does not meet your business requirements anymore, you can call the ModifyLifecycleHook operation to modify the information such as the scaling event, timeout period, and default action of the lifecycle hook. Before you modify a lifecycle hook, you can locate the lifecycle hook by its ID, name, or scaling group.
        
        @description You can use one of the following methods to locate the lifecycle hook that you want to modify:
        Specify LifecycleHookId. In this case, ScalingGroupId and LifecycleHookName are ignored.
        Specify ScalingGroupId and LifecycleHookName. Each lifecycle hook within a scaling group has a unique name.
        
        @param request: ModifyLifecycleHookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLifecycleHookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_result):
            query['DefaultResult'] = request.default_result
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['HeartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['LifecycleHookId'] = request.lifecycle_hook_id
        if not UtilClient.is_unset(request.lifecycle_hook_name):
            query['LifecycleHookName'] = request.lifecycle_hook_name
        if not UtilClient.is_unset(request.lifecycle_hook_status):
            query['LifecycleHookStatus'] = request.lifecycle_hook_status
        if not UtilClient.is_unset(request.lifecycle_transition):
            query['LifecycleTransition'] = request.lifecycle_transition
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_metadata):
            query['NotificationMetadata'] = request.notification_metadata
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLifecycleHook',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyLifecycleHookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_lifecycle_hook(
        self,
        request: ess_20220222_models.ModifyLifecycleHookRequest,
    ) -> ess_20220222_models.ModifyLifecycleHookResponse:
        """
        @summary Modifies a lifecycle hook. If an existing lifecycle hook does not meet your business requirements anymore, you can call the ModifyLifecycleHook operation to modify the information such as the scaling event, timeout period, and default action of the lifecycle hook. Before you modify a lifecycle hook, you can locate the lifecycle hook by its ID, name, or scaling group.
        
        @description You can use one of the following methods to locate the lifecycle hook that you want to modify:
        Specify LifecycleHookId. In this case, ScalingGroupId and LifecycleHookName are ignored.
        Specify ScalingGroupId and LifecycleHookName. Each lifecycle hook within a scaling group has a unique name.
        
        @param request: ModifyLifecycleHookRequest
        @return: ModifyLifecycleHookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_lifecycle_hook_with_options(request, runtime)

    async def modify_lifecycle_hook_async(
        self,
        request: ess_20220222_models.ModifyLifecycleHookRequest,
    ) -> ess_20220222_models.ModifyLifecycleHookResponse:
        """
        @summary Modifies a lifecycle hook. If an existing lifecycle hook does not meet your business requirements anymore, you can call the ModifyLifecycleHook operation to modify the information such as the scaling event, timeout period, and default action of the lifecycle hook. Before you modify a lifecycle hook, you can locate the lifecycle hook by its ID, name, or scaling group.
        
        @description You can use one of the following methods to locate the lifecycle hook that you want to modify:
        Specify LifecycleHookId. In this case, ScalingGroupId and LifecycleHookName are ignored.
        Specify ScalingGroupId and LifecycleHookName. Each lifecycle hook within a scaling group has a unique name.
        
        @param request: ModifyLifecycleHookRequest
        @return: ModifyLifecycleHookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_lifecycle_hook_with_options_async(request, runtime)

    def modify_notification_configuration_with_options(
        self,
        request: ess_20220222_models.ModifyNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyNotificationConfigurationResponse:
        """
        @summary Modifies event notification rules. Event notification rules support automatic sending of notifications to CloudMonitor, Message Service (MNS) topics, or MNS queues when a specified type of events occur. This helps you learn about the dynamics of your scaling group at the earliest opportunity and further automate resource management. If an existing event notification rule does not meet your business requirements, you can call the ModifyNotificationConfiguration operation to modify the event notification rule, without the need to create a new rule. Take not that you cannot modify the notification method of an event notification rule by calling this operation.
        
        @param request: ModifyNotificationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNotificationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_types):
            query['NotificationTypes'] = request.notification_types
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyNotificationConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_notification_configuration_with_options_async(
        self,
        request: ess_20220222_models.ModifyNotificationConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyNotificationConfigurationResponse:
        """
        @summary Modifies event notification rules. Event notification rules support automatic sending of notifications to CloudMonitor, Message Service (MNS) topics, or MNS queues when a specified type of events occur. This helps you learn about the dynamics of your scaling group at the earliest opportunity and further automate resource management. If an existing event notification rule does not meet your business requirements, you can call the ModifyNotificationConfiguration operation to modify the event notification rule, without the need to create a new rule. Take not that you cannot modify the notification method of an event notification rule by calling this operation.
        
        @param request: ModifyNotificationConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyNotificationConfigurationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notification_arn):
            query['NotificationArn'] = request.notification_arn
        if not UtilClient.is_unset(request.notification_types):
            query['NotificationTypes'] = request.notification_types
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyNotificationConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyNotificationConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_notification_configuration(
        self,
        request: ess_20220222_models.ModifyNotificationConfigurationRequest,
    ) -> ess_20220222_models.ModifyNotificationConfigurationResponse:
        """
        @summary Modifies event notification rules. Event notification rules support automatic sending of notifications to CloudMonitor, Message Service (MNS) topics, or MNS queues when a specified type of events occur. This helps you learn about the dynamics of your scaling group at the earliest opportunity and further automate resource management. If an existing event notification rule does not meet your business requirements, you can call the ModifyNotificationConfiguration operation to modify the event notification rule, without the need to create a new rule. Take not that you cannot modify the notification method of an event notification rule by calling this operation.
        
        @param request: ModifyNotificationConfigurationRequest
        @return: ModifyNotificationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_notification_configuration_with_options(request, runtime)

    async def modify_notification_configuration_async(
        self,
        request: ess_20220222_models.ModifyNotificationConfigurationRequest,
    ) -> ess_20220222_models.ModifyNotificationConfigurationResponse:
        """
        @summary Modifies event notification rules. Event notification rules support automatic sending of notifications to CloudMonitor, Message Service (MNS) topics, or MNS queues when a specified type of events occur. This helps you learn about the dynamics of your scaling group at the earliest opportunity and further automate resource management. If an existing event notification rule does not meet your business requirements, you can call the ModifyNotificationConfiguration operation to modify the event notification rule, without the need to create a new rule. Take not that you cannot modify the notification method of an event notification rule by calling this operation.
        
        @param request: ModifyNotificationConfigurationRequest
        @return: ModifyNotificationConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_notification_configuration_with_options_async(request, runtime)

    def modify_scaling_configuration_with_options(
        self,
        tmp_req: ess_20220222_models.ModifyScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScalingConfigurationResponse:
        """
        @summary Modifies a scaling configuration.
        
        @description You can change the name of a scaling configuration in a scaling group. The name must be unique within the scaling group.
        
        @param tmp_req: ModifyScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ess_20220222_models.ModifyScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.custom_priorities):
            query['CustomPriorities'] = request.custom_priorities
        if not UtilClient.is_unset(request.data_disks):
            query['DataDisks'] = request.data_disks
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_pattern_infos):
            query['InstancePatternInfos'] = request.instance_pattern_infos
        if not UtilClient.is_unset(request.instance_type_overrides):
            query['InstanceTypeOverrides'] = request.instance_type_overrides
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.network_interfaces):
            query['NetworkInterfaces'] = request.network_interfaces
        if not UtilClient.is_unset(request.override):
            query['Override'] = request.override
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scheduler_options_shrink):
            query['SchedulerOptions'] = request.scheduler_options_shrink
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limits):
            query['SpotPriceLimits'] = request.spot_price_limits
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.system_disk_categories):
            query['SystemDiskCategories'] = request.system_disk_categories
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.image_options):
            query['ImageOptions'] = request.image_options
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_configuration_with_options_async(
        self,
        tmp_req: ess_20220222_models.ModifyScalingConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScalingConfigurationResponse:
        """
        @summary Modifies a scaling configuration.
        
        @description You can change the name of a scaling configuration in a scaling group. The name must be unique within the scaling group.
        
        @param tmp_req: ModifyScalingConfigurationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingConfigurationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ess_20220222_models.ModifyScalingConfigurationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.scheduler_options):
            request.scheduler_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scheduler_options, 'SchedulerOptions', 'json')
        query = {}
        if not UtilClient.is_unset(request.affinity):
            query['Affinity'] = request.affinity
        if not UtilClient.is_unset(request.cpu):
            query['Cpu'] = request.cpu
        if not UtilClient.is_unset(request.credit_specification):
            query['CreditSpecification'] = request.credit_specification
        if not UtilClient.is_unset(request.custom_priorities):
            query['CustomPriorities'] = request.custom_priorities
        if not UtilClient.is_unset(request.data_disks):
            query['DataDisks'] = request.data_disks
        if not UtilClient.is_unset(request.dedicated_host_cluster_id):
            query['DedicatedHostClusterId'] = request.dedicated_host_cluster_id
        if not UtilClient.is_unset(request.dedicated_host_id):
            query['DedicatedHostId'] = request.dedicated_host_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.deployment_set_id):
            query['DeploymentSetId'] = request.deployment_set_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.hpc_cluster_id):
            query['HpcClusterId'] = request.hpc_cluster_id
        if not UtilClient.is_unset(request.image_family):
            query['ImageFamily'] = request.image_family
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.image_name):
            query['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.instance_description):
            query['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_pattern_infos):
            query['InstancePatternInfos'] = request.instance_pattern_infos
        if not UtilClient.is_unset(request.instance_type_overrides):
            query['InstanceTypeOverrides'] = request.instance_type_overrides
        if not UtilClient.is_unset(request.instance_types):
            query['InstanceTypes'] = request.instance_types
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.internet_max_bandwidth_out):
            query['InternetMaxBandwidthOut'] = request.internet_max_bandwidth_out
        if not UtilClient.is_unset(request.io_optimized):
            query['IoOptimized'] = request.io_optimized
        if not UtilClient.is_unset(request.ipv_6address_count):
            query['Ipv6AddressCount'] = request.ipv_6address_count
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.load_balancer_weight):
            query['LoadBalancerWeight'] = request.load_balancer_weight
        if not UtilClient.is_unset(request.memory):
            query['Memory'] = request.memory
        if not UtilClient.is_unset(request.network_interfaces):
            query['NetworkInterfaces'] = request.network_interfaces
        if not UtilClient.is_unset(request.override):
            query['Override'] = request.override
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.password_inherit):
            query['PasswordInherit'] = request.password_inherit
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_configuration_id):
            query['ScalingConfigurationId'] = request.scaling_configuration_id
        if not UtilClient.is_unset(request.scaling_configuration_name):
            query['ScalingConfigurationName'] = request.scaling_configuration_name
        if not UtilClient.is_unset(request.scheduler_options_shrink):
            query['SchedulerOptions'] = request.scheduler_options_shrink
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.spot_duration):
            query['SpotDuration'] = request.spot_duration
        if not UtilClient.is_unset(request.spot_interruption_behavior):
            query['SpotInterruptionBehavior'] = request.spot_interruption_behavior
        if not UtilClient.is_unset(request.spot_price_limits):
            query['SpotPriceLimits'] = request.spot_price_limits
        if not UtilClient.is_unset(request.spot_strategy):
            query['SpotStrategy'] = request.spot_strategy
        if not UtilClient.is_unset(request.storage_set_id):
            query['StorageSetId'] = request.storage_set_id
        if not UtilClient.is_unset(request.storage_set_partition_number):
            query['StorageSetPartitionNumber'] = request.storage_set_partition_number
        if not UtilClient.is_unset(request.system_disk_categories):
            query['SystemDiskCategories'] = request.system_disk_categories
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.tenancy):
            query['Tenancy'] = request.tenancy
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        if not UtilClient.is_unset(request.image_options):
            query['ImageOptions'] = request.image_options
        if not UtilClient.is_unset(request.private_pool_options):
            query['PrivatePoolOptions'] = request.private_pool_options
        if not UtilClient.is_unset(request.system_disk):
            query['SystemDisk'] = request.system_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingConfiguration',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scaling_configuration(
        self,
        request: ess_20220222_models.ModifyScalingConfigurationRequest,
    ) -> ess_20220222_models.ModifyScalingConfigurationResponse:
        """
        @summary Modifies a scaling configuration.
        
        @description You can change the name of a scaling configuration in a scaling group. The name must be unique within the scaling group.
        
        @param request: ModifyScalingConfigurationRequest
        @return: ModifyScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_configuration_with_options(request, runtime)

    async def modify_scaling_configuration_async(
        self,
        request: ess_20220222_models.ModifyScalingConfigurationRequest,
    ) -> ess_20220222_models.ModifyScalingConfigurationResponse:
        """
        @summary Modifies a scaling configuration.
        
        @description You can change the name of a scaling configuration in a scaling group. The name must be unique within the scaling group.
        
        @param request: ModifyScalingConfigurationRequest
        @return: ModifyScalingConfigurationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_configuration_with_options_async(request, runtime)

    def modify_scaling_group_with_options(
        self,
        request: ess_20220222_models.ModifyScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScalingGroupResponse:
        """
        @summary Modifies a scaling group. If you want to enable policy-based automatic addition or removal of instances of a specific type to meet evolving business requirements, you can modify scaling groups to adjust your computing power with ease. The computing power refers to the instances that provide the computing capability. When your scaling group cannot meet your business requirements, you can call the ModifyScalingGroup operation to modify scaling group attributes such as the maximum, minimum, and expected numbers of instances. This prevents repeated creation and configuration of scaling groups, which saves you a lot of time and resource costs.
        
        @description    You cannot modify the following parameters by calling this operation:
        RegionId
        LoadBalancerId
        *\
        *Note** If you want to modify the load balancer settings of your scaling group, you can call the AttachLoadBalancers operation or the DetachLoadBalancers operation.
        DBInstanceId
        *\
        *Note** If you want to modify the ApsaraDB RDS instance settings of your scaling group, you can call the AttachDBInstances operation or the DetachDBInstances operation.
        You can call this operation to modify a scaling group only when the scaling group is in the `Active` or `Inactive` state.
        Enabling a new scaling configuration in the scaling group will not impact existing Elastic Compute Service (ECS) instances or elastic container instances that were provisioned based on the previous scaling configuration. These instances will continue to run as expected.
        If the modification of the MaxSize setting leads to the total number of ECS instances or elastic container instances in the scaling group exceeding the new maximum limit, Auto Scaling proactively removes the surplus instances to restore the total number to match the new maximum limit.
        If the modification of the MinSize setting leads to the total number of ECS instances or elastic container instances in the scaling group exceeding the new minimum threshold, Auto Scaling proactively adds more instances to the scaling group to ensure that the total number aligns with the new minimum threshold.
        If the modification of the DesiredCapacity setting leads to the total number of ECS instances or elastic container instances in the scaling group not matching the new desired capacity, Auto Scaling proactively adjusts the total number of instances to ensure that the total number aligns with the new desired capacity.
        
        @param request: ModifyScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not UtilClient.is_unset(request.allocation_strategy):
            query['AllocationStrategy'] = request.allocation_strategy
        if not UtilClient.is_unset(request.az_balance):
            query['AzBalance'] = request.az_balance
        if not UtilClient.is_unset(request.compensate_with_on_demand):
            query['CompensateWithOnDemand'] = request.compensate_with_on_demand
        if not UtilClient.is_unset(request.custom_policy_arn):
            query['CustomPolicyARN'] = request.custom_policy_arn
        if not UtilClient.is_unset(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.disable_desired_capacity):
            query['DisableDesiredCapacity'] = request.disable_desired_capacity
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_types):
            query['HealthCheckTypes'] = request.health_check_types
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.max_instance_lifetime):
            query['MaxInstanceLifetime'] = request.max_instance_lifetime
        if not UtilClient.is_unset(request.max_size):
            query['MaxSize'] = request.max_size
        if not UtilClient.is_unset(request.min_size):
            query['MinSize'] = request.min_size
        if not UtilClient.is_unset(request.multi_azpolicy):
            query['MultiAZPolicy'] = request.multi_azpolicy
        if not UtilClient.is_unset(request.on_demand_base_capacity):
            query['OnDemandBaseCapacity'] = request.on_demand_base_capacity
        if not UtilClient.is_unset(request.on_demand_percentage_above_base_capacity):
            query['OnDemandPercentageAboveBaseCapacity'] = request.on_demand_percentage_above_base_capacity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.removal_policies):
            query['RemovalPolicies'] = request.removal_policies
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not UtilClient.is_unset(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not UtilClient.is_unset(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not UtilClient.is_unset(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_group_with_options_async(
        self,
        request: ess_20220222_models.ModifyScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScalingGroupResponse:
        """
        @summary Modifies a scaling group. If you want to enable policy-based automatic addition or removal of instances of a specific type to meet evolving business requirements, you can modify scaling groups to adjust your computing power with ease. The computing power refers to the instances that provide the computing capability. When your scaling group cannot meet your business requirements, you can call the ModifyScalingGroup operation to modify scaling group attributes such as the maximum, minimum, and expected numbers of instances. This prevents repeated creation and configuration of scaling groups, which saves you a lot of time and resource costs.
        
        @description    You cannot modify the following parameters by calling this operation:
        RegionId
        LoadBalancerId
        *\
        *Note** If you want to modify the load balancer settings of your scaling group, you can call the AttachLoadBalancers operation or the DetachLoadBalancers operation.
        DBInstanceId
        *\
        *Note** If you want to modify the ApsaraDB RDS instance settings of your scaling group, you can call the AttachDBInstances operation or the DetachDBInstances operation.
        You can call this operation to modify a scaling group only when the scaling group is in the `Active` or `Inactive` state.
        Enabling a new scaling configuration in the scaling group will not impact existing Elastic Compute Service (ECS) instances or elastic container instances that were provisioned based on the previous scaling configuration. These instances will continue to run as expected.
        If the modification of the MaxSize setting leads to the total number of ECS instances or elastic container instances in the scaling group exceeding the new maximum limit, Auto Scaling proactively removes the surplus instances to restore the total number to match the new maximum limit.
        If the modification of the MinSize setting leads to the total number of ECS instances or elastic container instances in the scaling group exceeding the new minimum threshold, Auto Scaling proactively adds more instances to the scaling group to ensure that the total number aligns with the new minimum threshold.
        If the modification of the DesiredCapacity setting leads to the total number of ECS instances or elastic container instances in the scaling group not matching the new desired capacity, Auto Scaling proactively adjusts the total number of instances to ensure that the total number aligns with the new desired capacity.
        
        @param request: ModifyScalingGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_scaling_configuration_id):
            query['ActiveScalingConfigurationId'] = request.active_scaling_configuration_id
        if not UtilClient.is_unset(request.allocation_strategy):
            query['AllocationStrategy'] = request.allocation_strategy
        if not UtilClient.is_unset(request.az_balance):
            query['AzBalance'] = request.az_balance
        if not UtilClient.is_unset(request.compensate_with_on_demand):
            query['CompensateWithOnDemand'] = request.compensate_with_on_demand
        if not UtilClient.is_unset(request.custom_policy_arn):
            query['CustomPolicyARN'] = request.custom_policy_arn
        if not UtilClient.is_unset(request.default_cooldown):
            query['DefaultCooldown'] = request.default_cooldown
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.disable_desired_capacity):
            query['DisableDesiredCapacity'] = request.disable_desired_capacity
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_types):
            query['HealthCheckTypes'] = request.health_check_types
        if not UtilClient.is_unset(request.launch_template_id):
            query['LaunchTemplateId'] = request.launch_template_id
        if not UtilClient.is_unset(request.launch_template_overrides):
            query['LaunchTemplateOverrides'] = request.launch_template_overrides
        if not UtilClient.is_unset(request.launch_template_version):
            query['LaunchTemplateVersion'] = request.launch_template_version
        if not UtilClient.is_unset(request.max_instance_lifetime):
            query['MaxInstanceLifetime'] = request.max_instance_lifetime
        if not UtilClient.is_unset(request.max_size):
            query['MaxSize'] = request.max_size
        if not UtilClient.is_unset(request.min_size):
            query['MinSize'] = request.min_size
        if not UtilClient.is_unset(request.multi_azpolicy):
            query['MultiAZPolicy'] = request.multi_azpolicy
        if not UtilClient.is_unset(request.on_demand_base_capacity):
            query['OnDemandBaseCapacity'] = request.on_demand_base_capacity
        if not UtilClient.is_unset(request.on_demand_percentage_above_base_capacity):
            query['OnDemandPercentageAboveBaseCapacity'] = request.on_demand_percentage_above_base_capacity
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.removal_policies):
            query['RemovalPolicies'] = request.removal_policies
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scaling_group_name):
            query['ScalingGroupName'] = request.scaling_group_name
        if not UtilClient.is_unset(request.scaling_policy):
            query['ScalingPolicy'] = request.scaling_policy
        if not UtilClient.is_unset(request.spot_allocation_strategy):
            query['SpotAllocationStrategy'] = request.spot_allocation_strategy
        if not UtilClient.is_unset(request.spot_instance_pools):
            query['SpotInstancePools'] = request.spot_instance_pools
        if not UtilClient.is_unset(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not UtilClient.is_unset(request.v_switch_ids):
            query['VSwitchIds'] = request.v_switch_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingGroup',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scaling_group(
        self,
        request: ess_20220222_models.ModifyScalingGroupRequest,
    ) -> ess_20220222_models.ModifyScalingGroupResponse:
        """
        @summary Modifies a scaling group. If you want to enable policy-based automatic addition or removal of instances of a specific type to meet evolving business requirements, you can modify scaling groups to adjust your computing power with ease. The computing power refers to the instances that provide the computing capability. When your scaling group cannot meet your business requirements, you can call the ModifyScalingGroup operation to modify scaling group attributes such as the maximum, minimum, and expected numbers of instances. This prevents repeated creation and configuration of scaling groups, which saves you a lot of time and resource costs.
        
        @description    You cannot modify the following parameters by calling this operation:
        RegionId
        LoadBalancerId
        *\
        *Note** If you want to modify the load balancer settings of your scaling group, you can call the AttachLoadBalancers operation or the DetachLoadBalancers operation.
        DBInstanceId
        *\
        *Note** If you want to modify the ApsaraDB RDS instance settings of your scaling group, you can call the AttachDBInstances operation or the DetachDBInstances operation.
        You can call this operation to modify a scaling group only when the scaling group is in the `Active` or `Inactive` state.
        Enabling a new scaling configuration in the scaling group will not impact existing Elastic Compute Service (ECS) instances or elastic container instances that were provisioned based on the previous scaling configuration. These instances will continue to run as expected.
        If the modification of the MaxSize setting leads to the total number of ECS instances or elastic container instances in the scaling group exceeding the new maximum limit, Auto Scaling proactively removes the surplus instances to restore the total number to match the new maximum limit.
        If the modification of the MinSize setting leads to the total number of ECS instances or elastic container instances in the scaling group exceeding the new minimum threshold, Auto Scaling proactively adds more instances to the scaling group to ensure that the total number aligns with the new minimum threshold.
        If the modification of the DesiredCapacity setting leads to the total number of ECS instances or elastic container instances in the scaling group not matching the new desired capacity, Auto Scaling proactively adjusts the total number of instances to ensure that the total number aligns with the new desired capacity.
        
        @param request: ModifyScalingGroupRequest
        @return: ModifyScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_group_with_options(request, runtime)

    async def modify_scaling_group_async(
        self,
        request: ess_20220222_models.ModifyScalingGroupRequest,
    ) -> ess_20220222_models.ModifyScalingGroupResponse:
        """
        @summary Modifies a scaling group. If you want to enable policy-based automatic addition or removal of instances of a specific type to meet evolving business requirements, you can modify scaling groups to adjust your computing power with ease. The computing power refers to the instances that provide the computing capability. When your scaling group cannot meet your business requirements, you can call the ModifyScalingGroup operation to modify scaling group attributes such as the maximum, minimum, and expected numbers of instances. This prevents repeated creation and configuration of scaling groups, which saves you a lot of time and resource costs.
        
        @description    You cannot modify the following parameters by calling this operation:
        RegionId
        LoadBalancerId
        *\
        *Note** If you want to modify the load balancer settings of your scaling group, you can call the AttachLoadBalancers operation or the DetachLoadBalancers operation.
        DBInstanceId
        *\
        *Note** If you want to modify the ApsaraDB RDS instance settings of your scaling group, you can call the AttachDBInstances operation or the DetachDBInstances operation.
        You can call this operation to modify a scaling group only when the scaling group is in the `Active` or `Inactive` state.
        Enabling a new scaling configuration in the scaling group will not impact existing Elastic Compute Service (ECS) instances or elastic container instances that were provisioned based on the previous scaling configuration. These instances will continue to run as expected.
        If the modification of the MaxSize setting leads to the total number of ECS instances or elastic container instances in the scaling group exceeding the new maximum limit, Auto Scaling proactively removes the surplus instances to restore the total number to match the new maximum limit.
        If the modification of the MinSize setting leads to the total number of ECS instances or elastic container instances in the scaling group exceeding the new minimum threshold, Auto Scaling proactively adds more instances to the scaling group to ensure that the total number aligns with the new minimum threshold.
        If the modification of the DesiredCapacity setting leads to the total number of ECS instances or elastic container instances in the scaling group not matching the new desired capacity, Auto Scaling proactively adjusts the total number of instances to ensure that the total number aligns with the new desired capacity.
        
        @param request: ModifyScalingGroupRequest
        @return: ModifyScalingGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_group_with_options_async(request, runtime)

    def modify_scaling_rule_with_options(
        self,
        request: ess_20220222_models.ModifyScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScalingRuleResponse:
        """
        @summary Modifies a scaling rule. If an existing scaling rule cannot meet your business requirements, you can call the ModifyScalingRule operation to modify the scaling rule, without the need to create a new one. This streamlines your workflow, enhancing operational efficiency while also contributing to cost optimization by avoiding redundant steps.
        
        @param request: ModifyScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.alarm_dimensions):
            query['AlarmDimensions'] = request.alarm_dimensions
        if not UtilClient.is_unset(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not UtilClient.is_unset(request.disable_scale_in):
            query['DisableScaleIn'] = request.disable_scale_in
        if not UtilClient.is_unset(request.estimated_instance_warmup):
            query['EstimatedInstanceWarmup'] = request.estimated_instance_warmup
        if not UtilClient.is_unset(request.initial_max_size):
            query['InitialMaxSize'] = request.initial_max_size
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.predictive_scaling_mode):
            query['PredictiveScalingMode'] = request.predictive_scaling_mode
        if not UtilClient.is_unset(request.predictive_task_buffer_time):
            query['PredictiveTaskBufferTime'] = request.predictive_task_buffer_time
        if not UtilClient.is_unset(request.predictive_value_behavior):
            query['PredictiveValueBehavior'] = request.predictive_value_behavior
        if not UtilClient.is_unset(request.predictive_value_buffer):
            query['PredictiveValueBuffer'] = request.predictive_value_buffer
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scale_in_evaluation_count):
            query['ScaleInEvaluationCount'] = request.scale_in_evaluation_count
        if not UtilClient.is_unset(request.scale_out_evaluation_count):
            query['ScaleOutEvaluationCount'] = request.scale_out_evaluation_count
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.step_adjustments):
            query['StepAdjustments'] = request.step_adjustments
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_rule_with_options_async(
        self,
        request: ess_20220222_models.ModifyScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScalingRuleResponse:
        """
        @summary Modifies a scaling rule. If an existing scaling rule cannot meet your business requirements, you can call the ModifyScalingRule operation to modify the scaling rule, without the need to create a new one. This streamlines your workflow, enhancing operational efficiency while also contributing to cost optimization by avoiding redundant steps.
        
        @param request: ModifyScalingRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScalingRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.alarm_dimensions):
            query['AlarmDimensions'] = request.alarm_dimensions
        if not UtilClient.is_unset(request.cooldown):
            query['Cooldown'] = request.cooldown
        if not UtilClient.is_unset(request.disable_scale_in):
            query['DisableScaleIn'] = request.disable_scale_in
        if not UtilClient.is_unset(request.estimated_instance_warmup):
            query['EstimatedInstanceWarmup'] = request.estimated_instance_warmup
        if not UtilClient.is_unset(request.initial_max_size):
            query['InitialMaxSize'] = request.initial_max_size
        if not UtilClient.is_unset(request.metric_name):
            query['MetricName'] = request.metric_name
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.predictive_scaling_mode):
            query['PredictiveScalingMode'] = request.predictive_scaling_mode
        if not UtilClient.is_unset(request.predictive_task_buffer_time):
            query['PredictiveTaskBufferTime'] = request.predictive_task_buffer_time
        if not UtilClient.is_unset(request.predictive_value_behavior):
            query['PredictiveValueBehavior'] = request.predictive_value_behavior
        if not UtilClient.is_unset(request.predictive_value_buffer):
            query['PredictiveValueBuffer'] = request.predictive_value_buffer
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scale_in_evaluation_count):
            query['ScaleInEvaluationCount'] = request.scale_in_evaluation_count
        if not UtilClient.is_unset(request.scale_out_evaluation_count):
            query['ScaleOutEvaluationCount'] = request.scale_out_evaluation_count
        if not UtilClient.is_unset(request.scaling_rule_id):
            query['ScalingRuleId'] = request.scaling_rule_id
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.step_adjustments):
            query['StepAdjustments'] = request.step_adjustments
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScalingRule',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scaling_rule(
        self,
        request: ess_20220222_models.ModifyScalingRuleRequest,
    ) -> ess_20220222_models.ModifyScalingRuleResponse:
        """
        @summary Modifies a scaling rule. If an existing scaling rule cannot meet your business requirements, you can call the ModifyScalingRule operation to modify the scaling rule, without the need to create a new one. This streamlines your workflow, enhancing operational efficiency while also contributing to cost optimization by avoiding redundant steps.
        
        @param request: ModifyScalingRuleRequest
        @return: ModifyScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_rule_with_options(request, runtime)

    async def modify_scaling_rule_async(
        self,
        request: ess_20220222_models.ModifyScalingRuleRequest,
    ) -> ess_20220222_models.ModifyScalingRuleResponse:
        """
        @summary Modifies a scaling rule. If an existing scaling rule cannot meet your business requirements, you can call the ModifyScalingRule operation to modify the scaling rule, without the need to create a new one. This streamlines your workflow, enhancing operational efficiency while also contributing to cost optimization by avoiding redundant steps.
        
        @param request: ModifyScalingRuleRequest
        @return: ModifyScalingRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_rule_with_options_async(request, runtime)

    def modify_scheduled_task_with_options(
        self,
        request: ess_20220222_models.ModifyScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScheduledTaskResponse:
        """
        @summary Modifies a scheduled task. If an existing scheduled task cannot meet your business requirements, you can call the ModifyScheduledTask operation to adjust its parameter settings including the scaling rule to execute and the boundary values of your scaling group, without the need to create a new scheduled task. This operation provides a flexible way to optimize scheduled tasks.
        
        @description You can use the following parameters to specify the scaling method of a scheduled task:
        If you use the `ScheduledAction` parameter, you must select an existing scaling rule for the scheduled task.
        If you use the `ScalingGroupId` parameter, you must specify the minimum number, maximum number, or expected number of instances in the scheduled task.
        > You cannot specify the `ScheduledAction` and `ScalingGroupId` parameters at the same time.
        
        @param request: ModifyScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not UtilClient.is_unset(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not UtilClient.is_unset(request.max_value):
            query['MaxValue'] = request.max_value
        if not UtilClient.is_unset(request.min_value):
            query['MinValue'] = request.min_value
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recurrence_end_time):
            query['RecurrenceEndTime'] = request.recurrence_end_time
        if not UtilClient.is_unset(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not UtilClient.is_unset(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not UtilClient.is_unset(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        if not UtilClient.is_unset(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        if not UtilClient.is_unset(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScheduledTask',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScheduledTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scheduled_task_with_options_async(
        self,
        request: ess_20220222_models.ModifyScheduledTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ModifyScheduledTaskResponse:
        """
        @summary Modifies a scheduled task. If an existing scheduled task cannot meet your business requirements, you can call the ModifyScheduledTask operation to adjust its parameter settings including the scaling rule to execute and the boundary values of your scaling group, without the need to create a new scheduled task. This operation provides a flexible way to optimize scheduled tasks.
        
        @description You can use the following parameters to specify the scaling method of a scheduled task:
        If you use the `ScheduledAction` parameter, you must select an existing scaling rule for the scheduled task.
        If you use the `ScalingGroupId` parameter, you must specify the minimum number, maximum number, or expected number of instances in the scheduled task.
        > You cannot specify the `ScheduledAction` and `ScalingGroupId` parameters at the same time.
        
        @param request: ModifyScheduledTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyScheduledTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.desired_capacity):
            query['DesiredCapacity'] = request.desired_capacity
        if not UtilClient.is_unset(request.launch_expiration_time):
            query['LaunchExpirationTime'] = request.launch_expiration_time
        if not UtilClient.is_unset(request.launch_time):
            query['LaunchTime'] = request.launch_time
        if not UtilClient.is_unset(request.max_value):
            query['MaxValue'] = request.max_value
        if not UtilClient.is_unset(request.min_value):
            query['MinValue'] = request.min_value
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recurrence_end_time):
            query['RecurrenceEndTime'] = request.recurrence_end_time
        if not UtilClient.is_unset(request.recurrence_type):
            query['RecurrenceType'] = request.recurrence_type
        if not UtilClient.is_unset(request.recurrence_value):
            query['RecurrenceValue'] = request.recurrence_value
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.scheduled_action):
            query['ScheduledAction'] = request.scheduled_action
        if not UtilClient.is_unset(request.scheduled_task_id):
            query['ScheduledTaskId'] = request.scheduled_task_id
        if not UtilClient.is_unset(request.scheduled_task_name):
            query['ScheduledTaskName'] = request.scheduled_task_name
        if not UtilClient.is_unset(request.task_enabled):
            query['TaskEnabled'] = request.task_enabled
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyScheduledTask',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ModifyScheduledTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_scheduled_task(
        self,
        request: ess_20220222_models.ModifyScheduledTaskRequest,
    ) -> ess_20220222_models.ModifyScheduledTaskResponse:
        """
        @summary Modifies a scheduled task. If an existing scheduled task cannot meet your business requirements, you can call the ModifyScheduledTask operation to adjust its parameter settings including the scaling rule to execute and the boundary values of your scaling group, without the need to create a new scheduled task. This operation provides a flexible way to optimize scheduled tasks.
        
        @description You can use the following parameters to specify the scaling method of a scheduled task:
        If you use the `ScheduledAction` parameter, you must select an existing scaling rule for the scheduled task.
        If you use the `ScalingGroupId` parameter, you must specify the minimum number, maximum number, or expected number of instances in the scheduled task.
        > You cannot specify the `ScheduledAction` and `ScalingGroupId` parameters at the same time.
        
        @param request: ModifyScheduledTaskRequest
        @return: ModifyScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_scheduled_task_with_options(request, runtime)

    async def modify_scheduled_task_async(
        self,
        request: ess_20220222_models.ModifyScheduledTaskRequest,
    ) -> ess_20220222_models.ModifyScheduledTaskResponse:
        """
        @summary Modifies a scheduled task. If an existing scheduled task cannot meet your business requirements, you can call the ModifyScheduledTask operation to adjust its parameter settings including the scaling rule to execute and the boundary values of your scaling group, without the need to create a new scheduled task. This operation provides a flexible way to optimize scheduled tasks.
        
        @description You can use the following parameters to specify the scaling method of a scheduled task:
        If you use the `ScheduledAction` parameter, you must select an existing scaling rule for the scheduled task.
        If you use the `ScalingGroupId` parameter, you must specify the minimum number, maximum number, or expected number of instances in the scheduled task.
        > You cannot specify the `ScheduledAction` and `ScalingGroupId` parameters at the same time.
        
        @param request: ModifyScheduledTaskRequest
        @return: ModifyScheduledTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_scheduled_task_with_options_async(request, runtime)

    def rebalance_instances_with_options(
        self,
        request: ess_20220222_models.RebalanceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.RebalanceInstancesResponse:
        """
        @summary Rebalances the distribution of Elastic Compute Service (ECS) instances across zones. If ECS instances are unevenly distributed across multiple zones, you can call the RebalanceInstances operation to rebalance the distribution of the ECS instances across the zones.
        
        @description ## [](#)Usage notes
        Auto Scaling creates new ECS instances to replace the existing ECS instances to fulfill the rebalancing purpose. Auto Scaling starts the new ECS instances before stopping the existing ECS instances. The rebalancing operation does not affect the performance or service availability of your application.
        This operation is supported by only multi-zone scaling groups whose `MultiAZPolicy` is set to `BALANCE`.
        A rebalancing operation is required only when the distribution of the instances of a multi-zone scaling group is significantly unbalanced. In a rebalancing activity, Auto Scaling replaces up to 20 ECS instances to rectify the unbalanced distribution.
        During the execution of a rebalancing operation, if the number of instances in the scaling group approaches or hits the value of MaxSize but the rebalancing operation needs to continue, Auto Scaling allows the total number of ECS instances to momentarily exceed the value of MaxSize by 10%. This temporary surplus condition persists for a duration until equilibrium in the distribution of ECS instances is achieved. Typically, it takes 1 to 6 minutes.
        *\
        *Note** If the 10% increment of the maximum number of instances in a scaling group yield a non-integer value, the decimal portion is always rounded up to ensure an additional instance is accounted for. For example, you have a scaling group that holds a maximum of 15 ECS instances. During a rebalancing operation, Auto Scaling would permit the total number of instances to momentarily surpass this limit by 2, instead of the calculated 10% (which is 1.5).
        
        @param request: RebalanceInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebalanceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebalanceInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RebalanceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebalance_instances_with_options_async(
        self,
        request: ess_20220222_models.RebalanceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.RebalanceInstancesResponse:
        """
        @summary Rebalances the distribution of Elastic Compute Service (ECS) instances across zones. If ECS instances are unevenly distributed across multiple zones, you can call the RebalanceInstances operation to rebalance the distribution of the ECS instances across the zones.
        
        @description ## [](#)Usage notes
        Auto Scaling creates new ECS instances to replace the existing ECS instances to fulfill the rebalancing purpose. Auto Scaling starts the new ECS instances before stopping the existing ECS instances. The rebalancing operation does not affect the performance or service availability of your application.
        This operation is supported by only multi-zone scaling groups whose `MultiAZPolicy` is set to `BALANCE`.
        A rebalancing operation is required only when the distribution of the instances of a multi-zone scaling group is significantly unbalanced. In a rebalancing activity, Auto Scaling replaces up to 20 ECS instances to rectify the unbalanced distribution.
        During the execution of a rebalancing operation, if the number of instances in the scaling group approaches or hits the value of MaxSize but the rebalancing operation needs to continue, Auto Scaling allows the total number of ECS instances to momentarily exceed the value of MaxSize by 10%. This temporary surplus condition persists for a duration until equilibrium in the distribution of ECS instances is achieved. Typically, it takes 1 to 6 minutes.
        *\
        *Note** If the 10% increment of the maximum number of instances in a scaling group yield a non-integer value, the decimal portion is always rounded up to ensure an additional instance is accounted for. For example, you have a scaling group that holds a maximum of 15 ECS instances. During a rebalancing operation, Auto Scaling would permit the total number of instances to momentarily surpass this limit by 2, instead of the calculated 10% (which is 1.5).
        
        @param request: RebalanceInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebalanceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebalanceInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RebalanceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebalance_instances(
        self,
        request: ess_20220222_models.RebalanceInstancesRequest,
    ) -> ess_20220222_models.RebalanceInstancesResponse:
        """
        @summary Rebalances the distribution of Elastic Compute Service (ECS) instances across zones. If ECS instances are unevenly distributed across multiple zones, you can call the RebalanceInstances operation to rebalance the distribution of the ECS instances across the zones.
        
        @description ## [](#)Usage notes
        Auto Scaling creates new ECS instances to replace the existing ECS instances to fulfill the rebalancing purpose. Auto Scaling starts the new ECS instances before stopping the existing ECS instances. The rebalancing operation does not affect the performance or service availability of your application.
        This operation is supported by only multi-zone scaling groups whose `MultiAZPolicy` is set to `BALANCE`.
        A rebalancing operation is required only when the distribution of the instances of a multi-zone scaling group is significantly unbalanced. In a rebalancing activity, Auto Scaling replaces up to 20 ECS instances to rectify the unbalanced distribution.
        During the execution of a rebalancing operation, if the number of instances in the scaling group approaches or hits the value of MaxSize but the rebalancing operation needs to continue, Auto Scaling allows the total number of ECS instances to momentarily exceed the value of MaxSize by 10%. This temporary surplus condition persists for a duration until equilibrium in the distribution of ECS instances is achieved. Typically, it takes 1 to 6 minutes.
        *\
        *Note** If the 10% increment of the maximum number of instances in a scaling group yield a non-integer value, the decimal portion is always rounded up to ensure an additional instance is accounted for. For example, you have a scaling group that holds a maximum of 15 ECS instances. During a rebalancing operation, Auto Scaling would permit the total number of instances to momentarily surpass this limit by 2, instead of the calculated 10% (which is 1.5).
        
        @param request: RebalanceInstancesRequest
        @return: RebalanceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rebalance_instances_with_options(request, runtime)

    async def rebalance_instances_async(
        self,
        request: ess_20220222_models.RebalanceInstancesRequest,
    ) -> ess_20220222_models.RebalanceInstancesResponse:
        """
        @summary Rebalances the distribution of Elastic Compute Service (ECS) instances across zones. If ECS instances are unevenly distributed across multiple zones, you can call the RebalanceInstances operation to rebalance the distribution of the ECS instances across the zones.
        
        @description ## [](#)Usage notes
        Auto Scaling creates new ECS instances to replace the existing ECS instances to fulfill the rebalancing purpose. Auto Scaling starts the new ECS instances before stopping the existing ECS instances. The rebalancing operation does not affect the performance or service availability of your application.
        This operation is supported by only multi-zone scaling groups whose `MultiAZPolicy` is set to `BALANCE`.
        A rebalancing operation is required only when the distribution of the instances of a multi-zone scaling group is significantly unbalanced. In a rebalancing activity, Auto Scaling replaces up to 20 ECS instances to rectify the unbalanced distribution.
        During the execution of a rebalancing operation, if the number of instances in the scaling group approaches or hits the value of MaxSize but the rebalancing operation needs to continue, Auto Scaling allows the total number of ECS instances to momentarily exceed the value of MaxSize by 10%. This temporary surplus condition persists for a duration until equilibrium in the distribution of ECS instances is achieved. Typically, it takes 1 to 6 minutes.
        *\
        *Note** If the 10% increment of the maximum number of instances in a scaling group yield a non-integer value, the decimal portion is always rounded up to ensure an additional instance is accounted for. For example, you have a scaling group that holds a maximum of 15 ECS instances. During a rebalancing operation, Auto Scaling would permit the total number of instances to momentarily surpass this limit by 2, instead of the calculated 10% (which is 1.5).
        
        @param request: RebalanceInstancesRequest
        @return: RebalanceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rebalance_instances_with_options_async(request, runtime)

    def record_lifecycle_action_heartbeat_with_options(
        self,
        request: ess_20220222_models.RecordLifecycleActionHeartbeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.RecordLifecycleActionHeartbeatResponse:
        """
        @summary Extends the time window during which Elastic Compute Service (ECS) instances stay in a Pending state. If the current time window during which an ECS instance stays in a Pending state is not sufficient for you to complete custom operations on the ECS instance, you can call the RecordLifecycleActionHeartbeat operation to extend the time window. When you call this operation, you can specify lifecycleHookId, lifecycleActionToken, and heartbeatTimeout to extend the time window for the desired ECS instance.
        
        @description You can call this operation only when the desired ECS instance enters a Pending state.\\
        An ECS instance can stay in a Pending state for up to six hours. Each time an ECS instance enters a Pending state, you can extend the time window during which the ECS instance stays in a Pending state up to 20 times.
        
        @param request: RecordLifecycleActionHeartbeatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecordLifecycleActionHeartbeatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['heartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_action_token):
            query['lifecycleActionToken'] = request.lifecycle_action_token
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['lifecycleHookId'] = request.lifecycle_hook_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecordLifecycleActionHeartbeat',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RecordLifecycleActionHeartbeatResponse(),
            self.call_api(params, req, runtime)
        )

    async def record_lifecycle_action_heartbeat_with_options_async(
        self,
        request: ess_20220222_models.RecordLifecycleActionHeartbeatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.RecordLifecycleActionHeartbeatResponse:
        """
        @summary Extends the time window during which Elastic Compute Service (ECS) instances stay in a Pending state. If the current time window during which an ECS instance stays in a Pending state is not sufficient for you to complete custom operations on the ECS instance, you can call the RecordLifecycleActionHeartbeat operation to extend the time window. When you call this operation, you can specify lifecycleHookId, lifecycleActionToken, and heartbeatTimeout to extend the time window for the desired ECS instance.
        
        @description You can call this operation only when the desired ECS instance enters a Pending state.\\
        An ECS instance can stay in a Pending state for up to six hours. Each time an ECS instance enters a Pending state, you can extend the time window during which the ECS instance stays in a Pending state up to 20 times.
        
        @param request: RecordLifecycleActionHeartbeatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RecordLifecycleActionHeartbeatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.heartbeat_timeout):
            query['heartbeatTimeout'] = request.heartbeat_timeout
        if not UtilClient.is_unset(request.lifecycle_action_token):
            query['lifecycleActionToken'] = request.lifecycle_action_token
        if not UtilClient.is_unset(request.lifecycle_hook_id):
            query['lifecycleHookId'] = request.lifecycle_hook_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecordLifecycleActionHeartbeat',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RecordLifecycleActionHeartbeatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def record_lifecycle_action_heartbeat(
        self,
        request: ess_20220222_models.RecordLifecycleActionHeartbeatRequest,
    ) -> ess_20220222_models.RecordLifecycleActionHeartbeatResponse:
        """
        @summary Extends the time window during which Elastic Compute Service (ECS) instances stay in a Pending state. If the current time window during which an ECS instance stays in a Pending state is not sufficient for you to complete custom operations on the ECS instance, you can call the RecordLifecycleActionHeartbeat operation to extend the time window. When you call this operation, you can specify lifecycleHookId, lifecycleActionToken, and heartbeatTimeout to extend the time window for the desired ECS instance.
        
        @description You can call this operation only when the desired ECS instance enters a Pending state.\\
        An ECS instance can stay in a Pending state for up to six hours. Each time an ECS instance enters a Pending state, you can extend the time window during which the ECS instance stays in a Pending state up to 20 times.
        
        @param request: RecordLifecycleActionHeartbeatRequest
        @return: RecordLifecycleActionHeartbeatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.record_lifecycle_action_heartbeat_with_options(request, runtime)

    async def record_lifecycle_action_heartbeat_async(
        self,
        request: ess_20220222_models.RecordLifecycleActionHeartbeatRequest,
    ) -> ess_20220222_models.RecordLifecycleActionHeartbeatResponse:
        """
        @summary Extends the time window during which Elastic Compute Service (ECS) instances stay in a Pending state. If the current time window during which an ECS instance stays in a Pending state is not sufficient for you to complete custom operations on the ECS instance, you can call the RecordLifecycleActionHeartbeat operation to extend the time window. When you call this operation, you can specify lifecycleHookId, lifecycleActionToken, and heartbeatTimeout to extend the time window for the desired ECS instance.
        
        @description You can call this operation only when the desired ECS instance enters a Pending state.\\
        An ECS instance can stay in a Pending state for up to six hours. Each time an ECS instance enters a Pending state, you can extend the time window during which the ECS instance stays in a Pending state up to 20 times.
        
        @param request: RecordLifecycleActionHeartbeatRequest
        @return: RecordLifecycleActionHeartbeatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.record_lifecycle_action_heartbeat_with_options_async(request, runtime)

    def remove_instances_with_options(
        self,
        request: ess_20220222_models.RemoveInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.RemoveInstancesResponse:
        """
        @summary Removes one or more Elastic Compute Service (ECS) instances or elastic container instances from a scaling group.
        
        @description    Before you call this operation, make sure that the following requirements are met:
        The scaling group is in the Active state.
        No scaling activity is in progress within the scaling group.
        > If no scaling activity is in progress within the scaling group, you can call the operation even within the cooldown period.
        If an ECS instance is automatically created by Auto Scaling, or if an ECS instance is manually added to a scaling group and managed by the scaling group, the ECS instance is stopped in economical mode or is released after the instance is removed from the scaling group.
        If an ECS instance is manually added to a scaling group and is not managed by the scaling group, the ECS instance is not stopped or released after the instance is removed from the scaling group.
        If the difference between the number of existing ECS instances specified by the TotalCapacity parameter and the number of ECS instances that you call this operation to remove is less than the value of the MinSize parameter, the call fails.
        A successful call only means that Auto Scaling accepts the request. The scaling activity may still fail. You can obtain the status of a scaling activity based on the value of the ScalingActivityId parameter in the response.
        
        @param request: RemoveInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.decrease_desired_capacity):
            query['DecreaseDesiredCapacity'] = request.decrease_desired_capacity
        if not UtilClient.is_unset(request.ignore_invalid_instance):
            query['IgnoreInvalidInstance'] = request.ignore_invalid_instance
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_policy):
            query['RemovePolicy'] = request.remove_policy
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RemoveInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_instances_with_options_async(
        self,
        request: ess_20220222_models.RemoveInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.RemoveInstancesResponse:
        """
        @summary Removes one or more Elastic Compute Service (ECS) instances or elastic container instances from a scaling group.
        
        @description    Before you call this operation, make sure that the following requirements are met:
        The scaling group is in the Active state.
        No scaling activity is in progress within the scaling group.
        > If no scaling activity is in progress within the scaling group, you can call the operation even within the cooldown period.
        If an ECS instance is automatically created by Auto Scaling, or if an ECS instance is manually added to a scaling group and managed by the scaling group, the ECS instance is stopped in economical mode or is released after the instance is removed from the scaling group.
        If an ECS instance is manually added to a scaling group and is not managed by the scaling group, the ECS instance is not stopped or released after the instance is removed from the scaling group.
        If the difference between the number of existing ECS instances specified by the TotalCapacity parameter and the number of ECS instances that you call this operation to remove is less than the value of the MinSize parameter, the call fails.
        A successful call only means that Auto Scaling accepts the request. The scaling activity may still fail. You can obtain the status of a scaling activity based on the value of the ScalingActivityId parameter in the response.
        
        @param request: RemoveInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.decrease_desired_capacity):
            query['DecreaseDesiredCapacity'] = request.decrease_desired_capacity
        if not UtilClient.is_unset(request.ignore_invalid_instance):
            query['IgnoreInvalidInstance'] = request.ignore_invalid_instance
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remove_policy):
            query['RemovePolicy'] = request.remove_policy
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveInstances',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.RemoveInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_instances(
        self,
        request: ess_20220222_models.RemoveInstancesRequest,
    ) -> ess_20220222_models.RemoveInstancesResponse:
        """
        @summary Removes one or more Elastic Compute Service (ECS) instances or elastic container instances from a scaling group.
        
        @description    Before you call this operation, make sure that the following requirements are met:
        The scaling group is in the Active state.
        No scaling activity is in progress within the scaling group.
        > If no scaling activity is in progress within the scaling group, you can call the operation even within the cooldown period.
        If an ECS instance is automatically created by Auto Scaling, or if an ECS instance is manually added to a scaling group and managed by the scaling group, the ECS instance is stopped in economical mode or is released after the instance is removed from the scaling group.
        If an ECS instance is manually added to a scaling group and is not managed by the scaling group, the ECS instance is not stopped or released after the instance is removed from the scaling group.
        If the difference between the number of existing ECS instances specified by the TotalCapacity parameter and the number of ECS instances that you call this operation to remove is less than the value of the MinSize parameter, the call fails.
        A successful call only means that Auto Scaling accepts the request. The scaling activity may still fail. You can obtain the status of a scaling activity based on the value of the ScalingActivityId parameter in the response.
        
        @param request: RemoveInstancesRequest
        @return: RemoveInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_instances_with_options(request, runtime)

    async def remove_instances_async(
        self,
        request: ess_20220222_models.RemoveInstancesRequest,
    ) -> ess_20220222_models.RemoveInstancesResponse:
        """
        @summary Removes one or more Elastic Compute Service (ECS) instances or elastic container instances from a scaling group.
        
        @description    Before you call this operation, make sure that the following requirements are met:
        The scaling group is in the Active state.
        No scaling activity is in progress within the scaling group.
        > If no scaling activity is in progress within the scaling group, you can call the operation even within the cooldown period.
        If an ECS instance is automatically created by Auto Scaling, or if an ECS instance is manually added to a scaling group and managed by the scaling group, the ECS instance is stopped in economical mode or is released after the instance is removed from the scaling group.
        If an ECS instance is manually added to a scaling group and is not managed by the scaling group, the ECS instance is not stopped or released after the instance is removed from the scaling group.
        If the difference between the number of existing ECS instances specified by the TotalCapacity parameter and the number of ECS instances that you call this operation to remove is less than the value of the MinSize parameter, the call fails.
        A successful call only means that Auto Scaling accepts the request. The scaling activity may still fail. You can obtain the status of a scaling activity based on the value of the ScalingActivityId parameter in the response.
        
        @param request: RemoveInstancesRequest
        @return: RemoveInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_instances_with_options_async(request, runtime)

    def resume_processes_with_options(
        self,
        request: ess_20220222_models.ResumeProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ResumeProcessesResponse:
        """
        @summary Resumes suspended processes in a scaling group.
        
        @param request: ResumeProcessesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeProcessesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.processes):
            query['Processes'] = request.processes
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeProcesses',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ResumeProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_processes_with_options_async(
        self,
        request: ess_20220222_models.ResumeProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ResumeProcessesResponse:
        """
        @summary Resumes suspended processes in a scaling group.
        
        @param request: ResumeProcessesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeProcessesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.processes):
            query['Processes'] = request.processes
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeProcesses',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ResumeProcessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_processes(
        self,
        request: ess_20220222_models.ResumeProcessesRequest,
    ) -> ess_20220222_models.ResumeProcessesResponse:
        """
        @summary Resumes suspended processes in a scaling group.
        
        @param request: ResumeProcessesRequest
        @return: ResumeProcessesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_processes_with_options(request, runtime)

    async def resume_processes_async(
        self,
        request: ess_20220222_models.ResumeProcessesRequest,
    ) -> ess_20220222_models.ResumeProcessesResponse:
        """
        @summary Resumes suspended processes in a scaling group.
        
        @param request: ResumeProcessesRequest
        @return: ResumeProcessesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_processes_with_options_async(request, runtime)

    def scale_with_adjustment_with_options(
        self,
        tmp_req: ess_20220222_models.ScaleWithAdjustmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ScaleWithAdjustmentResponse:
        """
        @summary Scales instances. The ScaleWithAdjustment operation differs from the ExecuteScalingRule operation in that ScaleWithAdjust can directly scale instances without requiring you to create a scaling rule in advance.
        
        @description    Before you call this operation, take note of the following items:
        The scaling group is in the Active state.
        The scaling group has no ongoing scaling activities.
        If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities before the cooldown period of the scaling group expires.
        If the addition of a specific number of Elastic Compute Service (ECS) instances to the scaling group causes the total number of ECS instances in the scaling group to exceed the maximum allowed number, Auto Scaling adds ECS instances to the scaling group until the total number of instances is equal to the maximum allowed number.
        If the removal of a specific number of ECS instances from the scaling group causes the total number of ECS instances in the scaling group to be less than the minimum allowed number, Auto Scaling removes ECS instances from the scaling group until the total number of instances is equal to the minimum allowed number.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity based on the value of `ScalingActivityId` in the response.
        
        @param tmp_req: ScaleWithAdjustmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleWithAdjustmentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ess_20220222_models.ScaleWithAdjustmentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lifecycle_hook_context):
            request.lifecycle_hook_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lifecycle_hook_context, 'LifecycleHookContext', 'json')
        if not UtilClient.is_unset(tmp_req.overrides):
            request.overrides_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.overrides, 'Overrides', 'json')
        query = {}
        if not UtilClient.is_unset(request.activity_metadata):
            query['ActivityMetadata'] = request.activity_metadata
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lifecycle_hook_context_shrink):
            query['LifecycleHookContext'] = request.lifecycle_hook_context_shrink
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.overrides_shrink):
            query['Overrides'] = request.overrides_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.sync_activity):
            query['SyncActivity'] = request.sync_activity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleWithAdjustment',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ScaleWithAdjustmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_with_adjustment_with_options_async(
        self,
        tmp_req: ess_20220222_models.ScaleWithAdjustmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.ScaleWithAdjustmentResponse:
        """
        @summary Scales instances. The ScaleWithAdjustment operation differs from the ExecuteScalingRule operation in that ScaleWithAdjust can directly scale instances without requiring you to create a scaling rule in advance.
        
        @description    Before you call this operation, take note of the following items:
        The scaling group is in the Active state.
        The scaling group has no ongoing scaling activities.
        If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities before the cooldown period of the scaling group expires.
        If the addition of a specific number of Elastic Compute Service (ECS) instances to the scaling group causes the total number of ECS instances in the scaling group to exceed the maximum allowed number, Auto Scaling adds ECS instances to the scaling group until the total number of instances is equal to the maximum allowed number.
        If the removal of a specific number of ECS instances from the scaling group causes the total number of ECS instances in the scaling group to be less than the minimum allowed number, Auto Scaling removes ECS instances from the scaling group until the total number of instances is equal to the minimum allowed number.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity based on the value of `ScalingActivityId` in the response.
        
        @param tmp_req: ScaleWithAdjustmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ScaleWithAdjustmentResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ess_20220222_models.ScaleWithAdjustmentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.lifecycle_hook_context):
            request.lifecycle_hook_context_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.lifecycle_hook_context, 'LifecycleHookContext', 'json')
        if not UtilClient.is_unset(tmp_req.overrides):
            request.overrides_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.overrides, 'Overrides', 'json')
        query = {}
        if not UtilClient.is_unset(request.activity_metadata):
            query['ActivityMetadata'] = request.activity_metadata
        if not UtilClient.is_unset(request.adjustment_type):
            query['AdjustmentType'] = request.adjustment_type
        if not UtilClient.is_unset(request.adjustment_value):
            query['AdjustmentValue'] = request.adjustment_value
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.lifecycle_hook_context_shrink):
            query['LifecycleHookContext'] = request.lifecycle_hook_context_shrink
        if not UtilClient.is_unset(request.min_adjustment_magnitude):
            query['MinAdjustmentMagnitude'] = request.min_adjustment_magnitude
        if not UtilClient.is_unset(request.overrides_shrink):
            query['Overrides'] = request.overrides_shrink
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        if not UtilClient.is_unset(request.sync_activity):
            query['SyncActivity'] = request.sync_activity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleWithAdjustment',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.ScaleWithAdjustmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_with_adjustment(
        self,
        request: ess_20220222_models.ScaleWithAdjustmentRequest,
    ) -> ess_20220222_models.ScaleWithAdjustmentResponse:
        """
        @summary Scales instances. The ScaleWithAdjustment operation differs from the ExecuteScalingRule operation in that ScaleWithAdjust can directly scale instances without requiring you to create a scaling rule in advance.
        
        @description    Before you call this operation, take note of the following items:
        The scaling group is in the Active state.
        The scaling group has no ongoing scaling activities.
        If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities before the cooldown period of the scaling group expires.
        If the addition of a specific number of Elastic Compute Service (ECS) instances to the scaling group causes the total number of ECS instances in the scaling group to exceed the maximum allowed number, Auto Scaling adds ECS instances to the scaling group until the total number of instances is equal to the maximum allowed number.
        If the removal of a specific number of ECS instances from the scaling group causes the total number of ECS instances in the scaling group to be less than the minimum allowed number, Auto Scaling removes ECS instances from the scaling group until the total number of instances is equal to the minimum allowed number.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity based on the value of `ScalingActivityId` in the response.
        
        @param request: ScaleWithAdjustmentRequest
        @return: ScaleWithAdjustmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.scale_with_adjustment_with_options(request, runtime)

    async def scale_with_adjustment_async(
        self,
        request: ess_20220222_models.ScaleWithAdjustmentRequest,
    ) -> ess_20220222_models.ScaleWithAdjustmentResponse:
        """
        @summary Scales instances. The ScaleWithAdjustment operation differs from the ExecuteScalingRule operation in that ScaleWithAdjust can directly scale instances without requiring you to create a scaling rule in advance.
        
        @description    Before you call this operation, take note of the following items:
        The scaling group is in the Active state.
        The scaling group has no ongoing scaling activities.
        If no scaling activities in the scaling group are in progress, the operation can trigger scaling activities before the cooldown period of the scaling group expires.
        If the addition of a specific number of Elastic Compute Service (ECS) instances to the scaling group causes the total number of ECS instances in the scaling group to exceed the maximum allowed number, Auto Scaling adds ECS instances to the scaling group until the total number of instances is equal to the maximum allowed number.
        If the removal of a specific number of ECS instances from the scaling group causes the total number of ECS instances in the scaling group to be less than the minimum allowed number, Auto Scaling removes ECS instances from the scaling group until the total number of instances is equal to the minimum allowed number.
        A successful call indicates that Auto Scaling accepts the request. However, the scaling activity may still fail. You can obtain the status of a scaling activity based on the value of `ScalingActivityId` in the response.
        
        @param request: ScaleWithAdjustmentRequest
        @return: ScaleWithAdjustmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.scale_with_adjustment_with_options_async(request, runtime)

    def set_group_deletion_protection_with_options(
        self,
        request: ess_20220222_models.SetGroupDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SetGroupDeletionProtectionResponse:
        """
        @summary Sets deletion protection for a scaling group. If you enable deletion protection for a scaling group, you cannot delete the scaling group. If you disable deletion protection for a scaling group, you can directly delete the scaling group. You can call the SetGroupDeletionProtection operation to enable or disable deletion protection.
        
        @param request: SetGroupDeletionProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetGroupDeletionProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGroupDeletionProtection',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetGroupDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_group_deletion_protection_with_options_async(
        self,
        request: ess_20220222_models.SetGroupDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SetGroupDeletionProtectionResponse:
        """
        @summary Sets deletion protection for a scaling group. If you enable deletion protection for a scaling group, you cannot delete the scaling group. If you disable deletion protection for a scaling group, you can directly delete the scaling group. You can call the SetGroupDeletionProtection operation to enable or disable deletion protection.
        
        @param request: SetGroupDeletionProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetGroupDeletionProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_deletion_protection):
            query['GroupDeletionProtection'] = request.group_deletion_protection
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetGroupDeletionProtection',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetGroupDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_group_deletion_protection(
        self,
        request: ess_20220222_models.SetGroupDeletionProtectionRequest,
    ) -> ess_20220222_models.SetGroupDeletionProtectionResponse:
        """
        @summary Sets deletion protection for a scaling group. If you enable deletion protection for a scaling group, you cannot delete the scaling group. If you disable deletion protection for a scaling group, you can directly delete the scaling group. You can call the SetGroupDeletionProtection operation to enable or disable deletion protection.
        
        @param request: SetGroupDeletionProtectionRequest
        @return: SetGroupDeletionProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_group_deletion_protection_with_options(request, runtime)

    async def set_group_deletion_protection_async(
        self,
        request: ess_20220222_models.SetGroupDeletionProtectionRequest,
    ) -> ess_20220222_models.SetGroupDeletionProtectionResponse:
        """
        @summary Sets deletion protection for a scaling group. If you enable deletion protection for a scaling group, you cannot delete the scaling group. If you disable deletion protection for a scaling group, you can directly delete the scaling group. You can call the SetGroupDeletionProtection operation to enable or disable deletion protection.
        
        @param request: SetGroupDeletionProtectionRequest
        @return: SetGroupDeletionProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_group_deletion_protection_with_options_async(request, runtime)

    def set_instance_health_with_options(
        self,
        request: ess_20220222_models.SetInstanceHealthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SetInstanceHealthResponse:
        """
        @summary Sets instance health. At times, the automatic health check system might not sufficiently determine the precise health status of your Elastic Compute Service (ECS) instances or elastic container instances. To overcome this, you can call the SetInstanceHealth operation to swiftly pinpoint problematic instances and resolve issues. This operation is designed to more precisely align with real-world business requirements and tackle O\\&M hurdles efficiently.
        
        @description Auto Scaling detects and removes unhealthy ECS instances or elastic container instances from the corresponding scaling groups. If you want to retain a specific instance in the corresponding scaling group, you can put the instance into the Standby or Protected state. For more information, see [EnterStandby](~~EnterStandby~~) and [SetInstancesProtection](~~SetInstancesProtection~~).
        
        @param request: SetInstanceHealthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetInstanceHealthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetInstanceHealth',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetInstanceHealthResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_instance_health_with_options_async(
        self,
        request: ess_20220222_models.SetInstanceHealthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SetInstanceHealthResponse:
        """
        @summary Sets instance health. At times, the automatic health check system might not sufficiently determine the precise health status of your Elastic Compute Service (ECS) instances or elastic container instances. To overcome this, you can call the SetInstanceHealth operation to swiftly pinpoint problematic instances and resolve issues. This operation is designed to more precisely align with real-world business requirements and tackle O\\&M hurdles efficiently.
        
        @description Auto Scaling detects and removes unhealthy ECS instances or elastic container instances from the corresponding scaling groups. If you want to retain a specific instance in the corresponding scaling group, you can put the instance into the Standby or Protected state. For more information, see [EnterStandby](~~EnterStandby~~) and [SetInstancesProtection](~~SetInstancesProtection~~).
        
        @param request: SetInstanceHealthRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetInstanceHealthResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.health_status):
            query['HealthStatus'] = request.health_status
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetInstanceHealth',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetInstanceHealthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_instance_health(
        self,
        request: ess_20220222_models.SetInstanceHealthRequest,
    ) -> ess_20220222_models.SetInstanceHealthResponse:
        """
        @summary Sets instance health. At times, the automatic health check system might not sufficiently determine the precise health status of your Elastic Compute Service (ECS) instances or elastic container instances. To overcome this, you can call the SetInstanceHealth operation to swiftly pinpoint problematic instances and resolve issues. This operation is designed to more precisely align with real-world business requirements and tackle O\\&M hurdles efficiently.
        
        @description Auto Scaling detects and removes unhealthy ECS instances or elastic container instances from the corresponding scaling groups. If you want to retain a specific instance in the corresponding scaling group, you can put the instance into the Standby or Protected state. For more information, see [EnterStandby](~~EnterStandby~~) and [SetInstancesProtection](~~SetInstancesProtection~~).
        
        @param request: SetInstanceHealthRequest
        @return: SetInstanceHealthResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_instance_health_with_options(request, runtime)

    async def set_instance_health_async(
        self,
        request: ess_20220222_models.SetInstanceHealthRequest,
    ) -> ess_20220222_models.SetInstanceHealthResponse:
        """
        @summary Sets instance health. At times, the automatic health check system might not sufficiently determine the precise health status of your Elastic Compute Service (ECS) instances or elastic container instances. To overcome this, you can call the SetInstanceHealth operation to swiftly pinpoint problematic instances and resolve issues. This operation is designed to more precisely align with real-world business requirements and tackle O\\&M hurdles efficiently.
        
        @description Auto Scaling detects and removes unhealthy ECS instances or elastic container instances from the corresponding scaling groups. If you want to retain a specific instance in the corresponding scaling group, you can put the instance into the Standby or Protected state. For more information, see [EnterStandby](~~EnterStandby~~) and [SetInstancesProtection](~~SetInstancesProtection~~).
        
        @param request: SetInstanceHealthRequest
        @return: SetInstanceHealthResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_instance_health_with_options_async(request, runtime)

    def set_instances_protection_with_options(
        self,
        request: ess_20220222_models.SetInstancesProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SetInstancesProtectionResponse:
        """
        @summary Puts Elastic Compute Service (ECS) instances into the Protected state. When ECS instances are put into the Protected state, they become immune to manual deletion attempts by using the Auto Scaling console or API operations. This operation serves as a robust safeguard, efficiently preventing any inadvertent instance release that could lead to irreversible consequences.
        
        @description Once ECS instances enter the Protected state, they become subject to the following restrictions:
        ECS instances will persist in the Protected state, unless you deliberately remove them from this state.
        Even in scenarios where automatic scale-in actions are initiated due to fluctuations in the number of ECS instances or the execution of event-triggered tasks, Auto Scaling does not remove ECS instances that are in the Protected state from their respective scaling groups. Only after being manually removed from their respective scaling groups can ECS instances that are in the Protected state be released. For more information, see [Remove an ECS instance](https://help.aliyun.com/document_detail/25955.html).
        ECS instances in the Protected state maintain their existing health status even when they undergo stopping or restarting processes.
        
        @param request: SetInstancesProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetInstancesProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protected_from_scale_in):
            query['ProtectedFromScaleIn'] = request.protected_from_scale_in
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetInstancesProtection',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetInstancesProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_instances_protection_with_options_async(
        self,
        request: ess_20220222_models.SetInstancesProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SetInstancesProtectionResponse:
        """
        @summary Puts Elastic Compute Service (ECS) instances into the Protected state. When ECS instances are put into the Protected state, they become immune to manual deletion attempts by using the Auto Scaling console or API operations. This operation serves as a robust safeguard, efficiently preventing any inadvertent instance release that could lead to irreversible consequences.
        
        @description Once ECS instances enter the Protected state, they become subject to the following restrictions:
        ECS instances will persist in the Protected state, unless you deliberately remove them from this state.
        Even in scenarios where automatic scale-in actions are initiated due to fluctuations in the number of ECS instances or the execution of event-triggered tasks, Auto Scaling does not remove ECS instances that are in the Protected state from their respective scaling groups. Only after being manually removed from their respective scaling groups can ECS instances that are in the Protected state be released. For more information, see [Remove an ECS instance](https://help.aliyun.com/document_detail/25955.html).
        ECS instances in the Protected state maintain their existing health status even when they undergo stopping or restarting processes.
        
        @param request: SetInstancesProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetInstancesProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protected_from_scale_in):
            query['ProtectedFromScaleIn'] = request.protected_from_scale_in
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetInstancesProtection',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SetInstancesProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_instances_protection(
        self,
        request: ess_20220222_models.SetInstancesProtectionRequest,
    ) -> ess_20220222_models.SetInstancesProtectionResponse:
        """
        @summary Puts Elastic Compute Service (ECS) instances into the Protected state. When ECS instances are put into the Protected state, they become immune to manual deletion attempts by using the Auto Scaling console or API operations. This operation serves as a robust safeguard, efficiently preventing any inadvertent instance release that could lead to irreversible consequences.
        
        @description Once ECS instances enter the Protected state, they become subject to the following restrictions:
        ECS instances will persist in the Protected state, unless you deliberately remove them from this state.
        Even in scenarios where automatic scale-in actions are initiated due to fluctuations in the number of ECS instances or the execution of event-triggered tasks, Auto Scaling does not remove ECS instances that are in the Protected state from their respective scaling groups. Only after being manually removed from their respective scaling groups can ECS instances that are in the Protected state be released. For more information, see [Remove an ECS instance](https://help.aliyun.com/document_detail/25955.html).
        ECS instances in the Protected state maintain their existing health status even when they undergo stopping or restarting processes.
        
        @param request: SetInstancesProtectionRequest
        @return: SetInstancesProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_instances_protection_with_options(request, runtime)

    async def set_instances_protection_async(
        self,
        request: ess_20220222_models.SetInstancesProtectionRequest,
    ) -> ess_20220222_models.SetInstancesProtectionResponse:
        """
        @summary Puts Elastic Compute Service (ECS) instances into the Protected state. When ECS instances are put into the Protected state, they become immune to manual deletion attempts by using the Auto Scaling console or API operations. This operation serves as a robust safeguard, efficiently preventing any inadvertent instance release that could lead to irreversible consequences.
        
        @description Once ECS instances enter the Protected state, they become subject to the following restrictions:
        ECS instances will persist in the Protected state, unless you deliberately remove them from this state.
        Even in scenarios where automatic scale-in actions are initiated due to fluctuations in the number of ECS instances or the execution of event-triggered tasks, Auto Scaling does not remove ECS instances that are in the Protected state from their respective scaling groups. Only after being manually removed from their respective scaling groups can ECS instances that are in the Protected state be released. For more information, see [Remove an ECS instance](https://help.aliyun.com/document_detail/25955.html).
        ECS instances in the Protected state maintain their existing health status even when they undergo stopping or restarting processes.
        
        @param request: SetInstancesProtectionRequest
        @return: SetInstancesProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_instances_protection_with_options_async(request, runtime)

    def suspend_processes_with_options(
        self,
        request: ess_20220222_models.SuspendProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SuspendProcessesResponse:
        """
        @summary Suspends scaling processes. This operation empowers you to selectively pause distinct scaling processes within a particular scaling group, enabling you to carry out alternative tasks and achieve more granular management over your scaling operations.
        
        @param request: SuspendProcessesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendProcessesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.processes):
            query['Processes'] = request.processes
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendProcesses',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SuspendProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_processes_with_options_async(
        self,
        request: ess_20220222_models.SuspendProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.SuspendProcessesResponse:
        """
        @summary Suspends scaling processes. This operation empowers you to selectively pause distinct scaling processes within a particular scaling group, enabling you to carry out alternative tasks and achieve more granular management over your scaling operations.
        
        @param request: SuspendProcessesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendProcessesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.processes):
            query['Processes'] = request.processes
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.scaling_group_id):
            query['ScalingGroupId'] = request.scaling_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendProcesses',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.SuspendProcessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_processes(
        self,
        request: ess_20220222_models.SuspendProcessesRequest,
    ) -> ess_20220222_models.SuspendProcessesResponse:
        """
        @summary Suspends scaling processes. This operation empowers you to selectively pause distinct scaling processes within a particular scaling group, enabling you to carry out alternative tasks and achieve more granular management over your scaling operations.
        
        @param request: SuspendProcessesRequest
        @return: SuspendProcessesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_processes_with_options(request, runtime)

    async def suspend_processes_async(
        self,
        request: ess_20220222_models.SuspendProcessesRequest,
    ) -> ess_20220222_models.SuspendProcessesResponse:
        """
        @summary Suspends scaling processes. This operation empowers you to selectively pause distinct scaling processes within a particular scaling group, enabling you to carry out alternative tasks and achieve more granular management over your scaling operations.
        
        @param request: SuspendProcessesRequest
        @return: SuspendProcessesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_processes_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ess_20220222_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.TagResourcesResponse:
        """
        @summary Creates and attaches tags. You can call the TagResources operation to uniformly create and attach tags to your Auto Scaling resources, streamlining resource management. This capability empowers you to categorize resources based on tags, thereby enhancing the overall efficiency of resource allocation and utilization.
        
        @description    You can attach up to 20 tags to a scaling group.
        *\
        *Note** Before you attach tags to a specific Auto Scaling resource, Alibaba Cloud automatically verifies the current number of tags attached to that resource. In the event the proposed addition would exceed the maximum allowed number of tags, an error message will be promptly returned after you call this operation.
        If you set `Tags.Propagate` to `true`, any tags attached to your scaling group will be automatically propagated to new instances that are subsequently created in the scaling group, without affecting existing instances.
        If both the scaling configuration and the scaling group have tags attached, and tag propagation from the scaling group is enabled, the tags of newly created instances comply with the following rules:
        Instances set to join the scaling group will inherit the following tags: tags attached to the scaling configuration that initiates the instance creation and tags attached to the scaling group that are allowed to propagate to these instances upon instance creation.
        If the tag keys of the scaling configuration and those attached to the scaling group and propagated to the instances are identical, the tags attached to the scaling group and propagated to the instances will be overwritten by the tags of the scaling configuration.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ess_20220222_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.TagResourcesResponse:
        """
        @summary Creates and attaches tags. You can call the TagResources operation to uniformly create and attach tags to your Auto Scaling resources, streamlining resource management. This capability empowers you to categorize resources based on tags, thereby enhancing the overall efficiency of resource allocation and utilization.
        
        @description    You can attach up to 20 tags to a scaling group.
        *\
        *Note** Before you attach tags to a specific Auto Scaling resource, Alibaba Cloud automatically verifies the current number of tags attached to that resource. In the event the proposed addition would exceed the maximum allowed number of tags, an error message will be promptly returned after you call this operation.
        If you set `Tags.Propagate` to `true`, any tags attached to your scaling group will be automatically propagated to new instances that are subsequently created in the scaling group, without affecting existing instances.
        If both the scaling configuration and the scaling group have tags attached, and tag propagation from the scaling group is enabled, the tags of newly created instances comply with the following rules:
        Instances set to join the scaling group will inherit the following tags: tags attached to the scaling configuration that initiates the instance creation and tags attached to the scaling group that are allowed to propagate to these instances upon instance creation.
        If the tag keys of the scaling configuration and those attached to the scaling group and propagated to the instances are identical, the tags attached to the scaling group and propagated to the instances will be overwritten by the tags of the scaling configuration.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: ess_20220222_models.TagResourcesRequest,
    ) -> ess_20220222_models.TagResourcesResponse:
        """
        @summary Creates and attaches tags. You can call the TagResources operation to uniformly create and attach tags to your Auto Scaling resources, streamlining resource management. This capability empowers you to categorize resources based on tags, thereby enhancing the overall efficiency of resource allocation and utilization.
        
        @description    You can attach up to 20 tags to a scaling group.
        *\
        *Note** Before you attach tags to a specific Auto Scaling resource, Alibaba Cloud automatically verifies the current number of tags attached to that resource. In the event the proposed addition would exceed the maximum allowed number of tags, an error message will be promptly returned after you call this operation.
        If you set `Tags.Propagate` to `true`, any tags attached to your scaling group will be automatically propagated to new instances that are subsequently created in the scaling group, without affecting existing instances.
        If both the scaling configuration and the scaling group have tags attached, and tag propagation from the scaling group is enabled, the tags of newly created instances comply with the following rules:
        Instances set to join the scaling group will inherit the following tags: tags attached to the scaling configuration that initiates the instance creation and tags attached to the scaling group that are allowed to propagate to these instances upon instance creation.
        If the tag keys of the scaling configuration and those attached to the scaling group and propagated to the instances are identical, the tags attached to the scaling group and propagated to the instances will be overwritten by the tags of the scaling configuration.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ess_20220222_models.TagResourcesRequest,
    ) -> ess_20220222_models.TagResourcesResponse:
        """
        @summary Creates and attaches tags. You can call the TagResources operation to uniformly create and attach tags to your Auto Scaling resources, streamlining resource management. This capability empowers you to categorize resources based on tags, thereby enhancing the overall efficiency of resource allocation and utilization.
        
        @description    You can attach up to 20 tags to a scaling group.
        *\
        *Note** Before you attach tags to a specific Auto Scaling resource, Alibaba Cloud automatically verifies the current number of tags attached to that resource. In the event the proposed addition would exceed the maximum allowed number of tags, an error message will be promptly returned after you call this operation.
        If you set `Tags.Propagate` to `true`, any tags attached to your scaling group will be automatically propagated to new instances that are subsequently created in the scaling group, without affecting existing instances.
        If both the scaling configuration and the scaling group have tags attached, and tag propagation from the scaling group is enabled, the tags of newly created instances comply with the following rules:
        Instances set to join the scaling group will inherit the following tags: tags attached to the scaling configuration that initiates the instance creation and tags attached to the scaling group that are allowed to propagate to these instances upon instance creation.
        If the tag keys of the scaling configuration and those attached to the scaling group and propagated to the instances are identical, the tags attached to the scaling group and propagated to the instances will be overwritten by the tags of the scaling configuration.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ess_20220222_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.UntagResourcesResponse:
        """
        @summary Removes tags from Auto Scaling resources simultaneously. This operation streamlines resource management activities, enhances system efficiency, and mitigates potential security vulnerabilities. Once a tag is removed from a particular resource, and if it is not re-added to any other resource, the system will automatically delete the unused tag.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ess_20220222_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.UntagResourcesResponse:
        """
        @summary Removes tags from Auto Scaling resources simultaneously. This operation streamlines resource management activities, enhances system efficiency, and mitigates potential security vulnerabilities. Once a tag is removed from a particular resource, and if it is not re-added to any other resource, the system will automatically delete the unused tag.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: ess_20220222_models.UntagResourcesRequest,
    ) -> ess_20220222_models.UntagResourcesResponse:
        """
        @summary Removes tags from Auto Scaling resources simultaneously. This operation streamlines resource management activities, enhances system efficiency, and mitigates potential security vulnerabilities. Once a tag is removed from a particular resource, and if it is not re-added to any other resource, the system will automatically delete the unused tag.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ess_20220222_models.UntagResourcesRequest,
    ) -> ess_20220222_models.UntagResourcesResponse:
        """
        @summary Removes tags from Auto Scaling resources simultaneously. This operation streamlines resource management activities, enhances system efficiency, and mitigates potential security vulnerabilities. Once a tag is removed from a particular resource, and if it is not re-added to any other resource, the system will automatically delete the unused tag.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def verify_authentication_with_options(
        self,
        request: ess_20220222_models.VerifyAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.VerifyAuthenticationResponse:
        """
        @summary Checks whether Auto Scaling is authorized to access Elastic Compute Service (ECS) and Elastic Container Instance resources.
        
        @param request: VerifyAuthenticationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyAuthenticationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.only_check):
            query['OnlyCheck'] = request.only_check
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyAuthentication',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.VerifyAuthenticationResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_authentication_with_options_async(
        self,
        request: ess_20220222_models.VerifyAuthenticationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.VerifyAuthenticationResponse:
        """
        @summary Checks whether Auto Scaling is authorized to access Elastic Compute Service (ECS) and Elastic Container Instance resources.
        
        @param request: VerifyAuthenticationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyAuthenticationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.only_check):
            query['OnlyCheck'] = request.only_check
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.uid):
            query['Uid'] = request.uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyAuthentication',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.VerifyAuthenticationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_authentication(
        self,
        request: ess_20220222_models.VerifyAuthenticationRequest,
    ) -> ess_20220222_models.VerifyAuthenticationResponse:
        """
        @summary Checks whether Auto Scaling is authorized to access Elastic Compute Service (ECS) and Elastic Container Instance resources.
        
        @param request: VerifyAuthenticationRequest
        @return: VerifyAuthenticationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_authentication_with_options(request, runtime)

    async def verify_authentication_async(
        self,
        request: ess_20220222_models.VerifyAuthenticationRequest,
    ) -> ess_20220222_models.VerifyAuthenticationResponse:
        """
        @summary Checks whether Auto Scaling is authorized to access Elastic Compute Service (ECS) and Elastic Container Instance resources.
        
        @param request: VerifyAuthenticationRequest
        @return: VerifyAuthenticationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_authentication_with_options_async(request, runtime)

    def verify_user_with_options(
        self,
        request: ess_20220222_models.VerifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.VerifyUserResponse:
        """
        @summary Verifies whether Auto Scaling is activated. This operation guarantees that in response to shifts in business workloads or variations in incoming traffic, the system will automatically adjust resource provisioning. This auto-scaling capability enhances the overall system performance, ensuring high availability and improved flexibility to accommodate dynamic demands.
        
        @param request: VerifyUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyUser',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.VerifyUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_user_with_options_async(
        self,
        request: ess_20220222_models.VerifyUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ess_20220222_models.VerifyUserResponse:
        """
        @summary Verifies whether Auto Scaling is activated. This operation guarantees that in response to shifts in business workloads or variations in incoming traffic, the system will automatically adjust resource provisioning. This auto-scaling capability enhances the overall system performance, ensuring high availability and improved flexibility to accommodate dynamic demands.
        
        @param request: VerifyUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyUser',
            version='2022-02-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ess_20220222_models.VerifyUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_user(
        self,
        request: ess_20220222_models.VerifyUserRequest,
    ) -> ess_20220222_models.VerifyUserResponse:
        """
        @summary Verifies whether Auto Scaling is activated. This operation guarantees that in response to shifts in business workloads or variations in incoming traffic, the system will automatically adjust resource provisioning. This auto-scaling capability enhances the overall system performance, ensuring high availability and improved flexibility to accommodate dynamic demands.
        
        @param request: VerifyUserRequest
        @return: VerifyUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_user_with_options(request, runtime)

    async def verify_user_async(
        self,
        request: ess_20220222_models.VerifyUserRequest,
    ) -> ess_20220222_models.VerifyUserResponse:
        """
        @summary Verifies whether Auto Scaling is activated. This operation guarantees that in response to shifts in business workloads or variations in incoming traffic, the system will automatically adjust resource provisioning. This auto-scaling capability enhances the overall system performance, ensuring high availability and improved flexibility to accommodate dynamic demands.
        
        @param request: VerifyUserRequest
        @return: VerifyUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_user_with_options_async(request, runtime)
