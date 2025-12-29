# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationGroupsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.DescribeApplicationGroupsResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The information about the instance groups of the application.
        self.data = data
        # The error code. Valid values:
        # 
        # *   If the call is successful, the **ErrorCode** parameter is not returned.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the instance groups of an application were obtained. Valid values:
        # 
        # *   **true**: The instance groups were obtained.
        # *   **false**: The instance groups failed to be obtained.
        self.success = success
        # The trace ID that is used to query the details of the request.
        self.trace_id = trace_id

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeApplicationGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribeApplicationGroupsResponseBodyData(DaraModel):
    def __init__(
        self,
        edas_container_version: str = None,
        group_id: str = None,
        group_name: str = None,
        group_type: int = None,
        image_url: str = None,
        jdk: str = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        package_version_id: str = None,
        replicas: int = None,
        running_instances: int = None,
        web_container: str = None,
    ):
        # The version of the container, such as Ali-Tomcat, in which an application that is developed based on High-speed Service Framework (HSF) is deployed.
        self.edas_container_version = edas_container_version
        # The ID of the instance group.
        self.group_id = group_id
        # The name of the instance group.
        self.group_name = group_name
        # The type of the instance group.
        self.group_type = group_type
        # The URL of the image. This parameter is returned only if the **PackageType** parameter is set to **Image**.
        self.image_url = image_url
        # The version of the JDK on which the deployment package of the application depends. This parameter is not returned if the **PackageType** parameter is set to **Image**.
        self.jdk = jdk
        # The type of the deployment package. Valid values:
        # 
        # *   If you deploy a Java application, the value of this parameter can be **FatJar**, **War**, or **Image**.
        # 
        # *   If you deploy a PHP application, the value of this parameter can be one of the following values:
        # 
        #     *   **PhpZip**
        #     *   **IMAGE_PHP_5_4**
        #     *   **IMAGE_PHP_5_4_ALPINE**
        #     *   **IMAGE_PHP_5_5**
        #     *   **IMAGE_PHP_5_5_ALPINE**
        #     *   **IMAGE_PHP_5_6**
        #     *   **IMAGE_PHP_5_6_ALPINE**
        #     *   **IMAGE_PHP_7_0**
        #     *   **IMAGE_PHP_7_0_ALPINE**
        #     *   **IMAGE_PHP_7_1**
        #     *   **IMAGE_PHP_7_1_ALPINE**
        #     *   **IMAGE_PHP_7_2**
        #     *   **IMAGE_PHP_7_2_ALPINE**
        #     *   **IMAGE_PHP_7_3**
        #     *   **IMAGE_PHP_7_3_ALPINE**
        self.package_type = package_type
        # The URL of the deployment package. This parameter is returned only if the **PackageType** parameter is set to **FatJar**, **War**, or **PhpZip**.
        self.package_url = package_url
        # The version of the deployment package. This parameter is returned only if the **PackageType** parameter is set to **FatJar**, **War**, or **PhpZip**. The value of this parameter is automatically generated only if the **ImageUrl** is returned.
        self.package_version = package_version
        self.package_version_id = package_version_id
        # The total number of instances.
        self.replicas = replicas
        # The number of running instances.
        self.running_instances = running_instances
        # The version of the Tomcat container on which the deployment package depends. This parameter is not returned if the **PackageType** parameter is set to **Image**.
        self.web_container = web_container

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.jdk is not None:
            result['Jdk'] = self.jdk

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.package_url is not None:
            result['PackageUrl'] = self.package_url

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.package_version_id is not None:
            result['PackageVersionId'] = self.package_version_id

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.running_instances is not None:
            result['RunningInstances'] = self.running_instances

        if self.web_container is not None:
            result['WebContainer'] = self.web_container

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('PackageVersionId') is not None:
            self.package_version_id = m.get('PackageVersionId')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('RunningInstances') is not None:
            self.running_instances = m.get('RunningInstances')

        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')

        return self

