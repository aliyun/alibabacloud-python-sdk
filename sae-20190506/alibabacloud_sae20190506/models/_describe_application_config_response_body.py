# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeApplicationConfigResponseBodyData = None,
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
        # The information about the application.
        self.data = data
        # The returned error code. Valid values:
        # 
        # *   If the call is successful, the **ErrorCode** parameter is not returned.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see the "**Error codes**" section of this topic.
        self.error_code = error_code
        # The returned information.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the configurations of an application were obtained. Valid values:
        # 
        # *   **true**: The configurations were obtained.
        # *   **false**: The configurations failed to be obtained.
        self.success = success
        # The trace ID that is used to query the details of the request.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

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

        if m.get('Data') is not None:
            temp_model = main_models.DescribeApplicationConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

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

class DescribeApplicationConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        acr_instance_id: str = None,
        agent_version: str = None,
        alb_ingress_readiness_gate: str = None,
        app_description: str = None,
        app_id: str = None,
        app_name: str = None,
        app_source: str = None,
        associate_eip: bool = None,
        base_app_id: str = None,
        batch_wait_time: int = None,
        cluster_id: str = None,
        cms_service_id: str = None,
        command: str = None,
        command_args: str = None,
        config_map_mount_desc: List[main_models.DescribeApplicationConfigResponseBodyDataConfigMapMountDesc] = None,
        cpu: int = None,
        custom_host_alias: str = None,
        custom_image_network_type: str = None,
        deployment_name: str = None,
        disk_size: int = None,
        dotnet: str = None,
        edas_container_version: str = None,
        empty_dir_desc: List[main_models.DescribeApplicationConfigResponseBodyDataEmptyDirDesc] = None,
        enable_ahas: str = None,
        enable_cpu_burst: str = None,
        enable_grey_tag_route: bool = None,
        enable_idle: bool = None,
        enable_namespace_agent_version: bool = None,
        enable_new_arms: bool = None,
        enable_prometheus: bool = None,
        envs: str = None,
        gpu_count: str = None,
        gpu_type: str = None,
        headless_pvtz_discovery: str = None,
        html: str = None,
        idle_hour: str = None,
        image_pull_secrets: str = None,
        image_url: str = None,
        init_containers_config: List[main_models.DescribeApplicationConfigResponseBodyDataInitContainersConfig] = None,
        is_stateful: bool = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        kafka_configs: str = None,
        liveness: str = None,
        loki_configs: str = None,
        max_surge_instance_ratio: int = None,
        max_surge_instances: int = None,
        memory: int = None,
        micro_registration: str = None,
        micro_registration_config: str = None,
        microservice_engine_config: str = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        mount_desc: List[main_models.DescribeApplicationConfigResponseBodyDataMountDesc] = None,
        mount_host: str = None,
        mse_application_id: str = None,
        mse_application_name: str = None,
        namespace_id: str = None,
        nas_configs: str = None,
        nas_id: str = None,
        new_sae_version: str = None,
        oidc_role_name: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: List[main_models.DescribeApplicationConfigResponseBodyDataOssMountDescs] = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        php: str = None,
        php_arms_config_location: str = None,
        php_config: str = None,
        php_config_location: str = None,
        post_start: str = None,
        pre_stop: str = None,
        programming_language: str = None,
        pvtz_discovery: str = None,
        python: str = None,
        python_modules: str = None,
        readiness: str = None,
        region_id: str = None,
        replicas: int = None,
        resource_type: str = None,
        secret_mount_desc: List[main_models.DescribeApplicationConfigResponseBodyDataSecretMountDesc] = None,
        security_group_id: str = None,
        service_tags: Dict[str, str] = None,
        sidecar_containers_config: List[main_models.DescribeApplicationConfigResponseBodyDataSidecarContainersConfig] = None,
        sls_configs: str = None,
        sls_log_env_tags: str = None,
        startup_probe: str = None,
        swimlane_pvtz_discovery: str = None,
        tags: List[main_models.DescribeApplicationConfigResponseBodyDataTags] = None,
        termination_grace_period_seconds: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        update_strategy: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        war_start_options: str = None,
        web_container: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) of the RAM role that is used to pull images across accounts. For more information, see [Pull images across Alibaba Cloud accounts](https://help.aliyun.com/document_detail/190675.html) and [Grant permissions across Alibaba Cloud accounts by using a RAM role](https://help.aliyun.com/document_detail/223585.html).
        self.acr_assume_role_arn = acr_assume_role_arn
        # The ID of the Container Registry Enterprise Edition instance.
        self.acr_instance_id = acr_instance_id
        self.agent_version = agent_version
        self.alb_ingress_readiness_gate = alb_ingress_readiness_gate
        # The description of the application.
        self.app_description = app_description
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The SAE application type.
        # 
        # *   micro_service
        # *   web
        # *   job
        self.app_source = app_source
        # Indicates whether an elastic IP address (EIP) is associated with the application instance. Valid values:
        # 
        # *   **true**: The EIP is associated with the application instance.
        # *   **false**: The EIP is not associated with the application instance.
        self.associate_eip = associate_eip
        # The base app ID.
        self.base_app_id = base_app_id
        # The interval between batches in a phased release. Unit: seconds.
        self.batch_wait_time = batch_wait_time
        # The cluster ID.
        self.cluster_id = cluster_id
        self.cms_service_id = cms_service_id
        # The command that is used to start the image. The command must be an existing executable object in the container. Example:
        # 
        # ```
        # 
        # command:
        #       - echo
        #       - abc
        #       - >
        #       - file0
        # ```
        # 
        # In this example, the Command parameter is set to `Command="echo", CommandArgs=["abc", ">", "file0"]`.
        self.command = command
        # The parameters of the image startup command. The CommandArgs parameter contains the parameters that are required for the **Command** parameter. Format:
        # 
        # `["a","b"]`
        # 
        # In the preceding **Command** example, the CommandArgs parameter is set to `CommandArgs=["abc", ">", "file0"]`. The data type of `["abc", ">", "file0"]` must be an array of strings in the JSON format. You do not need to configure this parameter if it does not exist in the Command parameter.
        self.command_args = command_args
        # The details of the ConfigMap.
        self.config_map_mount_desc = config_map_mount_desc
        # The CPU specifications that are required for each instance. Unit: millicores. You cannot set this parameter to 0. Valid values:
        # 
        # *   **500**
        # *   **1000**
        # *   **2000**
        # *   **4000**
        # *   **8000**
        # *   **16000**
        # *   **32000**
        self.cpu = cpu
        # The custom mappings between hostnames and IP addresses in the container. Valid values:
        # 
        # *   **hostName**: the domain name or hostname.
        # *   **ip**: the IP address.
        self.custom_host_alias = custom_host_alias
        # The type of custom image. Set to empty string if using pre-built image.
        # 
        # - internet: public network image.
        # 
        # - intranet: private network image.
        self.custom_image_network_type = custom_image_network_type
        self.deployment_name = deployment_name
        # The disk size. Unit: GB.
        self.disk_size = disk_size
        # The version of .NET.
        # 
        # - .NET 3.1
        # - .NET 5.0
        # - .NET 6.0
        # - .NET 7.0
        # - .NET 8.0
        self.dotnet = dotnet
        # The version of the container, such as Ali-Tomcat, in which an application developed based on High-speed Service Framework (HSF) is deployed.
        self.edas_container_version = edas_container_version
        self.empty_dir_desc = empty_dir_desc
        # Indicates whether access to Application High Availability Service (AHAS) is enabled. Valid values:
        # 
        # *   **true**: Access to AHAS is enabled.
        # *   **false**: Access to AHAS is disabled.
        self.enable_ahas = enable_ahas
        # Enable CPU Burst.
        # 
        # - true: enable
        # 
        # - false: disable
        self.enable_cpu_burst = enable_cpu_burst
        # Indicates whether canary release rules are enabled. Canary release rules apply only to applications in Spring Cloud and Dubbo frameworks. Valid values:
        # 
        # *   **true**: The canary release rules are enabled.
        # *   **false**: The canary release rules are disabled.
        self.enable_grey_tag_route = enable_grey_tag_route
        # Enable idle mode.
        # 
        # - true: enable
        # 
        # - false: disable
        self.enable_idle = enable_idle
        self.enable_namespace_agent_version = enable_namespace_agent_version
        # Enable new ARMS feature.
        # 
        # - true: enable
        # 
        # - false: disable
        self.enable_new_arms = enable_new_arms
        self.enable_prometheus = enable_prometheus
        # The environment variables. Variable description:
        # 
        # *   **name**: the name of the environment variable.
        # *   **value**: the value or reference of the environment variable.
        self.envs = envs
        self.gpu_count = gpu_count
        self.gpu_type = gpu_type
        self.headless_pvtz_discovery = headless_pvtz_discovery
        self.html = html
        self.idle_hour = idle_hour
        # The ID of the corresponding secret dictionary.
        self.image_pull_secrets = image_pull_secrets
        # The URL of the image. This parameter is returned only if the **PackageType** parameter is set to **Image**.
        self.image_url = image_url
        # Initialize container configuration.
        self.init_containers_config = init_containers_config
        self.is_stateful = is_stateful
        # The arguments in the JAR package. The arguments are used to start the application container. The default startup command is `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`.
        self.jar_start_args = jar_start_args
        # The option settings in the JAR package. The settings are used to start the application container. The default startup command is `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`.
        self.jar_start_options = jar_start_options
        # The version of the Java development kit (JDK) on which the deployment package of the application depends. The following versions are supported:
        # 
        # *   **Open JDK 8**
        # *   **Open JDK 7**
        # *   **Dragonwell 11**
        # *   **Dragonwell 8**
        # *   **openjdk-8u191-jdk-alpine3.9**
        # *   **openjdk-7u201-jdk-alpine3.9**
        # 
        # This parameter is not returned if the **PackageType** parameter is set to **Image**.
        self.jdk = jdk
        # The logging configurations of Message Queue for Apache Kafka. The following parameters are involved:
        # 
        # *   **KafkaConfigs**: the configurations of Message Queue for Apache Kafka.
        # 
        # *   **createTime**: the time when the Message Queue for Apache Kafka instance was created.
        # 
        # *   **kafkaTopic**: the message topic that is used to classify messages.
        # 
        # *   **logDir**: the path in which logs are stored.
        # 
        # *   **logType**: the type of collected logs. Valid values:
        # 
        #     *   **file_log**: the file log that is stored in the container. The path of the file logs in the container is returned.
        #     *   **stdout**: the standard output log of the container. You can specify only one stdout value.
        # 
        # *   **kafkaEndpoint**: the endpoint of the Message Queue for Apache Kafka service.
        # 
        # *   **kafkaInstanceId**: the ID of the Message Queue for Apache Kafka instance.
        # 
        # *   **region**: the region where the Message Queue for Apache Kafka instance resides.
        self.kafka_configs = kafka_configs
        # The details of the availability check that was performed on the container. If the container fails this health check multiple times, the system disables and restarts the container. You can use one of the following methods to perform the health check:
        # 
        # *   Sample code of the **exec** method: `{"exec":{"command":["sh","-c","cat/home/admin/start.sh"]},"initialDelaySeconds":30,"periodSeconds":30,"timeoutSeconds":2}`
        # *   Sample code of the **httpGet** method: `{"httpGet":{"path":"/","port":18091,"scheme":"HTTP","isContainKeyWord":true,"keyWord":"SAE"},"initialDelaySeconds":11,"periodSeconds":10,"timeoutSeconds":1}`
        # *   Sample code of the **tcpSocket** method: `{"tcpSocket":{"port":18091},"initialDelaySeconds":11,"periodSeconds":10,"timeoutSeconds":1}`
        # 
        # >  You can use only one method to perform the health check.
        # 
        # The following parameters are involved:
        # 
        # *   **exec.command**: the health check command.
        # *   **httpGet.path**: the request path.
        # *   **httpGet.scheme**: the protocol that is used to perform the health check. Valid values: **HTTP** and **HTTPS**.
        # *   **httpGet.isContainKeyWord**: indicates whether the response contains keywords. Valid values: **true** and **false**. If this field is not returned, the advanced settings are not used.
        # *   **httpGet.keyWord**: the custom keyword. This parameter is available only if the **isContainKeyWord** field is returned.
        # *   **tcpSocket.port**: the port that is used to check the status of TCP connections.
        # *   **initialDelaySeconds**: the delay of the health check. Default value: 10. Unit: seconds.
        # *   **periodSeconds**: the interval at which health checks are performed. Default value: 30. Unit: seconds.
        # *   **timeoutSeconds**: the timeout period of the health check. Default value: 1. Unit: seconds. If you set this parameter to 0 or leave this parameter empty, the timeout period is automatically set to 1 second.
        self.liveness = liveness
        self.loki_configs = loki_configs
        self.max_surge_instance_ratio = max_surge_instance_ratio
        self.max_surge_instances = max_surge_instances
        # The size of memory required by each instance. Unit: MB. You cannot set this parameter to 0. The values of this parameter correspond to the values of the Cpu parameter:
        # 
        # *   This parameter is set to **1024** if the Cpu parameter is set to 500 or 1000.
        # *   This parameter is set to **2048** if the Cpu parameter is set to 500, 1000, or 1000.
        # *   This parameter is set to **4096** if the Cpu parameter is set to 1000, 2000, or 4000.
        # *   This parameter is set to **8192** if the Cpu parameter is set to 2000, 4000, or 8000.
        # *   This parameter is set to **12288** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **16384** if the Cpu parameter is set to 4000, 8000, or 16000.
        # *   This parameter is set to **24567** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **32768** if the Cpu parameter is set to 16000.
        # *   This parameter is set to **65536** if the Cpu parameter is set to 8000, 16000, or 32000.
        # *   This parameter is set to **131072** if the Cpu parameter is set to 32000.
        self.memory = memory
        # The Nacos registry. Valid values:
        # 
        # *   **0**: SAE built-in Nacos registry
        # *   **1**: self-managed Nacos registry
        # *   **2** : MSE Nacos registry
        self.micro_registration = micro_registration
        # The configuration of registration center. Takes effect only the type of registration center is MSE enterprise Nacos.
        self.micro_registration_config = micro_registration_config
        # Configure microservices governance
        # 
        # enable: Whether to enable microservices governance
        # 
        # - true: Enable
        # - false: Disable
        # 
        # mseLosslessRule: Configure lossless online/offline deployment
        # 
        # - delayTime: Delay duration (unit: seconds)
        # - enable: Whether to enable lossless deployment. Set to "true" to enable; set to "false" to disable.
        # - notice: Whether to enable notifications. Set to "true" to enable; set to "false" to disable.
        # - warmupTime: Small-traffic warm-up duration (unit: seconds)
        self.microservice_engine_config = microservice_engine_config
        # The percentage of the minimum number of available instances. Valid values:
        # 
        # *   **-1**: the default value. This value indicates that the minimum number of available instances is not measured by percentage. If you do not configure this parameter, the default value **-1** is used.
        # *   **0 to 100**: indicates that the minimum number of available instances is calculated by using the following formula: Current number of instances × (Value of MinReadyInstanceRatio × 100%). If the calculated result is not an integer, the result is rounded up to the nearest integer. For example, if the percentage is set to **50**% and five instances are available, the minimum number of available instances is 3.
        # 
        # >  If the **MinReadyInstance** and **MinReadyInstanceRatio** parameters are returned and the value of the **MinReadyInstanceRatio** parameter is not **-1**, the value of the **MinReadyInstanceRatio** parameter takes effect. If the **MinReadyInstances** parameter is set to **5** and the **MinReadyInstanceRatio** parameter is set to **50**, the value of the **MinReadyInstanceRatio** parameter determines the minimum number of available instances.
        self.min_ready_instance_ratio = min_ready_instance_ratio
        # The minimum number of available instances. Valid values:
        # 
        # *   If you set the value to **0**, business interruptions occur when the application is updated.
        # *   If you set the value to **-1**, the minimum number of available instances is automatically set to a system-recommended value. The value is the nearest integer to which the calculated result of the following formula is rounded up: Current number of instances × 25%. For example, if five instances are available, the minimum number of available instances is calculated by using the following formula: 5 × 25% = 1.25. In this case, the minimum number of available instances is 2.
        # 
        # >  Make sure that at least one instance is available during application deployment and rollback to prevent business interruptions.
        self.min_ready_instances = min_ready_instances
        # The details of the mounted NAS file system.
        self.mount_desc = mount_desc
        # The mount target of the NAS file system in the VPC where the application is deployed. If you do not need to modify this configuration during the deployment, configure the **MountHost** parameter only in the first request. You do not need to include this parameter in subsequent requests. If you need to remove this configuration, leave the **MountHost** parameter empty in the request.
        self.mount_host = mount_host
        # The ID of the microservice application.
        self.mse_application_id = mse_application_id
        # The application name of SAE service registered in MSE.
        self.mse_application_name = mse_application_name
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The configurations for mounting the NAS file system.
        self.nas_configs = nas_configs
        # The ID of the NAS file system.
        self.nas_id = nas_id
        # The SAE application edition.
        # 
        # - lite: The lightweight edition.
        # - std: The standard edition.
        # - pro: The professional edition.
        self.new_sae_version = new_sae_version
        # The name of the RAM role used to authenticate the user identity.
        # 
        # >  You need to create an OpenID Connect (OIDC) identity provider (IdP) and an identity provider (IdP) for role-based single sign-on (SSO) in advance. For more information, see [Creates an OpenID Connect (OIDC) identity provider (IdP)](https://help.aliyun.com/document_detail/2331022.html) and [Creates an identity provider (IdP) for role-based single sign-on (SSO)](https://help.aliyun.com/document_detail/2331016.html).
        self.oidc_role_name = oidc_role_name
        # The AccessKey ID that is used to read data from and write data to Object Storage Service (OSS) buckets.
        self.oss_ak_id = oss_ak_id
        # The AccessKey secret that is used to read data from and write data to OSS buckets.
        self.oss_ak_secret = oss_ak_secret
        # The description of the mounted OSS bucket.
        self.oss_mount_descs = oss_mount_descs
        # The type of the deployment package. Valid values:
        # 
        # *   If you deploy the application by using a Java Archive (JAR) package, you can set this parameter to **FatJar**, **War**, or **Image**.
        # 
        # *   If you deploy the application by using a PHP package, you can set this parameter to one of the following values:
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
        # The URL of the deployment package. This parameter is returned only if the **PackageType** parameter is set to **FatJar** or **War**.
        self.package_url = package_url
        # The version of the deployment package. This parameter is returned only if the **PackageType** parameter is set to **FatJar** or **War**.
        self.package_version = package_version
        # The version of PHP supporting PHP deployment packages. Image is not supported.
        self.php = php
        # The path on which the PHP configuration file for application monitoring is mounted. Make sure that the PHP server loads the configuration file.
        # 
        # SAE automatically generates the corresponding configuration file. No manual operations are required.
        self.php_arms_config_location = php_arms_config_location
        # The details of the PHP configuration file.
        self.php_config = php_config
        # The path on which the PHP configuration file for application startup is mounted. Make sure that the PHP server uses this configuration file during the startup.
        self.php_config_location = php_config_location
        # The script that is run immediately after the container is started. Example: `{"exec":{"command":["cat","/etc/group"]}}`
        self.post_start = post_start
        # The script that is run before the container is stopped. Example: `{"exec":{"command":["cat","/etc/group"]}}`
        self.pre_stop = pre_stop
        # The programming language that is used to create the application. Valid values:
        # 
        # *   **java**: Java
        # *   **php**: PHP
        # *   **other**: Other programming languages, such as Python, C++, Go, .NET, and Node.js.
        self.programming_language = programming_language
        # Enable K8s Service discovery and registration.
        self.pvtz_discovery = pvtz_discovery
        # The Python environment. PYTHON 3.9.15 is supported.
        self.python = python
        # The configurations for installing custom module dependencies. By default, the dependencies defined by the requirements.txt file in the root directory are installed. If no software package is configured, you can specify dependencies based on your business requirements.
        self.python_modules = python_modules
        # The details of the health check that was performed on the container. If the container fails this health check multiple times, the system disables and restarts the container. Containers that fail health checks cannot receive traffic from Server Load Balancer (SLB) instances. You can use the **exec**, **httpGet**, or **tcpSocket** method to perform health checks. For more information, see the description of the **Liveness** parameter.
        # 
        # >  You can use only one method to perform the health check.
        self.readiness = readiness
        # The ID of the region.
        self.region_id = region_id
        # The number of application instances.
        self.replicas = replicas
        # The type of the resource. Set the value to `application`.
        self.resource_type = resource_type
        # Secret mount description.
        self.secret_mount_desc = secret_mount_desc
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The canary tag configured for the application.
        self.service_tags = service_tags
        # The configuration of the Sidecar container.
        self.sidecar_containers_config = sidecar_containers_config
        # The logging configurations of Log Service.
        # 
        # *   To use Log Service resources that are automatically created by SAE, set this parameter to `[{"logDir":"","logType":"stdout"},{"logDir":"/tmp/a.log"}]`.
        # *   To use custom Log Service resources, set this parameter to `[{"projectName":"test-sls","logType":"stdout","logDir":"","logstoreName":"sae","logtailName":""},{"projectName":"test","logDir":"/tmp/a.log","logstoreName":"sae","logtailName":""}]`.
        # 
        # The following parameters are involved:
        # 
        # *   **projectName**: the name of the Log Service project.
        # *   **logDir**: the path in which logs are stored.
        # *   **logType**: the log type. **stdout**: the standard output log of the container. You can specify only one stdout value for this parameter. If you leave this parameter empty, file logs are collected.
        # *   **logstoreName**: the name of the Logstore in Log Service.
        # *   **logtailName**: the name of the Logtail configuration in Log Service. If you do not configure this parameter, a new Logtail configuration is created.
        # 
        # If you do not need to modify the logging configurations when you deploy the application, configure the **SlsConfigs** parameter only in the first request. You do not need to include this parameter in subsequent requests. If you no longer need to use Log Service, leave the **SlsConfigs** parameter empty in the request.
        self.sls_configs = sls_configs
        self.sls_log_env_tags = sls_log_env_tags
        # Enable startup probe.
        self.startup_probe = startup_probe
        # Configuration of K8s Service discovery and registration, and full-chain gray-release feature.
        self.swimlane_pvtz_discovery = swimlane_pvtz_discovery
        # The details of the tags.
        self.tags = tags
        # The timeout period for a graceful shutdown. Default value: 30. Unit: seconds. Valid values: 1 to 300.
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # The time zone. Default value: **Asia/Shanghai**.
        self.timezone = timezone
        # The Tomcat configuration. If you want to delete the configuration, set this parameter to {} or leave this parameter empty. The following parameters are involved:
        # 
        # *   **port**: the port number. Valid values: 1024 to 65535. The root permissions are required to perform operations on ports whose number is smaller than 1024. Enter a value that ranges from 1025 to 65535 because the container has only the admin permissions. If you do not configure this parameter, the default port number 8080 is used.
        # *   **contextPath**: the path. Default value: /. This value indicates the root directory.
        # *   **maxThreads**: the maximum number of connections in the connection pool. Default value: 400.
        # *   **uriEncoding**: the URI encoding scheme in the Tomcat container. Valid values: **UTF-8**, **ISO-8859-1**, **GBK**, and **GB2312**. If you do not configure this parameter, the default value **ISO-8859-1** is used.
        # *   **useBodyEncoding**: indicates whether to use the encoding scheme that is specified by **BodyEncoding for URL**. Default value: **true**.
        self.tomcat_config = tomcat_config
        # The deployment policy. If the minimum number of available instances is 1, the value of the **UpdateStrategy** parameter is an empty string (""). If the minimum number of available instances is greater than 1, the following strategies can be configured:
        # 
        # *   The application is deployed on an instance. The remaining instances are automatically classified into two release batches whose interval is set to 1. In this case, the parameter is set to `{"type":"GrayBatchUpdate","batchUpdate":{"batch":2,"releaseType":"auto","batchWaitTime":1},"grayUpdate":{"gray":1}}`.
        # *   The application is deployed on an instance. The remaining instances are manually classified into two release batches. In this case, the parameter is set to `{"type":"GrayBatchUpdate","batchUpdate":{"batch":2,"releaseType":"manual"},"grayUpdate":{"gray":1}}`.
        # *   All instances are automatically classified into two release batches. The application is deployed on the instances of the two batches in parallel. In this case, the parameter is set to `{"type":"BatchUpdate","batchUpdate":{"batch":2,"releaseType":"auto","batchWaitTime":0}}`
        # 
        # The following parameters are involved:
        # 
        # *   **type**: the type of the release policy. Valid values: **GrayBatchUpdate** and **BatchUpdate**.
        # 
        # *   **batchUpdate**: the phased release policy.
        # 
        #     *   **batch**: the number of release batches.
        #     *   **releaseType**: the processing method for the batches. Valid values: **auto** and **manual**.
        #     *   **batchWaitTime**: the interval between release batches. Unit: seconds.
        # 
        # *   **grayUpdate**: the number of release batches in the phased release after a canary release. This parameter is returned only if the **type** parameter is set to **GrayBatchUpdate**.
        self.update_strategy = update_strategy
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC).
        self.vpc_id = vpc_id
        # The option settings in the WAR package. The settings are used to start the application container. The default startup command is `java $JAVA_OPTS $CATALINA_OPTS -Options org.apache.catalina.startup.Bootstrap "$@" start`.
        self.war_start_options = war_start_options
        # The version of the Tomcat container on which the deployment package depends. Valid values:
        # 
        # *   **apache-tomcat-7.0.91**
        # *   **apache-tomcat-8.5.42**
        # 
        # This parameter is not returned if the **PackageType** parameter is set to **Image**.
        self.web_container = web_container

    def validate(self):
        if self.config_map_mount_desc:
            for v1 in self.config_map_mount_desc:
                 if v1:
                    v1.validate()
        if self.empty_dir_desc:
            for v1 in self.empty_dir_desc:
                 if v1:
                    v1.validate()
        if self.init_containers_config:
            for v1 in self.init_containers_config:
                 if v1:
                    v1.validate()
        if self.mount_desc:
            for v1 in self.mount_desc:
                 if v1:
                    v1.validate()
        if self.oss_mount_descs:
            for v1 in self.oss_mount_descs:
                 if v1:
                    v1.validate()
        if self.secret_mount_desc:
            for v1 in self.secret_mount_desc:
                 if v1:
                    v1.validate()
        if self.sidecar_containers_config:
            for v1 in self.sidecar_containers_config:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn

        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.alb_ingress_readiness_gate is not None:
            result['AlbIngressReadinessGate'] = self.alb_ingress_readiness_gate

        if self.app_description is not None:
            result['AppDescription'] = self.app_description

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_source is not None:
            result['AppSource'] = self.app_source

        if self.associate_eip is not None:
            result['AssociateEip'] = self.associate_eip

        if self.base_app_id is not None:
            result['BaseAppId'] = self.base_app_id

        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cms_service_id is not None:
            result['CmsServiceId'] = self.cms_service_id

        if self.command is not None:
            result['Command'] = self.command

        if self.command_args is not None:
            result['CommandArgs'] = self.command_args

        result['ConfigMapMountDesc'] = []
        if self.config_map_mount_desc is not None:
            for k1 in self.config_map_mount_desc:
                result['ConfigMapMountDesc'].append(k1.to_map() if k1 else None)

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias

        if self.custom_image_network_type is not None:
            result['CustomImageNetworkType'] = self.custom_image_network_type

        if self.deployment_name is not None:
            result['DeploymentName'] = self.deployment_name

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.dotnet is not None:
            result['Dotnet'] = self.dotnet

        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version

        result['EmptyDirDesc'] = []
        if self.empty_dir_desc is not None:
            for k1 in self.empty_dir_desc:
                result['EmptyDirDesc'].append(k1.to_map() if k1 else None)

        if self.enable_ahas is not None:
            result['EnableAhas'] = self.enable_ahas

        if self.enable_cpu_burst is not None:
            result['EnableCpuBurst'] = self.enable_cpu_burst

        if self.enable_grey_tag_route is not None:
            result['EnableGreyTagRoute'] = self.enable_grey_tag_route

        if self.enable_idle is not None:
            result['EnableIdle'] = self.enable_idle

        if self.enable_namespace_agent_version is not None:
            result['EnableNamespaceAgentVersion'] = self.enable_namespace_agent_version

        if self.enable_new_arms is not None:
            result['EnableNewArms'] = self.enable_new_arms

        if self.enable_prometheus is not None:
            result['EnablePrometheus'] = self.enable_prometheus

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count

        if self.gpu_type is not None:
            result['GpuType'] = self.gpu_type

        if self.headless_pvtz_discovery is not None:
            result['HeadlessPvtzDiscovery'] = self.headless_pvtz_discovery

        if self.html is not None:
            result['Html'] = self.html

        if self.idle_hour is not None:
            result['IdleHour'] = self.idle_hour

        if self.image_pull_secrets is not None:
            result['ImagePullSecrets'] = self.image_pull_secrets

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        result['InitContainersConfig'] = []
        if self.init_containers_config is not None:
            for k1 in self.init_containers_config:
                result['InitContainersConfig'].append(k1.to_map() if k1 else None)

        if self.is_stateful is not None:
            result['IsStateful'] = self.is_stateful

        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args

        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options

        if self.jdk is not None:
            result['Jdk'] = self.jdk

        if self.kafka_configs is not None:
            result['KafkaConfigs'] = self.kafka_configs

        if self.liveness is not None:
            result['Liveness'] = self.liveness

        if self.loki_configs is not None:
            result['LokiConfigs'] = self.loki_configs

        if self.max_surge_instance_ratio is not None:
            result['MaxSurgeInstanceRatio'] = self.max_surge_instance_ratio

        if self.max_surge_instances is not None:
            result['MaxSurgeInstances'] = self.max_surge_instances

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.micro_registration is not None:
            result['MicroRegistration'] = self.micro_registration

        if self.micro_registration_config is not None:
            result['MicroRegistrationConfig'] = self.micro_registration_config

        if self.microservice_engine_config is not None:
            result['MicroserviceEngineConfig'] = self.microservice_engine_config

        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio

        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances

        result['MountDesc'] = []
        if self.mount_desc is not None:
            for k1 in self.mount_desc:
                result['MountDesc'].append(k1.to_map() if k1 else None)

        if self.mount_host is not None:
            result['MountHost'] = self.mount_host

        if self.mse_application_id is not None:
            result['MseApplicationId'] = self.mse_application_id

        if self.mse_application_name is not None:
            result['MseApplicationName'] = self.mse_application_name

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.nas_configs is not None:
            result['NasConfigs'] = self.nas_configs

        if self.nas_id is not None:
            result['NasId'] = self.nas_id

        if self.new_sae_version is not None:
            result['NewSaeVersion'] = self.new_sae_version

        if self.oidc_role_name is not None:
            result['OidcRoleName'] = self.oidc_role_name

        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id

        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret

        result['OssMountDescs'] = []
        if self.oss_mount_descs is not None:
            for k1 in self.oss_mount_descs:
                result['OssMountDescs'].append(k1.to_map() if k1 else None)

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.package_url is not None:
            result['PackageUrl'] = self.package_url

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.php is not None:
            result['Php'] = self.php

        if self.php_arms_config_location is not None:
            result['PhpArmsConfigLocation'] = self.php_arms_config_location

        if self.php_config is not None:
            result['PhpConfig'] = self.php_config

        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location

        if self.post_start is not None:
            result['PostStart'] = self.post_start

        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop

        if self.programming_language is not None:
            result['ProgrammingLanguage'] = self.programming_language

        if self.pvtz_discovery is not None:
            result['PvtzDiscovery'] = self.pvtz_discovery

        if self.python is not None:
            result['Python'] = self.python

        if self.python_modules is not None:
            result['PythonModules'] = self.python_modules

        if self.readiness is not None:
            result['Readiness'] = self.readiness

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['SecretMountDesc'] = []
        if self.secret_mount_desc is not None:
            for k1 in self.secret_mount_desc:
                result['SecretMountDesc'].append(k1.to_map() if k1 else None)

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.service_tags is not None:
            result['ServiceTags'] = self.service_tags

        result['SidecarContainersConfig'] = []
        if self.sidecar_containers_config is not None:
            for k1 in self.sidecar_containers_config:
                result['SidecarContainersConfig'].append(k1.to_map() if k1 else None)

        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs

        if self.sls_log_env_tags is not None:
            result['SlsLogEnvTags'] = self.sls_log_env_tags

        if self.startup_probe is not None:
            result['StartupProbe'] = self.startup_probe

        if self.swimlane_pvtz_discovery is not None:
            result['SwimlanePvtzDiscovery'] = self.swimlane_pvtz_discovery

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config

        if self.update_strategy is not None:
            result['UpdateStrategy'] = self.update_strategy

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options

        if self.web_container is not None:
            result['WebContainer'] = self.web_container

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')

        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('AlbIngressReadinessGate') is not None:
            self.alb_ingress_readiness_gate = m.get('AlbIngressReadinessGate')

        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppSource') is not None:
            self.app_source = m.get('AppSource')

        if m.get('AssociateEip') is not None:
            self.associate_eip = m.get('AssociateEip')

        if m.get('BaseAppId') is not None:
            self.base_app_id = m.get('BaseAppId')

        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CmsServiceId') is not None:
            self.cms_service_id = m.get('CmsServiceId')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')

        self.config_map_mount_desc = []
        if m.get('ConfigMapMountDesc') is not None:
            for k1 in m.get('ConfigMapMountDesc'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataConfigMapMountDesc()
                self.config_map_mount_desc.append(temp_model.from_map(k1))

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')

        if m.get('CustomImageNetworkType') is not None:
            self.custom_image_network_type = m.get('CustomImageNetworkType')

        if m.get('DeploymentName') is not None:
            self.deployment_name = m.get('DeploymentName')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('Dotnet') is not None:
            self.dotnet = m.get('Dotnet')

        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')

        self.empty_dir_desc = []
        if m.get('EmptyDirDesc') is not None:
            for k1 in m.get('EmptyDirDesc'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataEmptyDirDesc()
                self.empty_dir_desc.append(temp_model.from_map(k1))

        if m.get('EnableAhas') is not None:
            self.enable_ahas = m.get('EnableAhas')

        if m.get('EnableCpuBurst') is not None:
            self.enable_cpu_burst = m.get('EnableCpuBurst')

        if m.get('EnableGreyTagRoute') is not None:
            self.enable_grey_tag_route = m.get('EnableGreyTagRoute')

        if m.get('EnableIdle') is not None:
            self.enable_idle = m.get('EnableIdle')

        if m.get('EnableNamespaceAgentVersion') is not None:
            self.enable_namespace_agent_version = m.get('EnableNamespaceAgentVersion')

        if m.get('EnableNewArms') is not None:
            self.enable_new_arms = m.get('EnableNewArms')

        if m.get('EnablePrometheus') is not None:
            self.enable_prometheus = m.get('EnablePrometheus')

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')

        if m.get('GpuType') is not None:
            self.gpu_type = m.get('GpuType')

        if m.get('HeadlessPvtzDiscovery') is not None:
            self.headless_pvtz_discovery = m.get('HeadlessPvtzDiscovery')

        if m.get('Html') is not None:
            self.html = m.get('Html')

        if m.get('IdleHour') is not None:
            self.idle_hour = m.get('IdleHour')

        if m.get('ImagePullSecrets') is not None:
            self.image_pull_secrets = m.get('ImagePullSecrets')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        self.init_containers_config = []
        if m.get('InitContainersConfig') is not None:
            for k1 in m.get('InitContainersConfig'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataInitContainersConfig()
                self.init_containers_config.append(temp_model.from_map(k1))

        if m.get('IsStateful') is not None:
            self.is_stateful = m.get('IsStateful')

        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')

        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')

        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')

        if m.get('KafkaConfigs') is not None:
            self.kafka_configs = m.get('KafkaConfigs')

        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')

        if m.get('LokiConfigs') is not None:
            self.loki_configs = m.get('LokiConfigs')

        if m.get('MaxSurgeInstanceRatio') is not None:
            self.max_surge_instance_ratio = m.get('MaxSurgeInstanceRatio')

        if m.get('MaxSurgeInstances') is not None:
            self.max_surge_instances = m.get('MaxSurgeInstances')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MicroRegistration') is not None:
            self.micro_registration = m.get('MicroRegistration')

        if m.get('MicroRegistrationConfig') is not None:
            self.micro_registration_config = m.get('MicroRegistrationConfig')

        if m.get('MicroserviceEngineConfig') is not None:
            self.microservice_engine_config = m.get('MicroserviceEngineConfig')

        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')

        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')

        self.mount_desc = []
        if m.get('MountDesc') is not None:
            for k1 in m.get('MountDesc'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataMountDesc()
                self.mount_desc.append(temp_model.from_map(k1))

        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')

        if m.get('MseApplicationId') is not None:
            self.mse_application_id = m.get('MseApplicationId')

        if m.get('MseApplicationName') is not None:
            self.mse_application_name = m.get('MseApplicationName')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('NasConfigs') is not None:
            self.nas_configs = m.get('NasConfigs')

        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')

        if m.get('NewSaeVersion') is not None:
            self.new_sae_version = m.get('NewSaeVersion')

        if m.get('OidcRoleName') is not None:
            self.oidc_role_name = m.get('OidcRoleName')

        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')

        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')

        self.oss_mount_descs = []
        if m.get('OssMountDescs') is not None:
            for k1 in m.get('OssMountDescs'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataOssMountDescs()
                self.oss_mount_descs.append(temp_model.from_map(k1))

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('Php') is not None:
            self.php = m.get('Php')

        if m.get('PhpArmsConfigLocation') is not None:
            self.php_arms_config_location = m.get('PhpArmsConfigLocation')

        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')

        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')

        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')

        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')

        if m.get('ProgrammingLanguage') is not None:
            self.programming_language = m.get('ProgrammingLanguage')

        if m.get('PvtzDiscovery') is not None:
            self.pvtz_discovery = m.get('PvtzDiscovery')

        if m.get('Python') is not None:
            self.python = m.get('Python')

        if m.get('PythonModules') is not None:
            self.python_modules = m.get('PythonModules')

        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.secret_mount_desc = []
        if m.get('SecretMountDesc') is not None:
            for k1 in m.get('SecretMountDesc'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataSecretMountDesc()
                self.secret_mount_desc.append(temp_model.from_map(k1))

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('ServiceTags') is not None:
            self.service_tags = m.get('ServiceTags')

        self.sidecar_containers_config = []
        if m.get('SidecarContainersConfig') is not None:
            for k1 in m.get('SidecarContainersConfig'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataSidecarContainersConfig()
                self.sidecar_containers_config.append(temp_model.from_map(k1))

        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')

        if m.get('SlsLogEnvTags') is not None:
            self.sls_log_env_tags = m.get('SlsLogEnvTags')

        if m.get('StartupProbe') is not None:
            self.startup_probe = m.get('StartupProbe')

        if m.get('SwimlanePvtzDiscovery') is not None:
            self.swimlane_pvtz_discovery = m.get('SwimlanePvtzDiscovery')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')

        if m.get('UpdateStrategy') is not None:
            self.update_strategy = m.get('UpdateStrategy')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')

        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')

        return self

class DescribeApplicationConfigResponseBodyDataTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeApplicationConfigResponseBodyDataSidecarContainersConfig(DaraModel):
    def __init__(
        self,
        acr_instance_id: str = None,
        command: str = None,
        command_args: str = None,
        config_map_mount_desc: List[main_models.DescribeApplicationConfigResponseBodyDataSidecarContainersConfigConfigMapMountDesc] = None,
        cpu: int = None,
        empty_dir_desc: List[main_models.DescribeApplicationConfigResponseBodyDataSidecarContainersConfigEmptyDirDesc] = None,
        envs: str = None,
        image_url: str = None,
        memory: int = None,
        name: str = None,
    ):
        # The ID of Container Registry Enterprise Edition instance. This parameter is required when the **ImageUrl** parameter is set to the URL of an image in an ACR Enterprise Edition instance.
        self.acr_instance_id = acr_instance_id
        # The command that is used to start the image. The command must be an existing executable object in the container. Sample statements:
        # 
        #     command:
        #           - echo
        #           - abc
        #           - >
        #           - file0
        # 
        # In this example, the Command parameter is set to `Command="echo", CommandArgs=["abc", ">", "file0"]`.
        self.command = command
        # The parameters of the image startup command. The CommandArgs parameter specifies the parameters that are required for the **Command** parameter. You can specify the name in one of the following formats:
        # 
        # `["a","b"]`
        # 
        # In the preceding example, the CommandArgs parameter is set to `CommandArgs=["abc", ">", "file0"]`. The data type of `["abc", ">", "file0"]` must be an array of strings in the JSON format. This parameter is optional.
        self.command_args = command_args
        # The description of the **ConfigMap** instance mounted to the application. Use configurations created on the Configuration Items page to configure containers. The following table describes the parameters that are used in the preceding statements.
        # 
        # *   **congfigMapId**: the ID of the ConfigMap instance. You can call the [ListNamespacedConfigMaps](https://help.aliyun.com/document_detail/176917.html) operation to obtain the ID.
        # *   **key**: the key.
        # 
        # > You can use the `sae-sys-configmap-all` key to mount all keys.
        # 
        # *   **mountPath**: the mount path in the container.
        self.config_map_mount_desc = config_map_mount_desc
        # Set the CPU resource limit of the primary container that can be used by Sidecar container.
        self.cpu = cpu
        # Shared temporary storage mounted to the primary container and the Sidecar container.
        self.empty_dir_desc = empty_dir_desc
        # The environment variables. You can configure custom environment variables or reference a ConfigMap. If you want to reference a ConfigMap, you must first create a ConfigMap. For more information, see [CreateConfigMap](https://help.aliyun.com/document_detail/176914.html). Take note of the following rules:
        # 
        # *   Customize
        # 
        #     *   **name**: the name of the environment variable.
        #     *   **value**: the value of the environment variable.
        # 
        # *   Reference ConfigMap
        # 
        #     *   **name**: the name of the environment variable. You can reference one or all keys. If you want to reference all keys, specify `sae-sys-configmap-all-<ConfigMap name>`. Example: `sae-sys-configmap-all-test1`.
        #     *   **valueFrom**: the reference of the environment variable. Set the value to `configMapRef`.
        #     *   **configMapId**: the ConfigMap ID.
        #     *   **key**: the key. If you want to reference all keys, do not configure this parameter.
        self.envs = envs
        # The URL of the image.
        self.image_url = image_url
        # Set the memory limit of the primary container that can be used by Sidecar container.
        self.memory = memory
        # The container name.
        self.name = name

    def validate(self):
        if self.config_map_mount_desc:
            for v1 in self.config_map_mount_desc:
                 if v1:
                    v1.validate()
        if self.empty_dir_desc:
            for v1 in self.empty_dir_desc:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id

        if self.command is not None:
            result['Command'] = self.command

        if self.command_args is not None:
            result['CommandArgs'] = self.command_args

        result['ConfigMapMountDesc'] = []
        if self.config_map_mount_desc is not None:
            for k1 in self.config_map_mount_desc:
                result['ConfigMapMountDesc'].append(k1.to_map() if k1 else None)

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        result['EmptyDirDesc'] = []
        if self.empty_dir_desc is not None:
            for k1 in self.empty_dir_desc:
                result['EmptyDirDesc'].append(k1.to_map() if k1 else None)

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')

        self.config_map_mount_desc = []
        if m.get('ConfigMapMountDesc') is not None:
            for k1 in m.get('ConfigMapMountDesc'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataSidecarContainersConfigConfigMapMountDesc()
                self.config_map_mount_desc.append(temp_model.from_map(k1))

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        self.empty_dir_desc = []
        if m.get('EmptyDirDesc') is not None:
            for k1 in m.get('EmptyDirDesc'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataSidecarContainersConfigEmptyDirDesc()
                self.empty_dir_desc.append(temp_model.from_map(k1))

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationConfigResponseBodyDataSidecarContainersConfigEmptyDirDesc(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        name: str = None,
    ):
        # Mount path of the data volume within the container.
        self.mount_path = mount_path
        # The name of the shared temporary storage.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationConfigResponseBodyDataSidecarContainersConfigConfigMapMountDesc(DaraModel):
    def __init__(
        self,
        config_map_id: int = None,
        config_map_name: str = None,
        key: str = None,
        mount_path: str = None,
    ):
        # The ConfigMap ID.
        self.config_map_id = config_map_id
        # The ConfigMap name.
        self.config_map_name = config_map_name
        # The ConfigMap key
        self.key = key
        # The mount path.
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id

        if self.config_map_name is not None:
            result['ConfigMapName'] = self.config_map_name

        if self.key is not None:
            result['Key'] = self.key

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')

        if m.get('ConfigMapName') is not None:
            self.config_map_name = m.get('ConfigMapName')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        return self

class DescribeApplicationConfigResponseBodyDataSecretMountDesc(DaraModel):
    def __init__(
        self,
        key: str = None,
        mount_path: str = None,
        secret_id: int = None,
        secret_name: str = None,
    ):
        # The key to Base64 encode values.
        self.key = key
        # The mount path.
        self.mount_path = mount_path
        # The secret ID of the instance.
        self.secret_id = secret_id
        # The name of the secret.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        return self

class DescribeApplicationConfigResponseBodyDataOssMountDescs(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_path: str = None,
        mount_path: str = None,
        read_only: bool = None,
    ):
        # The name of the OSS bucket.
        self.bucket_name = bucket_name
        # The directory or object in OSS. If the specified directory or object does not exist, an error is returned.
        self.bucket_path = bucket_path
        # The path of the container in SAE. The parameter value that you specified overwrites the original value. If the specified path does not exist, SAE automatically creates the path.
        self.mount_path = mount_path
        # Indicates whether the application can use the container path to read data from or write data to resources in the directory of the OSS bucket. Valid values:
        # 
        # *   **true**: The application has the read-only permissions.
        # *   **false**: The application has the read and write permissions.
        self.read_only = read_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.bucket_path is not None:
            result['bucketPath'] = self.bucket_path

        if self.mount_path is not None:
            result['mountPath'] = self.mount_path

        if self.read_only is not None:
            result['readOnly'] = self.read_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('bucketPath') is not None:
            self.bucket_path = m.get('bucketPath')

        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')

        if m.get('readOnly') is not None:
            self.read_only = m.get('readOnly')

        return self

class DescribeApplicationConfigResponseBodyDataMountDesc(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        nas_path: str = None,
    ):
        # The path on which the NAS file system is mounted.
        self.mount_path = mount_path
        # The directory in the NAS file system.
        self.nas_path = nas_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.nas_path is not None:
            result['NasPath'] = self.nas_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('NasPath') is not None:
            self.nas_path = m.get('NasPath')

        return self

class DescribeApplicationConfigResponseBodyDataInitContainersConfig(DaraModel):
    def __init__(
        self,
        command: str = None,
        command_args: str = None,
        config_map_mount_desc: List[main_models.DescribeApplicationConfigResponseBodyDataInitContainersConfigConfigMapMountDesc] = None,
        empty_dir_desc: List[main_models.DescribeApplicationConfigResponseBodyDataInitContainersConfigEmptyDirDesc] = None,
        envs: str = None,
        image_url: str = None,
        name: str = None,
    ):
        # The command that is used to start the image. The command must be an existing executable object in the container. Sample statements:
        # 
        #     command:
        #           - echo
        #           - abc
        #           - >
        #           - file0
        # 
        # In this example, the Command parameter is set to `Command="echo", CommandArgs=["abc", ">", "file0"]`.
        self.command = command
        # The parameters of the image startup command. The CommandArgs parameter specifies the parameters that are required for the **Command** parameter. You can specify the name in one of the following formats:
        # 
        # `["a","b"]`
        # 
        # In the preceding example, the CommandArgs parameter is set to `CommandArgs=["abc", ">", "file0"]`. The data type of `["abc", ">", "file0"]` must be an array of strings in the JSON format. This parameter is optional.
        self.command_args = command_args
        # The information of ConfigMap.
        self.config_map_mount_desc = config_map_mount_desc
        self.empty_dir_desc = empty_dir_desc
        # The environment variables. You can configure custom environment variables or reference a ConfigMap. If you want to reference a ConfigMap, you must first create a ConfigMap. For more information, see [CreateConfigMap](https://help.aliyun.com/document_detail/176914.html). Take note of the following rules:
        # 
        # *   Customize
        # 
        #     *   **name**: the name of the environment variable.
        #     *   **value**: the value of the environment variable.
        # 
        # *   Reference ConfigMap
        # 
        #     *   **name**: the name of the environment variable. You can reference one or all keys. If you want to reference all keys, specify `sae-sys-configmap-all-<ConfigMap name>`. Example: `sae-sys-configmap-all-test1`.
        #     *   **valueFrom**: the reference of the environment variable. Set the value to `configMapRef`.
        #     *   **configMapId**: the ConfigMap ID.
        #     *   **key**: the key. If you want to reference all keys, do not configure this parameter.
        self.envs = envs
        # The image URL of the initialized container.
        self.image_url = image_url
        # The name of the initialized container.
        self.name = name

    def validate(self):
        if self.config_map_mount_desc:
            for v1 in self.config_map_mount_desc:
                 if v1:
                    v1.validate()
        if self.empty_dir_desc:
            for v1 in self.empty_dir_desc:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        if self.command_args is not None:
            result['CommandArgs'] = self.command_args

        result['ConfigMapMountDesc'] = []
        if self.config_map_mount_desc is not None:
            for k1 in self.config_map_mount_desc:
                result['ConfigMapMountDesc'].append(k1.to_map() if k1 else None)

        result['EmptyDirDesc'] = []
        if self.empty_dir_desc is not None:
            for k1 in self.empty_dir_desc:
                result['EmptyDirDesc'].append(k1.to_map() if k1 else None)

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')

        self.config_map_mount_desc = []
        if m.get('ConfigMapMountDesc') is not None:
            for k1 in m.get('ConfigMapMountDesc'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataInitContainersConfigConfigMapMountDesc()
                self.config_map_mount_desc.append(temp_model.from_map(k1))

        self.empty_dir_desc = []
        if m.get('EmptyDirDesc') is not None:
            for k1 in m.get('EmptyDirDesc'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataInitContainersConfigEmptyDirDesc()
                self.empty_dir_desc.append(temp_model.from_map(k1))

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationConfigResponseBodyDataInitContainersConfigEmptyDirDesc(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        name: str = None,
    ):
        self.mount_path = mount_path
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationConfigResponseBodyDataInitContainersConfigConfigMapMountDesc(DaraModel):
    def __init__(
        self,
        config_map_id: int = None,
        config_map_name: str = None,
        key: str = None,
        mount_path: str = None,
    ):
        # ConfigMap ID。
        self.config_map_id = config_map_id
        # The name of the ConfigMap.
        self.config_map_name = config_map_name
        # The key.
        self.key = key
        # The mount path.
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id

        if self.config_map_name is not None:
            result['ConfigMapName'] = self.config_map_name

        if self.key is not None:
            result['Key'] = self.key

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')

        if m.get('ConfigMapName') is not None:
            self.config_map_name = m.get('ConfigMapName')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        return self

class DescribeApplicationConfigResponseBodyDataEmptyDirDesc(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        name: str = None,
    ):
        self.mount_path = mount_path
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeApplicationConfigResponseBodyDataConfigMapMountDesc(DaraModel):
    def __init__(
        self,
        config_map_id: int = None,
        config_map_name: str = None,
        key: str = None,
        mount_path: str = None,
    ):
        # The ID of the ConfigMap.
        self.config_map_id = config_map_id
        # The name of the ConfigMap.
        self.config_map_name = config_map_name
        # The key-value pair that is stored in the ConfigMap.
        self.key = key
        # The path on which the ConfigMap is mounted.
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_map_id is not None:
            result['ConfigMapId'] = self.config_map_id

        if self.config_map_name is not None:
            result['ConfigMapName'] = self.config_map_name

        if self.key is not None:
            result['Key'] = self.key

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigMapId') is not None:
            self.config_map_id = m.get('ConfigMapId')

        if m.get('ConfigMapName') is not None:
            self.config_map_name = m.get('ConfigMapName')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        return self

