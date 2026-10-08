# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeployApplicationRequest(DaraModel):
    def __init__(
        self,
        app_env: str = None,
        app_id: str = None,
        batch: int = None,
        batch_wait_time: int = None,
        build_pack_id: int = None,
        component_ids: str = None,
        deploy_type: str = None,
        desc: str = None,
        gray: bool = None,
        group_id: str = None,
        image_url: str = None,
        package_version: str = None,
        release_type: int = None,
        traffic_control_strategy: str = None,
        war_url: str = None,
    ):
        # The environment variables of the application. Specify each environment variable by using two key-value pairs. Example: `{"name":"x","value":"y"},{"name":"x2","value":"y2"}`. The `keys` of the two key-value pairs are `name` and `value`.
        self.app_env = app_env
        # The ID of the application. You can call the ListApplication operation to query the application ID. For more information, see [ListApplication](https://help.aliyun.com/document_detail/423162.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The number of batches per instance group.
        # 
        # - If you specify an ID when you set the GroupId parameter, the application is deployed to the specified instance group. The minimum number of batches that can be specified is 1. The maximum number of batches is the maximum number of ECS instances in the Normal state in the instance group. The actual value falls in the range of [1, specified number]. The specified number of batches equals the number of ECS instances in the specified instance group.
        # 
        # - If you set the GroupId parameter to all, the application is deployed to all instance groups. The minimum number of batches that can be specified is 1. The maximum number of batches is the number of ECS instances in the instance group that has the largest number of ECS instances in the Normal state.
        self.batch = batch
        # The wait time between deployment batches for the application. Unit: minutes.
        # 
        # - Default value: 0. If no wait time between deployment batches is needed, set this parameter to 0.
        # 
        # - Maximum value: 5.
        # 
        # If many deployment batches are needed, we recommend that you specify a small value for this parameter. Otherwise, the application deployment is time-consuming.
        self.batch_wait_time = batch_wait_time
        # The build package number of EDAS Container.
        # 
        # - You do not need to set the parameter if you do not need to change the EDAS Container version during the deployment.
        # 
        # - Set the parameter if you need to update the EDAS Container version of the application during the deployment.
        # 
        # You can query the build package number by using one of the following methods:
        # 
        # - Call the ListBuildPack operation. For more information, see [ListBuildPack](https://help.aliyun.com/document_detail/149391.html).
        # 
        # - Obtain the value in the **Build package number** column of the [Release notes for EDAS Container](https://help.aliyun.com/document_detail/92614.html) topic. For example, `59` indicates `EDAS Container 3.5.8`.
        self.build_pack_id = build_pack_id
        # The IDs of the components used by the application. The parameter is not applicable to High-Speed Framework (HSF) applications. You can call the ListComponents operation to query the component IDs. For more information, see [ListComponents](https://help.aliyun.com/document_detail/423223.html).
        # 
        # - If you have specified the component IDs when you create the application, you do not need to set the parameter when you deploy the application.
        # 
        # - Set the parameter if you need to update the component versions for the application during the deployment.
        # 
        # Valid values for common application components:
        # 
        # - 4: Apache Tomcat 7.0.91
        # 
        # - 7: Apache Tomcat 8.5.42
        # 
        # - 5: OpenJDK 1.8.x
        # 
        # - 6: OpenJDK 1.7.x
        # 
        # For more information, see the Common application parameters section of the [InsertApplication](https://help.aliyun.com/document_detail/423185.html) topic.
        self.component_ids = component_ids
        # The deployment mode of the application. Valid values: `url` and `image`. The image value is deprecated. You can deploy an application to a Swarm cluster only by using an image.\\`\\`
        # 
        # This parameter is required.
        self.deploy_type = deploy_type
        # The description of the application deployment.
        self.desc = desc
        # Specifies whether canary release is selected as the deployment method. Valid values:
        # 
        # - true: Canary release is selected.
        # 
        #   - To implement a canary release, specify the GroupId parameter, which specifies the ID of the instance group for the canary release.
        # 
        #   - Canary release can be selected as the deployment method for only one batch.
        # 
        #   - After the canary release is complete, the application is released in regular mode. The Batch parameter specifies the number of batches.
        # 
        # - false: Single-batch release or phased release is selected.
        self.gray = gray
        # The ID of the instance group to which the application is deployed. You can call the ListDeployGroup operation to query the ID of the instance group. For more information, see [ListDeployGroup](https://help.aliyun.com/document_detail/423184.html).
        # 
        # Set the parameter to `all` if you want to deploy the application to all instance groups.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The URL of the application image that is used to deploy the application in a Swarm cluster. We recommend that you use an image that is stored in Alibaba Cloud Container Registry. This parameter is deprecated.
        self.image_url = image_url
        # The version of the application deployment package. The value can be up to 64 characters in length. We recommend that you use a timestamp.
        # 
        # This parameter is required.
        self.package_version = package_version
        # The mode in which the deployment batches are triggered. Valid values:
        # 
        # - 0: automatic.
        # 
        # - 1: You must manually trigger the next batch. You can manually click **Proceed to Next Batch** in the console or call the ContinuePipeline operation to proceed to the next batch. We recommend that you choose the automatic mode when you call an API operation to deploy the application. For more information, see [ContinuePipeline](https://help.aliyun.com/document_detail/126990.html).
        self.release_type = release_type
        # The canary release policy. For more information about canary release policies, see [DeployK8sApplication](https://help.aliyun.com/document_detail/423212.html).
        self.traffic_control_strategy = traffic_control_strategy
        # The URL of the application deployment package. The package can be a WAR or JAR package. This parameter is required if you set the **DeployType** parameter to `url`. We recommend that you specify the URL of an application deployment package that is stored in an Object Storage Service (OSS) bucket.
        self.war_url = war_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_env is not None:
            result['AppEnv'] = self.app_env

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.batch is not None:
            result['Batch'] = self.batch

        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time

        if self.build_pack_id is not None:
            result['BuildPackId'] = self.build_pack_id

        if self.component_ids is not None:
            result['ComponentIds'] = self.component_ids

        if self.deploy_type is not None:
            result['DeployType'] = self.deploy_type

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.gray is not None:
            result['Gray'] = self.gray

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.release_type is not None:
            result['ReleaseType'] = self.release_type

        if self.traffic_control_strategy is not None:
            result['TrafficControlStrategy'] = self.traffic_control_strategy

        if self.war_url is not None:
            result['WarUrl'] = self.war_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppEnv') is not None:
            self.app_env = m.get('AppEnv')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Batch') is not None:
            self.batch = m.get('Batch')

        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')

        if m.get('BuildPackId') is not None:
            self.build_pack_id = m.get('BuildPackId')

        if m.get('ComponentIds') is not None:
            self.component_ids = m.get('ComponentIds')

        if m.get('DeployType') is not None:
            self.deploy_type = m.get('DeployType')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Gray') is not None:
            self.gray = m.get('Gray')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('ReleaseType') is not None:
            self.release_type = m.get('ReleaseType')

        if m.get('TrafficControlStrategy') is not None:
            self.traffic_control_strategy = m.get('TrafficControlStrategy')

        if m.get('WarUrl') is not None:
            self.war_url = m.get('WarUrl')

        return self

