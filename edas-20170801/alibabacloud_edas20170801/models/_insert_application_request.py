# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InsertApplicationRequest(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        build_pack_id: int = None,
        cluster_id: str = None,
        component_ids: str = None,
        cpu: int = None,
        description: str = None,
        ecu_info: str = None,
        enable_port_check: bool = None,
        enable_url_check: bool = None,
        health_check_url: str = None,
        hooks: str = None,
        jdk: str = None,
        jvm_options: str = None,
        logical_region_id: str = None,
        max_heap_size: int = None,
        max_perm_size: int = None,
        mem: int = None,
        min_heap_size: int = None,
        package_type: str = None,
        reserved_port_str: str = None,
        resource_group_id: str = None,
        web_container: str = None,
    ):
        # The name of the application. The name can contain only digits, letters, hyphens (-), and underscores (_). It must start with a letter and can be up to 36 characters in length.
        # 
        # This parameter is required.
        self.application_name = application_name
        # The build package number of EDAS-Container. This parameter is required when you create a High-speed Service Framework (HSF) application. You can obtain the build package number in one of the following ways:
        # 
        # - Call the ListBuildPack operation. For more information, see [ListBuildPack](https://help.aliyun.com/document_detail/149391.html).
        # 
        # - Obtain the build package number from the **Build Package Number** column in the [Container versions](https://help.aliyun.com/document_detail/92614.html) table.
        self.build_pack_id = build_pack_id
        # The ID of the ECS cluster. Specify this parameter to create the application in a specific ECS cluster. If you leave this parameter empty, the application is created in the default cluster. We recommend that you specify this parameter.
        self.cluster_id = cluster_id
        # The ID of the application component. You can call the ListComponents operation to query the component ID. For more information, see [ListComponents](https://help.aliyun.com/document_detail/97502.html).
        # 
        # This parameter is required if the application runs in an Apache Tomcat container (for Dubbo applications that are deployed in a WAR package) or a standard Java application runtime environment (for Spring Boot or Spring Cloud applications that are deployed in a JAR package).
        # 
        # The following application component IDs are commonly used:
        # 
        # - 4: Apache Tomcat 7.0.91
        # 
        # - 7: Apache Tomcat 8.5.42
        # 
        # - 5: OpenJDK 1.8.x
        # 
        # - 6: OpenJDK 1.7.x
        # 
        # To set this parameter, you must update the Java or Python software development kit (SDK) to version 2.57.3 or later. If you do not use an EDAS SDK, such as aliyun-python-sdk-core, aliyun-java-sdk-core, or Alibaba Cloud CLI, you can set this parameter.
        self.component_ids = component_ids
        # \\*\\*(Deprecated)\\*\\* The number of CPU cores for the application container in a Swarm cluster.
        self.cpu = cpu
        # The description of the application.
        self.description = description
        # The \\`ecu_id\\` of the ECS instance to which you want to scale out the application. The \\`ecu_id\\` is the unique ID of an ECS instance that is imported to EDAS. To specify multiple \\`ecu_id\\`s, separate them with commas (,). You can call the ListScaleOutEcu operation to query the \\`ecu_id\\`. For more information, see [ListScaleOutEcu](https://help.aliyun.com/document_detail/149371.html).
        self.ecu_info = ecu_info
        # Specifies whether to enable the port health check. Valid values:
        # 
        # - **true**: Enabled
        # 
        # - **false**: Disabled
        self.enable_port_check = enable_port_check
        # Specifies whether to enable the health check URL. Valid values:
        # 
        # - **true**: Enabled
        # 
        # - **false**: Disabled
        self.enable_url_check = enable_url_check
        # The health check URL of the application. This parameter is equivalent to the HealthCheckURL parameter.
        self.health_check_url = health_check_url
        # The configuration of the mounted script. The value is a JSON string. Example:
        # `[{"ignoreFail":false,"name":"postprepareInstanceEnvironmentOnScaleOut","script":"ls"},{"ignoreFail":true,"name":"postdeleteInstanceDataOnScaleIn","script":""},{"ignoreFail":true,"name":"prestartInstance","script":""},{"ignoreFail":true,"name":"poststartInstance","script":""},{"ignoreFail":true,"name":"prestopInstance","script":""},{"ignoreFail":true,"name":"poststopInstance","script":""}]`
        self.hooks = hooks
        # **(Deprecated)** The version of the Java Development Kit (JDK) that the application uses.
        self.jdk = jdk
        # The custom parameters.
        self.jvm_options = jvm_options
        # The ID of the microservices namespace. In the EDAS console, choose **Resource Management** > **Microservices Namespace** in the navigation pane on the left to view the ID of the microservices namespace. You can also call the ListUserDefineRegion operation to query the ID. For more information, see [ListUserDefineRegion](https://help.aliyun.com/document_detail/149377.html).
        # 
        # - If the specified cluster is not in the default microservices namespace, you must specify this parameter. Otherwise, the \\`application regionId is different with cluster regionId!\\` error is reported.
        # 
        # - If the cluster is in the default microservices namespace, you do not need to specify this parameter. The microservices namespace of the application must be the same as the microservices namespace of the specified cluster.
        self.logical_region_id = logical_region_id
        # The maximum size of the heap memory. Unit: MB.
        self.max_heap_size = max_heap_size
        # The size of the permanent generation memory. Unit: MB.
        self.max_perm_size = max_perm_size
        # \\*\\*(Deprecated)\\*\\* The memory size for the application container in a Swarm cluster.
        self.mem = mem
        # The initial size of the heap memory. Unit: MB.
        self.min_heap_size = min_heap_size
        # The format of the application deployment package. Valid values: war and jar.
        self.package_type = package_type
        # \\*\\*(Deprecated)\\*\\* The reserved port of the application.
        self.reserved_port_str = reserved_port_str
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # **(Deprecated)** The version of Apache Tomcat.
        self.web_container = web_container

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.build_pack_id is not None:
            result['BuildPackId'] = self.build_pack_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.component_ids is not None:
            result['ComponentIds'] = self.component_ids

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.description is not None:
            result['Description'] = self.description

        if self.ecu_info is not None:
            result['EcuInfo'] = self.ecu_info

        if self.enable_port_check is not None:
            result['EnablePortCheck'] = self.enable_port_check

        if self.enable_url_check is not None:
            result['EnableUrlCheck'] = self.enable_url_check

        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url

        if self.hooks is not None:
            result['Hooks'] = self.hooks

        if self.jdk is not None:
            result['Jdk'] = self.jdk

        if self.jvm_options is not None:
            result['JvmOptions'] = self.jvm_options

        if self.logical_region_id is not None:
            result['LogicalRegionId'] = self.logical_region_id

        if self.max_heap_size is not None:
            result['MaxHeapSize'] = self.max_heap_size

        if self.max_perm_size is not None:
            result['MaxPermSize'] = self.max_perm_size

        if self.mem is not None:
            result['Mem'] = self.mem

        if self.min_heap_size is not None:
            result['MinHeapSize'] = self.min_heap_size

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.reserved_port_str is not None:
            result['ReservedPortStr'] = self.reserved_port_str

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.web_container is not None:
            result['WebContainer'] = self.web_container

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('BuildPackId') is not None:
            self.build_pack_id = m.get('BuildPackId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ComponentIds') is not None:
            self.component_ids = m.get('ComponentIds')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EcuInfo') is not None:
            self.ecu_info = m.get('EcuInfo')

        if m.get('EnablePortCheck') is not None:
            self.enable_port_check = m.get('EnablePortCheck')

        if m.get('EnableUrlCheck') is not None:
            self.enable_url_check = m.get('EnableUrlCheck')

        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')

        if m.get('Hooks') is not None:
            self.hooks = m.get('Hooks')

        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')

        if m.get('JvmOptions') is not None:
            self.jvm_options = m.get('JvmOptions')

        if m.get('LogicalRegionId') is not None:
            self.logical_region_id = m.get('LogicalRegionId')

        if m.get('MaxHeapSize') is not None:
            self.max_heap_size = m.get('MaxHeapSize')

        if m.get('MaxPermSize') is not None:
            self.max_perm_size = m.get('MaxPermSize')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        if m.get('MinHeapSize') is not None:
            self.min_heap_size = m.get('MinHeapSize')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('ReservedPortStr') is not None:
            self.reserved_port_str = m.get('ReservedPortStr')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')

        return self

