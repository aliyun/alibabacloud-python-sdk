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
        # The API status or POP error code. Valid values:
        # 
        # - **2xx**: success.
        # - **3xx**: redirection.
        # - **4xx**: request error.
        # - **5xx**: server error.
        self.code = code
        # The application information.
        self.data = data
        # The error code. Valid values:
        # 
        # - If the request is successful, the **ErrorCode** field is not returned.
        # - If the request fails, the **ErrorCode** field is returned. For more information, see the **Error codes** section in this topic.
        self.error_code = error_code
        # The additional information about the call result.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the application configuration information is retrieved. Valid values:
        # 
        # - **true**: Retrieved.
        # - **false**: Failed to retrieve.
        self.success = success
        # The trace ID, which is used to query the details of a call.
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
        labels: Dict[str, str] = None,
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
        rasp_config: List[main_models.DescribeApplicationConfigResponseBodyDataRaspConfig] = None,
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
        # The ARN of the RAM role required for pulling images across accounts. For more information, see [Pull Alibaba Cloud images across accounts](https://help.aliyun.com/document_detail/190675.html) and [Grant cross-account permissions by using RAM roles](https://help.aliyun.com/document_detail/223585.html).
        self.acr_assume_role_arn = acr_assume_role_arn
        # The ACR Enterprise instance ID.
        self.acr_instance_id = acr_instance_id
        # The agent version.
        self.agent_version = agent_version
        # The ALB gateway ReadinessGate configuration.
        self.alb_ingress_readiness_gate = alb_ingress_readiness_gate
        # The application description.
        self.app_description = app_description
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The SAE application type.
        # 
        # - micro_service
        # 
        # - web
        # 
        # - job
        self.app_source = app_source
        # Specifies whether to associate an EIP. Valid values:
        # 
        # - **true**: Associated.
        # - **false**: Not associated.
        self.associate_eip = associate_eip
        # The ID of the baseline application.
        self.base_app_id = base_app_id
        # The wait time between batches during a phased release, in seconds.
        self.batch_wait_time = batch_wait_time
        # The cluster ID.
        self.cluster_id = cluster_id
        # The CloudMonitor service ID.
        self.cms_service_id = cms_service_id
        # The image startup command. This command must be an executable object that exists in the container. Example:
        # 
        # ```
        # command:
        #       - echo
        #       - abc
        #       - >
        #       - file0
        # ```
        # Based on the preceding example, `Command="echo", CommandArgs=["abc", ">", "file0"]`.
        self.command = command
        # The arguments for the image startup command. These are the arguments required by the startup command **Command**. Format:
        # 
        # `["a","b"]`
        # 
        # In the example for the **Command** parameter, `CommandArgs=["abc", ">", "file0"]`, where `["abc", ">", "file0"]` must be converted to the String type and the internal format is a JSON array. If this parameter is not required, leave it empty.
        self.command_args = command_args
        # The ConfigMap information.
        self.config_map_mount_desc = config_map_mount_desc
        # The CPU required by each instance, in millicores. This value cannot be 0. Only the following defined specifications are supported:
        # 
        # - **500**
        # - **1000**
        # - **2000**
        # - **4000**
        # - **8000**
        # - **16000**
        # - **32000**
        self.cpu = cpu
        # The custom host mapping in the container. Valid values:
        # 
        # - **hostName**: The domain name or hostname.
        # - **ip**: The IP address.
        self.custom_host_alias = custom_host_alias
        # The type of the custom image. If the image is not a custom image, set this parameter to an empty string. Valid values:
        # 
        # - internet: public image
        # - intranet: internal image
        self.custom_image_network_type = custom_image_network_type
        # The instance name of the application in the ASI cluster.
        self.deployment_name = deployment_name
        # The disk storage size, in GB.
        self.disk_size = disk_size
        # The .NET framework version:
        # 
        # - .NET 3.1
        # - .NET 5.0
        # - .NET 6.0
        # - .NET 7.0
        # - .NET 8.0
        self.dotnet = dotnet
        # The version of the application runtime environment in the HSF framework, such as the Ali-Tomcat container.
        self.edas_container_version = edas_container_version
        # The shared temporary storage.
        self.empty_dir_desc = empty_dir_desc
        # Specifies whether to connect to Application High Availability Service (AHAS). Valid values:
        # 
        # - **true**: Connected to AHAS.
        # - **false**: Not connected to AHAS.
        self.enable_ahas = enable_ahas
        # Specifies whether to enable the CPU Burst feature. Valid values:
        # 
        # - true: Enabled.
        # - false: Not enabled.
        self.enable_cpu_burst = enable_cpu_burst
        # Specifies whether to enable the traffic canary release rule. This rule applies only to applications that use the Spring Cloud and Dubbo frameworks. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.enable_grey_tag_route = enable_grey_tag_route
        # Specifies whether to enable idle mode. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        self.enable_idle = enable_idle
        # Indicates whether the namespace agent version configuration is reused.
        self.enable_namespace_agent_version = enable_namespace_agent_version
        # Specifies whether to enable the new ARMS feature. Valid values:
        # 
        # - true: Enabled.
        # - false: Not enabled.
        self.enable_new_arms = enable_new_arms
        # Indicates whether Prometheus custom metric collection is enabled.
        self.enable_prometheus = enable_prometheus
        # The container environment variable parameters. Custom values or references to configuration items are supported. To reference a configuration item, create a ConfigMap instance first. For more information, see [CreateConfigMap](https://help.aliyun.com/document_detail/176914.html). Valid values:
        # - Custom configuration
        #     - **name**: The environment variable name.
        #     - **value**: The environment variable value.
        # - Reference to a configuration item
        #     - **name**: The environment variable name. You can reference a single key or all keys. To reference all keys, enter `sae-sys-configmap-all-<ConfigMap name>`, such as `sae-sys-configmap-all-test1`.
        #     - **valueFrom**: The environment variable reference. Set the value to `configMapRef`.
        #     - **configMapId**: The ConfigMap ID.
        #     - **key**: The key. If all keys are referenced, do not set this field.
        self.envs = envs
        # The number of GPUs.
        self.gpu_count = gpu_count
        # The GPU type.
        self.gpu_type = gpu_type
        self.headless_pvtz_discovery = headless_pvtz_discovery
        self.html = html
        self.idle_hour = idle_hour
        # The corresponding secret ID.
        self.image_pull_secrets = image_pull_secrets
        # The image URL. This parameter is required when **Package Type** is set to **Image**.
        self.image_url = image_url
        # The init container configuration.
        self.init_containers_config = init_containers_config
        # Indicates whether the application is stateful.
        self.is_stateful = is_stateful
        # The arguments for starting the JAR package application. The default startup command for the application: `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`
        self.jar_start_args = jar_start_args
        # The options for starting the JAR package application. The default startup command for the application: `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`
        self.jar_start_options = jar_start_options
        # The JDK version on which the deployment package depends. Valid values:
        # 
        # - **Open JDK 8**
        # - **Open JDK 7**
        # - **Dragonwell 11**
        # - **Dragonwell 8**
        # - **openjdk-8u191-jdk-alpine3.9**
        # - **openjdk-7u201-jdk-alpine3.9**
        # 
        # This parameter is not supported when **Package Type** is set to **Image**.
        self.jdk = jdk
        # The summary of log collection configurations for Kafka. Valid values:
        # 
        # - **kafkaEndpoint**: The endpoint of the Kafka API.
        # - **kafkaInstanceId**: The Kafka instance ID.
        # - **kafkaConfigs**: The configuration summary for one or more log entries. For example values and parameter descriptions, see the **kafkaConfigs** request parameter in this topic.
        self.kafka_configs = kafka_configs
        # The labels.
        self.labels = labels
        # The container health check settings. Containers that fail the health check are shut down and recovered. The following methods are supported:
        # 
        # - **exec**: For example, `{"exec":{"command":["sh","-c","cat/home/admin/start.sh"]},"initialDelaySeconds":30,"periodSeconds":30,"timeoutSeconds":2}`
        # - **httpGet**: For example, `{"httpGet":{"path":"/","port":18091,"scheme":"HTTP","isContainKeyWord":true,"keyWord":"SAE"},"initialDelaySeconds":11,"periodSeconds":10,"timeoutSeconds":1}`
        # - **tcpSocket**: For example, `{"tcpSocket":{"port":18091},"initialDelaySeconds":11,"periodSeconds":10,"timeoutSeconds":1}`
        # 
        # > You can select only one method for health checks.
        # 
        # Parameter descriptions:
        # 
        # - **exec.command**: The health check command.
        # - **httpGet.path**: The access path.
        # - **httpGet.scheme**: **HTTP** or **HTTPS**.
        # - **httpGet.isContainKeyWord**: **true** indicates that the keyword is included. **false** indicates that the keyword is not included. If this field is missing, the advanced feature is not used.
        # - **httpGet.keyWord**: The custom keyword. The **isContainKeyWord** field must be present when this parameter is used.
        # - **tcpSocket.port**: The port for TCP connection detection.
        # - **initialDelaySeconds**: The initial delay for the health check. Default value: 10. Unit: seconds.
        # - **periodSeconds**: The health check period. Default value: 30. Unit: seconds.
        # - **timeoutSeconds**: The health check timeout period. Default value: 1. Unit: seconds. If this parameter is set to 0 or is not set, the default timeout period is 1 second.
        self.liveness = liveness
        # LokiConfigs
        self.loki_configs = loki_configs
        # The Peak Volume instance ratio.
        self.max_surge_instance_ratio = max_surge_instance_ratio
        # The Peak Volume of instances.
        self.max_surge_instances = max_surge_instances
        # The memory size required by each instance, in MB. This value cannot be 0. The memory size has a one-to-one mapping with CPU. Only the following defined specifications are supported:
        # - **1024**: Corresponds to 500 millicores and 1000 millicores of CPU.
        # - **2048**: Corresponds to 500, 1000, and 2000 millicores of CPU.
        # - **4096**: Corresponds to 1000, 2000, and 4000 millicores of CPU.
        # - **8192**: Corresponds to 2000, 4000, and 8000 millicores of CPU.
        # - **12288**: Corresponds to 12000 millicores of CPU.
        # - **16384**: Corresponds to 4000, 8000, and 16000 millicores of CPU.
        # - **24576**: Corresponds to 12000 millicores of CPU.
        # - **32768**: Corresponds to 16000 millicores of CPU.
        # - **65536**: Corresponds to 8000, 16000, and 32000 millicores of CPU.
        # - **131072**: Corresponds to 32000 millicores of CPU.
        self.memory = memory
        # The Nacos registry. Valid values:
        # - **0**: SAE built-in Nacos.
        # - **1**: Self-managed Nacos.
        # - **2**: MSE commercial edition Nacos.
        self.micro_registration = micro_registration
        # The registry configuration. This parameter takes effect only when the registry type is MSE Nacos Enterprise Edition.
        self.micro_registration_config = micro_registration_config
        # The microservice governance configuration.
        # 
        # - Specifies whether to enable microservice governance (enable):
        # 
        #    - true: enabled
        # 
        #   - false: disabled
        # 
        # - Lossless rolling update configuration (mseLosslessRule):
        # 
        #   - delayTime: the delay time.
        # 
        #   - enable: specifies whether to enable the lossless online feature. true indicates enabled. false indicates disabled.
        # 
        #   - notice: specifies whether to enable the notification feature. true indicates enabled. false indicates disabled.
        # 
        #   - warmupTime: the warm-up duration for traffic ramping, in seconds.
        self.microservice_engine_config = microservice_engine_config
        # The minimum percentage of available instances. Valid values:
        # 
        # - **-1**: The default value, which indicates that the percentage is not used. If this parameter is not specified, the system uses **-1** by default.
        # - **0~100**: The unit is percentage, rounded up. For example, if set to **50**%, and the current number of instances is 5, the minimum number of available instances is 3.
        # 
        # > When both **MinReadyInstance** and **MinReadyInstanceRatio** are specified and the value of **MinReadyInstanceRatio** is not **-1**, the **MinReadyInstanceRatio** parameter takes precedence. For example, if **MinReadyInstances** is set to **5** and **MinReadyInstanceRatio** is set to **50**, the system uses **MinReadyInstanceRatio** to calculate the minimum number of available instances.
        self.min_ready_instance_ratio = min_ready_instance_ratio
        # The minimum number of available instances. Valid values:
        # 
        # - If set to **0**, the application interrupts services during the upgrade process.
        # - If set to **-1**, the system-recommended value is used, which is 25% of the current number of instances. If the current number of instances is 5, 5 × 25% = 1.25, which is rounded up to 2.
        # 
        # > Set the minimum number of available instances to ≥ 1 for each rolling deployment to avoid service interruptions.
        self.min_ready_instances = min_ready_instances
        # The mount description information.
        self.mount_desc = mount_desc
        # The mount point of NAS within the application VPC. If the configuration has not changed during deployment, you do not need to set this parameter (that is, the **MountHost** field does not need to be included in the request). To clear the NAS configuration, set the value of this field to an empty string in the request (that is, set the value of the **MountHost** field to "").
        self.mount_host = mount_host
        # The application ID on the Microservices Engine (MSE) side.
        self.mse_application_id = mse_application_id
        # The application name after the SAE service is registered with MSE.
        self.mse_application_name = mse_application_name
        # The namespace ID.
        self.namespace_id = namespace_id
        # The NAS mount configurations.
        self.nas_configs = nas_configs
        # NAS ID。
        self.nas_id = nas_id
        # The application version. Valid values:
        # 
        # - lite: Lite Edition
        # - std: Standard Edition
        # - pro: Professional Edition
        self.new_sae_version = new_sae_version
        # The RAM role for identity authentication.
        # > Create an OIDC identity provider and an identity provider role in the same region in advance. For more information, see [Create an OIDC identity provider](https://help.aliyun.com/document_detail/2331022.html) and [Create a role for SSO identity provider](https://help.aliyun.com/document_detail/2331016.html).
        self.oidc_role_name = oidc_role_name
        # The AccessKey ID for OSS read/write operations.
        self.oss_ak_id = oss_ak_id
        # The AccessKey Secret for OSS read/write operations.
        self.oss_ak_secret = oss_ak_secret
        # The OSS mount description.
        self.oss_mount_descs = oss_mount_descs
        # The application package type. Valid values:
        # 
        # - When you deploy with Java, **FatJar**, **War**, and **Image** are supported.
        # - When you deploy with PHP, the following types are supported:
        #     - **PhpZip**
        #     - **IMAGE_PHP_5_4**
        #     - **IMAGE_PHP_5_4_ALPINE**
        #     - **IMAGE_PHP_5_5**
        #     - **IMAGE_PHP_5_5_ALPINE**
        #     - **IMAGE_PHP_5_6**
        #     - **IMAGE_PHP_5_6_ALPINE**
        #     - **IMAGE_PHP_7_0**
        #     - **IMAGE_PHP_7_0_ALPINE**
        #     - **IMAGE_PHP_7_1**
        #     - **IMAGE_PHP_7_1_ALPINE**
        #     - **IMAGE_PHP_7_2**
        #     - **IMAGE_PHP_7_2_ALPINE**
        #     - **IMAGE_PHP_7_3**
        #     - **IMAGE_PHP_7_3_ALPINE**
        self.package_type = package_type
        # The deployment package URL. If your deployment package is uploaded through SAE, note the following:
        # 
        # - This URL cannot be used for direct download. Use the GetPackageVersionAccessableUrl operation to obtain a downloadable URL (valid for 10 minutes).
        # - SAE retains the package for a maximum of 90 days. After 90 days, the URL is no longer returned and the package is no longer available for download.
        self.package_url = package_url
        # The version of the deployment package. This parameter is required when **Package Type** is set to **FatJar** or **War**.
        self.package_version = package_version
        # The PHP version on which the PHP deployment package depends. Images are not supported.
        self.php = php
        # The mount path for PHP application monitoring. Make sure that the PHP server loads the configuration file from this path.
        # 
        # You do not need to manage the configuration content. SAE automatically renders the correct configuration file.
        self.php_arms_config_location = php_arms_config_location
        # The content of the PHP configuration file.
        self.php_config = php_config
        # The mount path of the PHP application startup configuration. Make sure that the PHP server uses this configuration file for startup.
        self.php_config_location = php_config_location
        # The script that is run after the container starts. A script is triggered immediately after the container is created. Format: `{"exec":{"command":["cat","/etc/group"\\]}}`
        self.post_start = post_start
        # The script that is run before the container stops. A script is triggered before the container is deleted. Format: `{"exec":{"command":["cat","/etc/group"\\]}}`
        self.pre_stop = pre_stop
        # The programming language of the technology stack used to create the application. Valid values:
        # 
        # - **java**: Java.
        # - **php**: PHP.
        # - **other**: Other languages, such as Python, C++, Go, .NET, and Node.js.
        self.programming_language = programming_language
        # Enables K8s Service-based service registration and discovery.
        self.pvtz_discovery = pvtz_discovery
        # The Python environment. PYTHON 3.9.15 is supported.
        self.python = python
        # The custom installation module dependencies. By default, the dependencies defined in the requirements.txt file in the root directory are installed. If no dependencies are configured or custom packages are needed, you can specify the dependencies to install.
        self.python_modules = python_modules
        self.rasp_config = rasp_config
        # The application startup status check. Containers that fail multiple health checks are shut down and restarted. Containers that do not pass the health check do not receive SLB traffic. The **exec**, **httpGet**, and **tcpSocket** methods are supported. For specific examples, see the **Liveness** parameter.
        # 
        # > You can select only one method for health checks.
        self.readiness = readiness
        # The region ID.
        self.region_id = region_id
        # The number of application instances.
        self.replicas = replicas
        # The resource type. Only `application` is supported.
        self.resource_type = resource_type
        # The Secret mount description.
        self.secret_mount_desc = secret_mount_desc
        # The security group ID.
        self.security_group_id = security_group_id
        # The canary release tags configured for the application.
        self.service_tags = service_tags
        # The sidecar container configuration.
        self.sidecar_containers_config = sidecar_containers_config
        # The settings for log collection to Simple Log Service (SLS).
        # 
        # - To use SLS resources that are automatically created by Serverless App Engine (SAE): `[{"logDir":"","logType":"stdout"},{"logDir":"/tmp/a.log"}]`.
        # - To use custom SLS resources: `[{"projectName":"test-sls","logType":"stdout","logDir":"","logstoreName":"sae","logtailName":""},{"projectName":"test","logDir":"/tmp/a.log","logstoreName":"sae","logtailName":""}]`.
        # 
        # Parameter descriptions:
        # 
        # - **projectName**: The name of the project in SLS.  
        # - **logDir**: The log path.
        # - **logType**: The log type. **stdout** indicates container standard output logs. You can set only one stdout entry. If this parameter is not set, file logs are collected.
        # - **logstoreName**: The name of the Logstore in SLS.
        # - **logtailName**: The name of the Logtail in SLS. If this parameter is not specified, a new Logtail is created through automatic creation.
        # 
        # If the SLS collection configuration has not changed during multiple deployments, you do not need to set this parameter (that is, the **SlsConfigs** field does not need to be included in the request). If you no longer need the SLS collection feature, set the value of this field to an empty string in the request (that is, set the value of the **SlsConfigs** field to "").
        self.sls_configs = sls_configs
        # sls log env tags
        self.sls_log_env_tags = sls_log_env_tags
        # The startup probe of the application.
        self.startup_probe = startup_probe
        # Configures K8s Service-based service registration and discovery with end-to-end canary release.
        self.swimlane_pvtz_discovery = swimlane_pvtz_discovery
        # The tag information.
        self.tags = tags
        # The graceful shutdown timeout period. Default value: 30. Unit: seconds. Valid values: 1 to 300.
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # The time zone. Default value: **Asia/Shanghai**.
        self.timezone = timezone
        # The Tomcat configuration. Set this parameter to "" or "{}" to delete the configuration:
        # 
        # - **port**: The port number. Valid values: 1024 to 65535. Ports smaller than 1024 require root permissions. Because the container is configured with admin permissions, specify a port greater than 1024. Default value: 8080.
        # - **contextPath**: The access path. Default value: root directory "/".
        # - **maxThreads**: The maximum number of connections in the connection pool. Default value: 400.
        # - **uriEncoding**: The encoding format of Tomcat. Valid values: **UTF-8**, **ISO-8859-1**, **GBK**, and **GB2312**. Default value: **ISO-8859-1**.
        # - **useBodyEncoding**: Specifies whether to use **BodyEncoding for URL**. Default value: **true**.
        self.tomcat_config = tomcat_config
        # The deployment policy. When the minimum number of available instances is 1, the value of the **UpdateStrategy** field is "". When the minimum number of available instances is greater than 1, examples are as follows:
        # 
        # - Canary release of 1 instance + 2 subsequent batches + automatic batching + 1-minute batch interval: `{"type":"GrayBatchUpdate","batchUpdate":{"batch":2,"releaseType":"auto","batchWaitTime":1},"grayUpdate":{"gray":1}}`
        #  
        # - Canary release of 1 instance + 2 subsequent batches + manual batching: `{"type":"GrayBatchUpdate","batchUpdate":{"batch":2,"releaseType":"manual"},"grayUpdate":{"gray":1}}`
        # 
        # - 2 batches + automatic batching + 0-minute batch interval: `{"type":"BatchUpdate","batchUpdate":{"batch":2,"releaseType":"auto","batchWaitTime":0}}`
        # 
        # Parameter descriptions:
        # 
        # - **type**: The release policy type. Valid values: **GrayBatchUpdate** (grayscale batch release) and **BatchUpdate** (batch release).
        # - **batchUpdate**: The batch release policy.
        #     - **batch**: The number of release batches.
        #     - **releaseType**: The processing method between batches. Valid values: **auto** (automatic) and **manual** (manual).
        #     - **batchWaitTime**: The interval between deployments within a batch, in seconds.
        # - **grayUpdate**: The remaining batches after grayscale release. This parameter is required when **type** is set to **GrayBatchUpdate**.
        self.update_strategy = update_strategy
        # vSwitch ID。
        self.v_switch_id = v_switch_id
        # VPC ID。
        self.vpc_id = vpc_id
        # The startup options for the WAR package application. The default startup command for the application: `java $JAVA_OPTS $CATALINA_OPTS -Options org.apache.catalina.startup.Bootstrap "$@" start`.
        self.war_start_options = war_start_options
        # The Tomcat version on which the deployment package depends. Valid values:
        # 
        # - **apache-tomcat-7.0.91**
        # - **apache-tomcat-8.5.42**
        # 
        # This parameter is not supported when **Package Type** is set to **Image**.
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
        if self.rasp_config:
            for v1 in self.rasp_config:
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

        if self.labels is not None:
            result['Labels'] = self.labels

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

        result['RaspConfig'] = []
        if self.rasp_config is not None:
            for k1 in self.rasp_config:
                result['RaspConfig'].append(k1.to_map() if k1 else None)

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

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

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

        self.rasp_config = []
        if m.get('RaspConfig') is not None:
            for k1 in m.get('RaspConfig'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataRaspConfig()
                self.rasp_config.append(temp_model.from_map(k1))

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
        # The tag key.
        self.key = key
        # The tag value.
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
        liveness: str = None,
        memory: int = None,
        name: str = None,
        post_start: str = None,
        pre_stop: str = None,
        readiness: str = None,
        secret_mount_desc: List[main_models.DescribeApplicationConfigResponseBodyDataSidecarContainersConfigSecretMountDesc] = None,
    ):
        # The ACR Enterprise instance ID. This parameter is required when **ImageUrl** is from ACR Enterprise Edition.
        self.acr_instance_id = acr_instance_id
        # The image startup command. This command must be an executable object that exists in the container. Example:
        # 
        # ```
        # command:
        #       - echo
        #       - abc
        #       - >
        #       - file0
        # ```
        # Based on the preceding example, `Command="echo", CommandArgs=["abc", ">", "file0"]`.
        self.command = command
        # The arguments for the image startup command. These are the arguments required by the startup command **Command**. Format:
        # 
        # `["a","b"]`
        # 
        # In the preceding example, `CommandArgs=["abc", ">", "file0"]`, where `["abc", ">", "file0"]` must be converted to the String type and the internal format is a JSON array. If this parameter is not required, leave it empty.
        self.command_args = command_args
        # The ConfigMap mount description. Use the configuration items created on the namespace configuration page to inject configuration information into the container. Parameter descriptions:
        # - **configMapId**: The ConfigMap instance ID. You can obtain this ID by calling the [ListNamespacedConfigMaps](https://help.aliyun.com/document_detail/176917.html) operation.
        # - **key**: The key-value pair.
        # > You can mount all keys by passing the `sae-sys-configmap-all` parameter.
        # - **mountPath**: The mount path.
        # - **ConfigMapName**: The ConfigMap name.
        self.config_map_mount_desc = config_map_mount_desc
        # The maximum CPU resources of the primary container that the sidecar container can use.
        self.cpu = cpu
        # The shared temporary storage. Sets a temporary storage directory and mounts it to the primary container and sidecar container.
        self.empty_dir_desc = empty_dir_desc
        # The container environment variable parameters. Custom values or references to configuration items are supported. To reference a configuration item, create a ConfigMap instance first. For more information, see [CreateConfigMap](https://help.aliyun.com/document_detail/176914.html). Valid values:
        # - Custom configuration
        #     - **name**: The environment variable name.
        #     - **value**: The environment variable value. This value takes precedence over valueFrom.
        # - Reference to a configuration item (valueFrom)
        #     - **name**: The environment variable name. You can reference a single key or all keys. To reference all keys, enter `sae-sys-configmap-all-<ConfigMap name>`, such as `sae-sys-configmap-all-test1`.
        #     - **valueFrom**: The environment variable reference. Set the value to `configMapRef`.
        #         - **configMapId**: The ConfigMap ID.
        #         - **key**: The key. If all keys are referenced, do not set this field.
        self.envs = envs
        # The image URL.
        self.image_url = image_url
        # The container health check.
        self.liveness = liveness
        # The maximum memory resources of the primary container that the sidecar container can use.
        self.memory = memory
        # The container name.
        self.name = name
        # The script that is run after the container starts.
        self.post_start = post_start
        # The script that is run before the container stops.
        self.pre_stop = pre_stop
        # The application startup status check.
        self.readiness = readiness
        # The Secret mount description.
        self.secret_mount_desc = secret_mount_desc

    def validate(self):
        if self.config_map_mount_desc:
            for v1 in self.config_map_mount_desc:
                 if v1:
                    v1.validate()
        if self.empty_dir_desc:
            for v1 in self.empty_dir_desc:
                 if v1:
                    v1.validate()
        if self.secret_mount_desc:
            for v1 in self.secret_mount_desc:
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

        if self.liveness is not None:
            result['Liveness'] = self.liveness

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.name is not None:
            result['Name'] = self.name

        if self.post_start is not None:
            result['PostStart'] = self.post_start

        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop

        if self.readiness is not None:
            result['Readiness'] = self.readiness

        result['SecretMountDesc'] = []
        if self.secret_mount_desc is not None:
            for k1 in self.secret_mount_desc:
                result['SecretMountDesc'].append(k1.to_map() if k1 else None)

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

        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')

        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')

        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')

        self.secret_mount_desc = []
        if m.get('SecretMountDesc') is not None:
            for k1 in m.get('SecretMountDesc'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataSidecarContainersConfigSecretMountDesc()
                self.secret_mount_desc.append(temp_model.from_map(k1))

        return self

class DescribeApplicationConfigResponseBodyDataSidecarContainersConfigSecretMountDesc(DaraModel):
    def __init__(
        self,
        key: str = None,
        mount_path: str = None,
        secret_id: int = None,
        secret_name: str = None,
    ):
        # The key with Base64-encoded data value.
        self.key = key
        # The mount path.
        self.mount_path = mount_path
        # The Secret instance ID.
        self.secret_id = secret_id
        # The Secret instance name.
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

class DescribeApplicationConfigResponseBodyDataSidecarContainersConfigEmptyDirDesc(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        name: str = None,
    ):
        # The mount path of the data volume in the container.
        self.mount_path = mount_path
        # The temporary storage name.
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
        # The ConfigMap instance ID.
        self.config_map_id = config_map_id
        # The ConfigMap name.
        self.config_map_name = config_map_name
        # The ConfigMap key.
        self.key = key
        # The container mount path.
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
        # The key with Base64-encoded data value.
        self.key = key
        # The mount path.
        self.mount_path = mount_path
        # The queried Secret instance ID.
        self.secret_id = secret_id
        # The Secret instance name.
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

class DescribeApplicationConfigResponseBodyDataRaspConfig(DaraModel):
    def __init__(
        self,
        enable_rasp: bool = None,
        rasp_app_key: str = None,
        rasp_app_name: str = None,
    ):
        self.enable_rasp = enable_rasp
        self.rasp_app_key = rasp_app_key
        self.rasp_app_name = rasp_app_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_rasp is not None:
            result['EnableRasp'] = self.enable_rasp

        if self.rasp_app_key is not None:
            result['RaspAppKey'] = self.rasp_app_key

        if self.rasp_app_name is not None:
            result['RaspAppName'] = self.rasp_app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableRasp') is not None:
            self.enable_rasp = m.get('EnableRasp')

        if m.get('RaspAppKey') is not None:
            self.rasp_app_key = m.get('RaspAppKey')

        if m.get('RaspAppName') is not None:
            self.rasp_app_name = m.get('RaspAppName')

        return self

class DescribeApplicationConfigResponseBodyDataOssMountDescs(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        bucket_path: str = None,
        mount_path: str = None,
        read_only: bool = None,
    ):
        # The bucket name.
        self.bucket_name = bucket_name
        # The directory or OSS object that you created in OSS. If the OSS mount directory does not exist, an exception is triggered.
        self.bucket_path = bucket_path
        # The container path in SAE. If the path already exists, it is overwritten. If the path does not exist, it is created.
        self.mount_path = mount_path
        # Indicates whether the container path has read-only permission to the mounted directory resources. Valid values:
        # 
        # - **true**: Read-only permission.
        # - **false**: Read and write permission.
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
        # The container mount path.
        self.mount_path = mount_path
        # The NAS relative file directory.
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
        secret_mount_desc: List[main_models.DescribeApplicationConfigResponseBodyDataInitContainersConfigSecretMountDesc] = None,
    ):
        # The image startup command. This command must be an executable object that exists in the container. Example:
        # 
        # ```
        # command:
        #       - echo
        #       - abc
        #       - >
        #       - file0
        # ```
        # Based on the preceding example, `Command="echo", CommandArgs=["abc", ">", "file0"]`.
        self.command = command
        # The arguments for the image startup command. These are the arguments required by the startup command **Command**. Format:
        # 
        # `["a","b"]`
        # 
        # In the preceding example, `CommandArgs=["abc", ">", "file0"]`, where `["abc", ">", "file0"]` must be converted to the String type and the internal format is a JSON array. If this parameter is not required, leave it empty.
        self.command_args = command_args
        # The ConfigMap information.
        self.config_map_mount_desc = config_map_mount_desc
        # The shared temporary storage.
        self.empty_dir_desc = empty_dir_desc
        # The container environment variable parameters. You can customize environment variables or reference ConfigMap instances. To reference a ConfigMap instance, create a ConfigMap instance first. For more information, see [CreateConfigMap](https://help.aliyun.com/document_detail/176914.html). Valid values:
        # - Custom configuration
        #     - **name**: the name of the environment variable.
        #     - **value**: the value of the environment variable. This takes priority over valueFrom.
        # - Reference a ConfigMap instance (valueFrom)
        #     - **name**: the name of the environment variable. You can reference a single key or all keys. To reference all keys, enter `sae-sys-configmap-all-<ConfigMap name>`, such as `sae-sys-configmap-all-test1`.
        #     - **valueFrom**: the reference of the environment variable. Set the value to `configMapRef`.
        #     - **configMapId**: the ID of the ConfigMap instance.
        #     - **key**: the key. Do not set this field if you want to reference all keys.
        # - Reference a secret (valueFrom)
        #     - **name**: the name of the environment variable. You can reference a single key or all keys. To reference all keys, enter `sae-sys-secret-all-<secret name>`, such as `sae-sys-secret-all-test1`.
        #     - **valueFrom**: the reference of the environment variable. Set the value to `secretRef`.
        #     - **secretId**: the ID of the secret.
        #     - **key**: the key. Do not set this field if you want to reference all keys.
        self.envs = envs
        # The image URL used by the init container.
        # [_single.resp.200.props.Data.InitContainersConfig.items.Env
        self.image_url = image_url
        # The init container name.
        self.name = name
        # The Secret mount description.
        self.secret_mount_desc = secret_mount_desc

    def validate(self):
        if self.config_map_mount_desc:
            for v1 in self.config_map_mount_desc:
                 if v1:
                    v1.validate()
        if self.empty_dir_desc:
            for v1 in self.empty_dir_desc:
                 if v1:
                    v1.validate()
        if self.secret_mount_desc:
            for v1 in self.secret_mount_desc:
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

        result['SecretMountDesc'] = []
        if self.secret_mount_desc is not None:
            for k1 in self.secret_mount_desc:
                result['SecretMountDesc'].append(k1.to_map() if k1 else None)

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

        self.secret_mount_desc = []
        if m.get('SecretMountDesc') is not None:
            for k1 in m.get('SecretMountDesc'):
                temp_model = main_models.DescribeApplicationConfigResponseBodyDataInitContainersConfigSecretMountDesc()
                self.secret_mount_desc.append(temp_model.from_map(k1))

        return self

class DescribeApplicationConfigResponseBodyDataInitContainersConfigSecretMountDesc(DaraModel):
    def __init__(
        self,
        key: str = None,
        mount_path: str = None,
        secret_id: int = None,
        secret_name: str = None,
    ):
        # The key.
        self.key = key
        # The mount path.
        self.mount_path = mount_path
        # The Secret instance ID.
        self.secret_id = secret_id
        # The Secret instance name.
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

class DescribeApplicationConfigResponseBodyDataInitContainersConfigEmptyDirDesc(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        name: str = None,
    ):
        # The mount path of the data volume in the container.
        self.mount_path = mount_path
        # The temporary storage name.
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
        # The ConfigMap name.
        self.config_map_name = config_map_name
        # The ConfigMap key-value pair.
        self.key = key
        # The container mount path.
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
        # The mount path.
        self.mount_path = mount_path
        # The temporary storage name.
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
        # ConfigMap ID。
        self.config_map_id = config_map_id
        # The ConfigMap name.
        self.config_map_name = config_map_name
        # The ConfigMap key-value pair.
        self.key = key
        # The container mount path.
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

