# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class CreateApplicationRequest(DaraModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        acr_instance_id: str = None,
        agent_version: str = None,
        app_description: str = None,
        app_name: str = None,
        app_source: str = None,
        associate_eip: bool = None,
        auto_config: bool = None,
        base_app_id: str = None,
        command: str = None,
        command_args: str = None,
        config_map_mount_desc: str = None,
        cpu: int = None,
        custom_host_alias: str = None,
        custom_image_network_type: str = None,
        deploy: bool = None,
        disk_size: int = None,
        dotnet: str = None,
        edas_container_version: str = None,
        empty_dir_desc: str = None,
        enable_cpu_burst: bool = None,
        enable_ebpf: str = None,
        enable_namespace_agent_version: bool = None,
        enable_namespace_sls_config: bool = None,
        enable_new_arms: bool = None,
        enable_prometheus: bool = None,
        enable_sidecar_resource_isolated: bool = None,
        envs: str = None,
        gpu_config: str = None,
        headless_pvtz_discovery_svc: str = None,
        html: str = None,
        image_pull_secrets: str = None,
        image_url: str = None,
        init_containers_config: List[main_models.InitContainerConfig] = None,
        is_stateful: bool = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        kafka_configs: str = None,
        liveness: str = None,
        loki_configs: str = None,
        memory: int = None,
        micro_registration: str = None,
        micro_registration_config: str = None,
        microservice_engine_config: str = None,
        mount_desc: str = None,
        mount_host: str = None,
        namespace_id: str = None,
        nas_configs: str = None,
        nas_id: str = None,
        new_sae_version: str = None,
        oidc_role_name: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: str = None,
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
        pvtz_discovery_svc: str = None,
        python: str = None,
        python_modules: str = None,
        readiness: str = None,
        replicas: int = None,
        resource_type: str = None,
        sae_version: str = None,
        secret_mount_desc: str = None,
        security_group_id: str = None,
        service_tags: str = None,
        sidecar_containers_config: List[main_models.SidecarContainerConfig] = None,
        sls_configs: str = None,
        sls_log_env_tags: str = None,
        startup_probe: str = None,
        termination_grace_period_seconds: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        war_start_options: str = None,
        web_container: str = None,
    ):
        # The Alibaba Cloud Resource Name (ARN) required for a RAM role to obtain images across accounts. For more information, see [Grant permissions across Alibaba Cloud accounts by using a RAM role](https://help.aliyun.com/document_detail/223585.html).
        self.acr_assume_role_arn = acr_assume_role_arn
        # The ID of Container Registry Enterprise Edition instance N. This parameter is required when the **ImageUrl** parameter is set to the URL of an image in an ACR Enterprise Edition instance.
        self.acr_instance_id = acr_instance_id
        self.agent_version = agent_version
        # The description of the template. The description cannot exceed 1,024 characters in length.
        self.app_description = app_description
        # The name of the application. The name can contain digits, letters, and hyphens (-). The name must start with a letter and cannot end with a hyphen (-). It cannot exceed 36 characters in length.
        # 
        # This parameter is required.
        self.app_name = app_name
        # Select micro_service, which is the application.
        self.app_source = app_source
        # Specifies whether to associate an EIP with the node pool. Take note of the following rules:
        # 
        # *   **true**: The EIP is associated with the application instance.
        # *   **false**: The EIP is not associated with the application instance.
        self.associate_eip = associate_eip
        # Specifies whether to automatically configure the network environment. Valid values:
        # 
        # *   **true**: SAE automatically configures the network environment when you create the application. If you set this parameter to true, the values of the **NamespaceId**, **VpcId**, **vSwitchId**, and **SecurityGroupId** parameters are ignored.
        # *   **false**: SAE configures the network environment based on your settings when you create the application.
        # 
        # >  If you select **true**, other **NamespaceId** will be ignored.
        self.auto_config = auto_config
        # The ID of the basic application.
        self.base_app_id = base_app_id
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
        # > You can use `sae-sys-configmap-all` to mount all keys.
        # 
        # *   **mountPath**: the mount path in the container.
        self.config_map_mount_desc = config_map_mount_desc
        # The CPU specifications that are required for each instance. Unit: millicores. This parameter cannot be set to 0. Valid values:
        # 
        # *   **500**
        # *   **1000**
        # *   **2000**
        # *   **4000**
        # *   **8000**
        # *   **12000**
        # *   **16000**
        # *   **32000**
        self.cpu = cpu
        # The custom mappings between hostnames and IP addresses in the container. Take note of the following rules:
        # 
        # *   **hostName**: the domain name or hostname.
        # *   **ip**: the IP address.
        self.custom_host_alias = custom_host_alias
        # Custom image type. To it to empty string to use pre-built image.
        # 
        # - internet: Public network image
        # 
        # - intranet: Private network image
        self.custom_image_network_type = custom_image_network_type
        # Whether to deploy now.
        # 
        # *   **true** (default): Deploy now.
        # *   **false**: Deploy later.
        self.deploy = deploy
        # The disk size. Unit: GB.
        self.disk_size = disk_size
        # . NET Framework version number:
        # 
        # *   .NET 3.1
        # *   .NET 5.0
        # *   .NET 6.0
        # *   .NET 7.0
        # *   .NET 8.0
        self.dotnet = dotnet
        # The version of the container in HSF.
        self.edas_container_version = edas_container_version
        self.empty_dir_desc = empty_dir_desc
        # Enable CPU Burst.
        # - true: enable
        # - false: disable
        self.enable_cpu_burst = enable_cpu_burst
        # Enable application monitoring for non-Java applications based on eBPF technology. The value options are as follows:
        # 
        # - true: Enable.
        # - false: Disable (default).
        self.enable_ebpf = enable_ebpf
        self.enable_namespace_agent_version = enable_namespace_agent_version
        self.enable_namespace_sls_config = enable_namespace_sls_config
        # Indicates whether to enable the new ARMS feature:
        # 
        # *   true: enables this parameter.
        # *   false: disables this parameter.
        self.enable_new_arms = enable_new_arms
        self.enable_prometheus = enable_prometheus
        # Enable Sidecar resource isolation.
        # 
        # - true: enable
        # - false: disable
        self.enable_sidecar_resource_isolated = enable_sidecar_resource_isolated
        # The environment variables. You can configure custom environment variables or reference a ConfigMap. Before you can reference a ConfigMap, you must create a ConfigMap. For more information, see [CreateConfigMap](https://help.aliyun.com/document_detail/176914.html). Valid values:
        # 
        # *   Custom configuration
        # 
        #     *   **name**: the name of the environment variable.
        #     *   **value**: the value of the environment variable. The priority of the custom configuration is higher than valueFrom.
        # 
        # *   Reference a ConfigMap (valueFrom)
        # 
        #     *   **name**: the name of the environment variable. You can reference one or all keys. To reference all keys, specify `sae-sys-configmap-all-<ConfigMap name>`. Example: `sae-sys-configmap-all-test1`.
        #     *   **valueFrom**: the reference of the environment variable. Valid value: `configMapRef`.
        #     *   **configMapId**: the ID of the ConfigMap.
        #     *   **key**: the key. If you want to reference all key values, you do not need to configure this parameter.
        self.envs = envs
        self.gpu_config = gpu_config
        self.headless_pvtz_discovery_svc = headless_pvtz_discovery_svc
        self.html = html
        # The ID of the corresponding Secret.
        self.image_pull_secrets = image_pull_secrets
        # The URL of the image. This parameter is required if you set the `PackageType` parameter to `Image`.
        self.image_url = image_url
        # Initialize container configuration.
        self.init_containers_config = init_containers_config
        self.is_stateful = is_stateful
        # The arguments in the JAR package. The arguments are used to start the application container. The default startup command is `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`.
        self.jar_start_args = jar_start_args
        # The option settings in the JAR package. The settings are used to start the application container. The default startup command for application deployment is `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`.
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
        # The logging configurations of Message Queue for Apache Kafka. Take note of the following rules:
        # 
        # *   **kafkaEndpoint**: the endpoint of the Message Queue for Apache Kafka API.
        # *   **kafkaInstanceId**: the ID of the Message Queue for Apache Kafka instance.
        # *   **kafkaConfigs**: One or more logging configurations of Message Queue for Apache Kafka. For information about sample values and parameters, see the request parameter **KafkaLogfileConfig** in this topic.
        self.kafka_configs = kafka_configs
        # Container health check. If the container fails this check, it will be revoked and relaunch again. Use one of the following methods to perform the health check:
        # 
        # *   Example of **exec**: `{"exec":{"command":["sh","-c","cat/home/admin/start.sh"]},"initialDelaySeconds":30,"periodSeconds":30,"timeoutSeconds":2}`
        # *   Sample code of the **httpGet** method: `{"httpGet":{"path":"/","port":18091,"scheme":"HTTP","isContainKeyWord":true,"keyWord":"SAE"},"initialDelaySeconds":11,"periodSeconds":10,"timeoutSeconds":1}`
        # *   Sample code of the **tcpSocket** method: `{"tcpSocket":{"port":18091},"initialDelaySeconds":11,"periodSeconds":10,"timeoutSeconds":1}`
        # 
        # > You can use only one method to perform the health check.
        # 
        # The following table describes the parameters that are used in the preceding statements.
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
        # The memory size that is required by each instance. Unit: MB. This parameter cannot be set to 0. The values of this parameter correspond to the values of the Cpu parameter:
        # 
        # *   This parameter is set to **1024** if the Cpu parameter is set to 500 or 1000.
        # *   This parameter is set to **2048** if the Cpu parameter is set to 500, 1000, or 2000.
        # *   This parameter is set to **4096** if the Cpu parameter is set to 1000, 2000, or 4000.
        # *   This parameter is set to **8192** if the Cpu parameter is set to 2000, 4000, or 8,000.
        # *   This parameter is set to **12288** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **16384** if the Cpu parameter is set to 4000, 8000, or 16000.
        # *   This parameter is set to **24576** if the Cpu parameter is set to 12000.
        # *   This parameter is set to **32768** if the Cpu parameter is set to 16000.
        # *   This parameter is set to **65536** if the Cpu parameter is set to 8000, 16000, or 32000.
        # *   This parameter is set to **131072** if the Cpu parameter is set to 32000.
        self.memory = memory
        # The Nacos registry. Valid values:
        # 
        # *   **0**: SAE built-in Nacos registry
        # *   **1**: self-managed Nacos registry
        # *   **2** : MSE enterprise edition Nacos registry
        self.micro_registration = micro_registration
        # The Registry configurations.
        self.micro_registration_config = micro_registration_config
        # Configure microservices governance
        # 
        # Whether to enable microservices governance (enable):
        # - true: Enable
        # - false: Disable
        # 
        # Configure lossless online/offline deployment (mseLosslessRule):
        # 
        # delayTime: Delay duration (unit: seconds)
        # 
        # enable: Whether to enable lossless deployment
        # 
        # - true: Enable
        # 
        # - false: Disable
        # 
        # notice: Whether to enable notifications
        # 
        # - true: Enable
        # 
        # - false: Disable
        # 
        # warmupTime: Small-traffic warm-up duration (unit: seconds)
        self.microservice_engine_config = microservice_engine_config
        # It is not recommended to configure this field; configuring NasConfigs instead. This field specifies the NAS mount description. When deploying, if the configuration has not changed, you do not need to set this parameter (i.e., the MountDesc field does not need to be included in the request). If you need to clear the NAS configuration, set the value of this field to an empty string in the request (i.e., set the value of the MountDesc field to "").
        self.mount_desc = mount_desc
        # It is not recommended to configure this field; configuring NasConfigs instead. This field specifies the NAS mount point within the application\\"s VPC. When deploying, if the configuration has not changed, you do not need to set this parameter (i.e., the MountHost field does not need to be included in the request). If you need to clear the NAS configuration, set the value of this field to an empty string in the request (i.e., set the value of the MountHost field to "").
        self.mount_host = mount_host
        # SAE namespace ID. Only namespaces consisting of lowercase letters and hyphens (-) are supported, and the name must start with a letter.
        self.namespace_id = namespace_id
        # The configurations of mounting the NAS file system. Take note of the following rules:
        # 
        # *   **mountPath**: the mount path of the container.
        # *   **readOnly**: If you set the value to **false**, the application has the read and write permissions.
        # *   **nasId**: the ID of the NAS file system.
        # *   **mountDomain**: the domain name of the mount target. For more information, see [DescribeMountTargets](https://help.aliyun.com/document_detail/62626.html).
        # *   **nasPath**: the directory in the NAS file system.
        self.nas_configs = nas_configs
        # It is not recommended to configure this field; configuring NasConfigs instead. The ID of the mounted NAS must be in the same region as the cluster. The NAS must have available mount point quota or its mount point must already be on a switch within the VPC. If this field is not specified and the mountDescs field exists, a NAS will be automatically purchased and mounted to a switch within the VPC by default.
        # 
        # When deploying, if the configuration has not changed, you do not need to set this parameter (i.e., the NASId field does not need to be included in the request). If you need to clear the NAS configuration, set the value of this field to an empty string in the request (i.e., set the value of the NASId field to "").
        self.nas_id = nas_id
        # SAE edition.
        # 
        # - lite: the lightweight edition.
        # 
        # - std: the standard edition.
        # 
        # - pro: the professional edition.
        self.new_sae_version = new_sae_version
        # The name of the RAM role used to authenticate the user identity.
        # 
        # >  You need to create an OpenID Connect (OIDC) identity provider (IdP) and an identity provider (IdP) for role-based single sign-on (SSO) in advance. For more information, see [Creates an OpenID Connect (OIDC) identity provider (IdP)](https://help.aliyun.com/document_detail/2331022.html) and [Creates an identity provider (IdP) for role-based single sign-on (SSO)](https://help.aliyun.com/document_detail/2331016.html).
        self.oidc_role_name = oidc_role_name
        # The Accesskey ID that the OSS reads and writes from.
        self.oss_ak_id = oss_ak_id
        # The AccessKey Secret that the OSS reads and writes from.
        self.oss_ak_secret = oss_ak_secret
        # Information of the Object Storage Service (OSS) bucket mounted to the application. The following table describes the parameters that are used in the preceding statements.
        # 
        # *   **bucketName**: the name of the OSS bucket.
        # 
        # *   **bucketPath**: the directory or object in OSS. If the specified directory or object does not exist, an error is returned.
        # 
        # *   **mountPath**: the directory of the container in SAE. If the path already exists, the newly specified path overwrites the previous one. If the path does not exist, it is created.
        # 
        # *   **readOnly**: specifies whether to only allow the container path to read data from the OSS directory. Valid values:
        # 
        #     *   **true**: The container path only has read permission on the OSS directory.
        #     *   **false**: The application has read and write permissions.
        self.oss_mount_descs = oss_mount_descs
        # The type of the deployment package. Take note of the following rules:
        # 
        # *   If you deploy the application by using a Java Archive (JAR) package, you can set this parameter to **FatJar**, **War**, or **Image**.
        # *   If you deploy the application by using a PHP package, you can set this parameter to one of the following values:
        # 
        # **PhpZip** **IMAGE_PHP_5_4** **IMAGE_PHP_5_4_ALPINE** **IMAGE_PHP_5_5** **IMAGE_PHP_5_5_ALPINE** **IMAGE_PHP_5_6** **IMAGE_PHP_5_6_ALPINE** **IMAGE_PHP_7_0** **IMAGE_PHP_7_0_ALPINE** **IMAGE_PHP_7_1** **IMAGE_PHP_7_1_ALPINE** **IMAGE_PHP_7_2** **IMAGE_PHP_7_2_ALPINE** **IMAGE_PHP_7_3** **IMAGE_PHP_7_3_ALPINE**
        # 
        # *   If you deploy the application by using a **Python** package, you can set this parameter to **PythonZip** or **Image**:
        # 
        # This parameter is required.
        self.package_type = package_type
        # The address of the deployment package. This parameter is required if you set **PackageType** to **FatJar**, **War**, or **PythonZip**.
        self.package_url = package_url
        # The version of the deployment package. This parameter is required when the **PackageType** parameter is set to **FatJar**, **War**, or **PythonZip**.
        self.package_version = package_version
        # The dependent PHP version of PHP package. Image is not supported.
        self.php = php
        # The path on which the PHP configuration file for application monitoring is mounted. Make sure that the PHP server loads the configuration file. SAE automatically generates the corresponding configuration file. No manual operations are required.
        self.php_arms_config_location = php_arms_config_location
        # The details of the PHP configuration file.
        self.php_config = php_config
        # The path on which the PHP configuration file for application startup is mounted. Make sure that the PHP server uses this configuration file during the startup.
        self.php_config_location = php_config_location
        # Control whether to run a script after the container is initialized. Example: {"exec":{"command":["cat","/etc/group"]}}
        self.post_start = post_start
        # To controle whether to run a script before the container stops. Example: {"exec":{"command":["cat","/etc/group"]}}
        self.pre_stop = pre_stop
        # The programming language for the application’s technology stack. The value options are as follows:
        # 
        # - java: Java language
        # - php: PHP language
        # - python: Python language
        # - dotnet: .NET Core language
        # - other: Multi-language, such as C++, Go, Node.js, etc.
        self.programming_language = programming_language
        # The configurations of Kubernetes Service-based service registration and discovery. Take note of the following rules:
        # 
        # *   **serviceName**: the name of the Alibaba Cloud service. Format: `<Custom content>-<Namespace ID>`. `-<Namespace ID>` is automatically specified based on the namespace in which an application resides and cannot be changed. For example, if you select the default namespace in the China (Beijing) region, `-cn-beijing-default` is automatically specified.
        # *   **namespaceId**: the namespace ID.
        # *   **portAndProtocol**: the port number and protocol. Valid values of the port number: 1 to 65535. Valid values of the protocol: **TCP** and **UDP**.
        # *   **enable**: enables the Kubernetes Service-based registration and discovery feature.
        self.pvtz_discovery_svc = pvtz_discovery_svc
        # The Python environment. Set the value to **PYTHON 3.9.15**.
        self.python = python
        # The configurations for installing custom module dependencies. By default, the dependencies defined by the requirements.txt file in the root directory are installed. If the package does not contain this file and you do not configure custom dependencies in the package, specify the dependencies that you want to install in the text box.
        self.python_modules = python_modules
        # Check the launch status of the container. Containers that fail health checks more than once will not receive traffic from Server Load Balancer (SLB) instances any loner. You can use the **exec**, **httpGet**, or **tcpSocket** method to perform health checks. For more information, see the description of the **Liveness** parameter.
        # 
        # > You can use only one method to perform the health check.
        self.readiness = readiness
        # The number of instances when initialized.
        # 
        # This parameter is required.
        self.replicas = replicas
        # The resource type. Supports NULL (default) and haiguang (haiguang server).
        self.resource_type = resource_type
        # The SAE version. Supported versions:
        # 
        # *   **v1**
        # *   **v2**
        self.sae_version = sae_version
        # Secret Mount Description
        # Use the secret dictionaries created in the Namespace Secret Dictionary page to inject information into containers. Parameter descriptions are as follows:
        # 
        # - secretId: Secret instance ID. Obtain via the ListSecrets interface.
        # 
        # - key: Key-value pair. Note: Set the parameter sae-sys-secret-all to mount all keys.
        # 
        # - mountPath: Mount path.
        self.secret_mount_desc = secret_mount_desc
        # Security group ID.
        self.security_group_id = security_group_id
        # The canary tag configured for the application.
        self.service_tags = service_tags
        # The configuration of the container.
        self.sidecar_containers_config = sidecar_containers_config
        # The logging configurations of Log Service.
        # 
        # *   To use Log Service resources that are automatically created by SAE, set this parameter to `[{"logDir":"","logType":"stdout"},{"logDir":"/tmp/a.log"}]`.
        # *   To use custom Log Service resources, set this parameter to `[{"projectName":"test-sls","logType":"stdout","logDir":"","logstoreName":"sae","logtailName":""},{"projectName":"test","logDir":"/tmp/a.log","logstoreName":"sae","logtailName":""}]`.
        # 
        # The following table describes the parameters that are used in the preceding statements.
        # 
        # *   **projectName**: the name of the Log Service project.
        # *   **logDir**: the path in which logs are stored.
        # *   **logType**: the log type. **stdout**: the standard output log of the container. You can specify only one stdout value for this parameter. If you leave this parameter empty, file logs are collected.
        # *   **logstoreName**: the name of the Logstore in Log Service.
        # *   **logtailName**: the name of the Logtail configuration in Log Service. If you do not configure this parameter, a new Logtail configuration is created.
        # 
        # If you do not need to modify the logging configurations when you deploy the application, configure the **SlsConfigs** parameter only in the first request. You do not need to include this parameter in subsequent requests. If you no longer need to use Log Service, leave the **SlsConfigs** parameter empty in the request.
        # 
        # > A Log Service project that is automatically created by SAE when you create an application is deleted when the application is deleted. Therefore, when you create an application, you cannot select a Log Service project that is automatically created by SAE for log collection.
        self.sls_configs = sls_configs
        self.sls_log_env_tags = sls_log_env_tags
        # Enable application startup probe.
        # 
        # Check succeeded: Indicates that the application has started successfully. If you have configured Liveness and Readiness checks, they will be performed after the application startup is successful.
        # Check failed: Indicates that the application failed to start; an exception will be reported and the application will be automatically restarted.
        # 
        # > - exec, httpGet, and tcpSocket methods are supported. For specific examples, see the Liveness parameter documentation.
        # > - Only one health check method can be selected.
        self.startup_probe = startup_probe
        # The timeout period for a graceful shutdown. Default value: 30. Unit: seconds. Valid values: 1 to 300.
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # Time zone. Default to time zone of Asia/Shanghai.
        self.timezone = timezone
        # The Tomcat configuration. If you want to cancel this configuration, set this parameter to "" or "{}". The following variables are included in the configuration: Take note of the following rules:
        # 
        # *   **port**: the port number. The port number ranges from 1024 to 65535. Though the admin permissions are configured for the container, the root permissions are required to perform operations on ports whose number is smaller than 1024. Enter a value that ranges from 1025 to 65535 because the container has only the admin permissions. If you do not specify this parameter, the default port number 8080 is used.
        # *   **contextPath**: the path. Default value: /. This value indicates the root directory.
        # *   **maxThreads**: the maximum number of connections in the connection pool. Default value: 400.
        # *   **uriEncoding**: the URI encoding scheme in the Tomcat container. Valid values: UTF-8, ISO-8859-1, GBK, and GB2312.************ If you do not specify this parameter, the default value **ISO-8859-1** is used.
        # *   **useBodyEncoding**: specifies whether to use the encoding scheme specified in the request body for URI query parameters. Default value: true.
        self.tomcat_config = tomcat_config
        # The vSwitch to which the elastic network interface (ENI) of the application instance is connected. The vSwitch must be located in the VPC specified by the VpcId parameter. The SAE namespace is bound with this vSwitch. The default value is the ID of the vSwitch that is bound to the namespace.
        self.v_switch_id = v_switch_id
        # The ID of the virtual private cloud (VPC) that corresponds to the SAE namespace. In SAE, once correspondence is configured between a namespace and a VPC, the namespace cannot correspond to other VPCs. When the SAE application is created within the namespace, the application is bound with the VPC. Multiple namespaces can correspond to the same VPC. The default value is the ID of the VPC that is bound to the namespace.
        self.vpc_id = vpc_id
        # The startup command of the WAR package. For information about how to configure the startup command, see [Configure startup commands](https://help.aliyun.com/document_detail/96677.html).
        self.war_start_options = war_start_options
        # The version of the Tomcat container on which the deployment package depends. Valid values:
        # 
        # *   **apache-tomcat-7.0.91**
        # *   **apache-tomcat-8.5.42**
        # 
        # This parameter is not returned if the **PackageType** parameter is set to **Image**.
        self.web_container = web_container

    def validate(self):
        if self.init_containers_config:
            for v1 in self.init_containers_config:
                 if v1:
                    v1.validate()
        if self.sidecar_containers_config:
            for v1 in self.sidecar_containers_config:
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

        if self.app_description is not None:
            result['AppDescription'] = self.app_description

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.app_source is not None:
            result['AppSource'] = self.app_source

        if self.associate_eip is not None:
            result['AssociateEip'] = self.associate_eip

        if self.auto_config is not None:
            result['AutoConfig'] = self.auto_config

        if self.base_app_id is not None:
            result['BaseAppId'] = self.base_app_id

        if self.command is not None:
            result['Command'] = self.command

        if self.command_args is not None:
            result['CommandArgs'] = self.command_args

        if self.config_map_mount_desc is not None:
            result['ConfigMapMountDesc'] = self.config_map_mount_desc

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias

        if self.custom_image_network_type is not None:
            result['CustomImageNetworkType'] = self.custom_image_network_type

        if self.deploy is not None:
            result['Deploy'] = self.deploy

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.dotnet is not None:
            result['Dotnet'] = self.dotnet

        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version

        if self.empty_dir_desc is not None:
            result['EmptyDirDesc'] = self.empty_dir_desc

        if self.enable_cpu_burst is not None:
            result['EnableCpuBurst'] = self.enable_cpu_burst

        if self.enable_ebpf is not None:
            result['EnableEbpf'] = self.enable_ebpf

        if self.enable_namespace_agent_version is not None:
            result['EnableNamespaceAgentVersion'] = self.enable_namespace_agent_version

        if self.enable_namespace_sls_config is not None:
            result['EnableNamespaceSlsConfig'] = self.enable_namespace_sls_config

        if self.enable_new_arms is not None:
            result['EnableNewArms'] = self.enable_new_arms

        if self.enable_prometheus is not None:
            result['EnablePrometheus'] = self.enable_prometheus

        if self.enable_sidecar_resource_isolated is not None:
            result['EnableSidecarResourceIsolated'] = self.enable_sidecar_resource_isolated

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.gpu_config is not None:
            result['GpuConfig'] = self.gpu_config

        if self.headless_pvtz_discovery_svc is not None:
            result['HeadlessPvtzDiscoverySvc'] = self.headless_pvtz_discovery_svc

        if self.html is not None:
            result['Html'] = self.html

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

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.micro_registration is not None:
            result['MicroRegistration'] = self.micro_registration

        if self.micro_registration_config is not None:
            result['MicroRegistrationConfig'] = self.micro_registration_config

        if self.microservice_engine_config is not None:
            result['MicroserviceEngineConfig'] = self.microservice_engine_config

        if self.mount_desc is not None:
            result['MountDesc'] = self.mount_desc

        if self.mount_host is not None:
            result['MountHost'] = self.mount_host

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

        if self.oss_mount_descs is not None:
            result['OssMountDescs'] = self.oss_mount_descs

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

        if self.pvtz_discovery_svc is not None:
            result['PvtzDiscoverySvc'] = self.pvtz_discovery_svc

        if self.python is not None:
            result['Python'] = self.python

        if self.python_modules is not None:
            result['PythonModules'] = self.python_modules

        if self.readiness is not None:
            result['Readiness'] = self.readiness

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.sae_version is not None:
            result['SaeVersion'] = self.sae_version

        if self.secret_mount_desc is not None:
            result['SecretMountDesc'] = self.secret_mount_desc

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

        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config

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

        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AppSource') is not None:
            self.app_source = m.get('AppSource')

        if m.get('AssociateEip') is not None:
            self.associate_eip = m.get('AssociateEip')

        if m.get('AutoConfig') is not None:
            self.auto_config = m.get('AutoConfig')

        if m.get('BaseAppId') is not None:
            self.base_app_id = m.get('BaseAppId')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')

        if m.get('ConfigMapMountDesc') is not None:
            self.config_map_mount_desc = m.get('ConfigMapMountDesc')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')

        if m.get('CustomImageNetworkType') is not None:
            self.custom_image_network_type = m.get('CustomImageNetworkType')

        if m.get('Deploy') is not None:
            self.deploy = m.get('Deploy')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('Dotnet') is not None:
            self.dotnet = m.get('Dotnet')

        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')

        if m.get('EmptyDirDesc') is not None:
            self.empty_dir_desc = m.get('EmptyDirDesc')

        if m.get('EnableCpuBurst') is not None:
            self.enable_cpu_burst = m.get('EnableCpuBurst')

        if m.get('EnableEbpf') is not None:
            self.enable_ebpf = m.get('EnableEbpf')

        if m.get('EnableNamespaceAgentVersion') is not None:
            self.enable_namespace_agent_version = m.get('EnableNamespaceAgentVersion')

        if m.get('EnableNamespaceSlsConfig') is not None:
            self.enable_namespace_sls_config = m.get('EnableNamespaceSlsConfig')

        if m.get('EnableNewArms') is not None:
            self.enable_new_arms = m.get('EnableNewArms')

        if m.get('EnablePrometheus') is not None:
            self.enable_prometheus = m.get('EnablePrometheus')

        if m.get('EnableSidecarResourceIsolated') is not None:
            self.enable_sidecar_resource_isolated = m.get('EnableSidecarResourceIsolated')

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('GpuConfig') is not None:
            self.gpu_config = m.get('GpuConfig')

        if m.get('HeadlessPvtzDiscoverySvc') is not None:
            self.headless_pvtz_discovery_svc = m.get('HeadlessPvtzDiscoverySvc')

        if m.get('Html') is not None:
            self.html = m.get('Html')

        if m.get('ImagePullSecrets') is not None:
            self.image_pull_secrets = m.get('ImagePullSecrets')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        self.init_containers_config = []
        if m.get('InitContainersConfig') is not None:
            for k1 in m.get('InitContainersConfig'):
                temp_model = main_models.InitContainerConfig()
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

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MicroRegistration') is not None:
            self.micro_registration = m.get('MicroRegistration')

        if m.get('MicroRegistrationConfig') is not None:
            self.micro_registration_config = m.get('MicroRegistrationConfig')

        if m.get('MicroserviceEngineConfig') is not None:
            self.microservice_engine_config = m.get('MicroserviceEngineConfig')

        if m.get('MountDesc') is not None:
            self.mount_desc = m.get('MountDesc')

        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')

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

        if m.get('OssMountDescs') is not None:
            self.oss_mount_descs = m.get('OssMountDescs')

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

        if m.get('PvtzDiscoverySvc') is not None:
            self.pvtz_discovery_svc = m.get('PvtzDiscoverySvc')

        if m.get('Python') is not None:
            self.python = m.get('Python')

        if m.get('PythonModules') is not None:
            self.python_modules = m.get('PythonModules')

        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SaeVersion') is not None:
            self.sae_version = m.get('SaeVersion')

        if m.get('SecretMountDesc') is not None:
            self.secret_mount_desc = m.get('SecretMountDesc')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('ServiceTags') is not None:
            self.service_tags = m.get('ServiceTags')

        self.sidecar_containers_config = []
        if m.get('SidecarContainersConfig') is not None:
            for k1 in m.get('SidecarContainersConfig'):
                temp_model = main_models.SidecarContainerConfig()
                self.sidecar_containers_config.append(temp_model.from_map(k1))

        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')

        if m.get('SlsLogEnvTags') is not None:
            self.sls_log_env_tags = m.get('SlsLogEnvTags')

        if m.get('StartupProbe') is not None:
            self.startup_probe = m.get('StartupProbe')

        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')

        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')

        return self

