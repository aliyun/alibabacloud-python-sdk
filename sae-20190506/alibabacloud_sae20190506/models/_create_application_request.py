# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

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
        labels: Dict[str, str] = None,
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
        # The ARN of the RAM role required to pull images across Alibaba Cloud accounts. For more information, see [Authorize cross-account access using a RAM role](https://help.aliyun.com/document_detail/223585.html).
        self.acr_assume_role_arn = acr_assume_role_arn
        # The Container Registry Enterprise Edition (ACR Enterprise Edition) instance ID. This parameter is required when **ImageUrl** is a Container Registry Enterprise Edition image.
        self.acr_instance_id = acr_instance_id
        # The AliyunAgent version.
        self.agent_version = agent_version
        # The application description. It cannot exceed 1024 characters.
        self.app_description = app_description
        # The application name. It can contain digits, letters, and hyphens (-). It must start with a letter and cannot end with a hyphen (-). The name cannot exceed 36 characters.
        # 
        # This parameter is required.
        self.app_name = app_name
        # Select micro_service for a microservice application.
        self.app_source = app_source
        # Whether to bind an Elastic IP address (EIP). Valid values:
        # 
        # - **true**: Bind.
        # 
        # - **false**: Do not bind.
        self.associate_eip = associate_eip
        # Whether to automatically configure the network environment. Valid values:
        # 
        # - **true**: SAE automatically configures the network environment when creating an application. The values of **NamespaceId**, **VpcId**, **vSwitchId**, and **SecurityGroupId** are ignored.
        # 
        # - **false**: SAE manually configures the network environment when creating an application.
        # 
        # > If you select **true**, other **NamespaceId** values passed are ignored.
        self.auto_config = auto_config
        # The base application ID.
        self.base_app_id = base_app_id
        # The image start command. This command must be an executable object that exists in the container. Example:
        # 
        # ```
        # command:
        #       - echo
        #       - abc
        #       - >
        #       - file0
        # ```
        # 
        # Based on the example, Command="echo" and `CommandArgs=["abc", ">", "file0"]`.
        # 
        # >Notice: 
        # 
        # This option is required when PackageType is DotnetZip.
        self.command = command
        # The image start command parameters. These are the parameters required by the **Command** parameter. Format:
        # 
        # `["a","b"]`
        # 
        # In the example, `CommandArgs=["abc", ">", "file0"]`. Convert `["abc", ">", "file0"]` to a string type, with the format as a JSON array. If this parameter is not needed, do not specify it.
        # >Notice: This option is required when PackageType is DotnetZip.
        self.command_args = command_args
        # The **ConfigMap** mount description. Use configuration items created on the namespace configuration item page to inject configuration information into the container. Parameter description:
        # 
        # - **configMapId**: The ConfigMap instance ID. Obtain it by calling the [ListNamespacedConfigMaps](https://help.aliyun.com/document_detail/176917.html) API operation.
        # 
        # - **key**: The key value.
        # 
        # > You can mount all keys by passing the `sae-sys-configmap-all` parameter.
        # 
        # - **mountPath**: The mount path.
        self.config_map_mount_desc = config_map_mount_desc
        # The CPU required for each instance, in millicores. It cannot be 0. Currently, only the following defined specifications are supported:
        # 
        # - **500**
        # 
        # - **1000**
        # 
        # - **2000**
        # 
        # - **4000**
        # 
        # - **8000**
        # 
        # - **16000**
        # 
        # - **32000**
        self.cpu = cpu
        # Custom Host mapping within the container. Valid values:
        # 
        # - **hostName**: The domain name or hostname.
        # 
        # - **ip**: The IP address.
        self.custom_host_alias = custom_host_alias
        # The custom image type. If it is not a custom image, set it to an empty string:
        # 
        # - internet: Public network image.
        # 
        # - intranet: Private network image.
        self.custom_image_network_type = custom_image_network_type
        # Whether to deploy immediately. Valid values:
        # 
        # - **true**: Default value. Deploy immediately.
        # 
        # - **false**: Deploy later.
        self.deploy = deploy
        # The disk storage size, in GB.
        self.disk_size = disk_size
        # The version number of the .NET framework:
        # 
        # - .NET 3.1
        # 
        # - .NET 5.0
        # 
        # - .NET 6.0
        # 
        # - .NET 7.0
        # 
        # - .NET 8.0
        self.dotnet = dotnet
        # The application runtime environment version in the HSF framework, such as the Ali-Tomcat container.
        self.edas_container_version = edas_container_version
        # Shared temporary storage configuration.
        self.empty_dir_desc = empty_dir_desc
        # Whether to enable the CPU Burst feature:
        # 
        # - true: Enable.
        # 
        # - false: Do not enable.
        self.enable_cpu_burst = enable_cpu_burst
        # Enable application monitoring for non-Java applications based on eBPF technology. Valid values:
        # 
        # - **true**: Enable.
        # 
        # - **false**: Disable. Default value.
        self.enable_ebpf = enable_ebpf
        # Whether to reuse the namespace Agent version configuration.
        self.enable_namespace_agent_version = enable_namespace_agent_version
        # Whether to reuse the namespace SLS log configuration.
        self.enable_namespace_sls_config = enable_namespace_sls_config
        # Whether to enable new ARMS features:
        # 
        # - true: Enable.
        # 
        # - false: Do not enable.
        self.enable_new_arms = enable_new_arms
        # Whether to enable Prometheus custom metric collection.
        self.enable_prometheus = enable_prometheus
        # Whether to enable Sidecar resource isolation:
        # 
        # - true: Enable isolation.
        # 
        # - false: Do not enable isolation.
        self.enable_sidecar_resource_isolated = enable_sidecar_resource_isolated
        # Container environment variable parameters. Support custom configurations or referencing configuration items. To reference a configuration item, create a ConfigMap instance first. For more information, see [CreateConfigMap](https://help.aliyun.com/document_detail/176914.html). Valid values:
        # 
        # - Custom configuration
        # 
        #   - **name**: The environment variable name.
        # 
        #   - **value**: The environment variable value. This has a higher priority than valueFrom.
        # 
        # - Reference configuration item (valueFrom)
        # 
        #   - **name**: The environment variable name. You can reference a single key or all keys. To reference all keys, enter `sae-sys-configmap-all-<configuration item name>`, for example, `sae-sys-configmap-all-test1`.
        # 
        #   - **valueFrom**: The environment variable reference. Set this to `configMapRef`.
        # 
        #     - **configMapId**: The configuration item ID.
        # 
        #     - **key**: The key. If you reference all key-values, do not set this field.
        self.envs = envs
        self.gpu_config = gpu_config
        # K8s Headless Service service discovery.
        # 
        # - serviceName: The service name.
        # 
        # - namespaceId: The namespace ID.
        self.headless_pvtz_discovery_svc = headless_pvtz_discovery_svc
        # The Nginx version.
        # 
        # - nginx 1.20
        # 
        # - nginx 1.22
        # 
        # - nginx 1.24
        # 
        # - nginx 1.26
        # 
        # - nginx 1.28
        self.html = html
        # The ID of the corresponding secret.
        self.image_pull_secrets = image_pull_secrets
        # The image address. This parameter is required when **Package Type** is **Image**.
        self.image_url = image_url
        # Initialization container configuration.
        self.init_containers_config = init_containers_config
        # Whether it is a stateful application.
        self.is_stateful = is_stateful
        # JAR package startup parameters for the application. The application\\"s default start command is: `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`
        self.jar_start_args = jar_start_args
        # JAR package startup options for the application. The application\\"s default start command is: `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`
        self.jar_start_options = jar_start_options
        # The JDK version that the deployment package depends on. Supported versions:
        # 
        # - **Open JDK 8**
        # 
        # - **Open JDK 7**
        # 
        # - **Dragonwell 11**
        # 
        # - **Dragonwell 8**
        # 
        # - **openjdk-8u191-jdk-alpine3.9**
        # 
        # - **openjdk-7u201-jdk-alpine3.9**
        # 
        # This parameter is not supported when **Package Type** is **Image**.
        self.jdk = jdk
        # The summary configuration for collecting logs to Kafka. Valid values:
        # 
        # - **kafkaEndpoint**: The service registration address for the Kafka API.
        # 
        # - **kafkaInstanceId**: The Kafka instance ID.
        # 
        # - **kafkaConfigs**: The summary configuration for single or multiple logs. For valid values, see the **kafkaConfigs** request parameter in this topic.
        self.kafka_configs = kafka_configs
        self.labels = labels
        # Container health check. Containers that fail the health check are shut down and recovered. Supported methods:
        # 
        # - **exec**: For example, `{"exec":{"command":["sh","-c","cat/home/admin/start.sh"]},"initialDelaySeconds":30,"periodSeconds":30,"timeoutSeconds":2}`
        # 
        # - **httpGet**: For example, `{"httpGet":{"path":"/","port":18091,"scheme":"HTTP","isContainKeyWord":true,"keyWord":"SAE"},"initialDelaySeconds":11,"periodSeconds":10,"timeoutSeconds":1}`
        # 
        # - **tcpSocket**: For example, `{"tcpSocket":{"port":18091},"initialDelaySeconds":11,"periodSeconds":10,"timeoutSeconds":1}`
        # 
        # > Select only one method for the health check.
        # 
        # Parameter description:
        # 
        # - **exec.command**: Set the health check command.
        # 
        # - **httpGet.path**: The access path.
        # 
        # - **httpGet.scheme**: **HTTP** or **HTTPS**.
        # 
        # - **httpGet.isContainKeyWord**: **true** means the keyword is included, **false** means the keyword is not included. If this field is missing, advanced features are not used.
        # 
        # - **httpGet.keyWord**: The custom keyword. Do not omit the **isContainKeyWord** field when using it.
        # 
        # - **tcpSocket.port**: The port for TCP connection detection.
        # 
        # - **initialDelaySeconds**: Set the health check delay detection time. Default is 10 seconds.
        # 
        # - **periodSeconds**: Set the health check period. Default is 30 seconds.
        # 
        # - **timeoutSeconds**: Set the health check timeout duration. Default is 1 second. If you set it to 0 or do not set it, the default timeout is 1 second.
        self.liveness = liveness
        self.loki_configs = loki_configs
        # The memory required for each instance, in MB. It cannot be 0. It has a one-to-one correspondence with CPU. Currently, only the following defined specifications are supported:
        # 
        # - **1024**: Corresponds to 500 millicores and 1000 millicores CPU.
        # 
        # - **2048**: Corresponds to 500, 1000 millicores, and 2000 millicores CPU.
        # 
        # - **4096**: Corresponds to 1000, 2000 millicores, and 4000 millicores CPU.
        # 
        # - **8192**: Corresponds to 2000, 4000 millicores, and 8000 millicores CPU.
        # 
        # - **12288**: Corresponds to 12000 millicores CPU.
        # 
        # - **16384**: Corresponds to 4000, 8000 millicores, and 16000 millicores CPU.
        # 
        # - **24576**: Corresponds to 12000 millicores CPU.
        # 
        # - **32768**: Corresponds to 16000 millicores CPU.
        # 
        # - **65536**: Corresponds to 8000, 16000, and 32000 millicores CPU.
        # 
        # - **131072**: Corresponds to 32000 millicores CPU.
        self.memory = memory
        # Select the Nacos registry. Valid values:
        # 
        # - **0**: SAE built-in Nacos.
        # 
        # - **1**: User-managed Nacos.
        # 
        # - **2**: MSE Professional Edition Nacos.
        self.micro_registration = micro_registration
        # The registry configuration information.
        self.micro_registration_config = micro_registration_config
        # Configure microservice administration features.
        # 
        # - Whether to enable microservice administration (enable):
        # 
        #   - true: Enable.
        # 
        #   - false: Do not enable.
        # 
        # - Configure graceful start and graceful shutdown (mseLosslessRule):
        # 
        #   - delayTime: The delay time.
        # 
        #   - enable: Whether to enable the graceful start feature. true means enabled, false means not enabled.
        # 
        #   - notice: Whether to enable the notification feature. true means enabled, false means enabled.
        # 
        #   - warmupTime: The duration of traffic prefetch, in seconds.
        self.microservice_engine_config = microservice_engine_config
        # Do not configure this field; configure **NasConfigs** instead. The NAS mount description. If the configuration has not changed during deployment, you do not need to set this parameter (that is, the request does not need to include the **MountDesc** field). To clear the NAS configuration, set the value of this field to an empty string in the request (that is, the value of the **MountDesc** field in the request is "").
        self.mount_desc = mount_desc
        # Do not configure this field; configure **NasConfigs** instead. The NAS mount target within the application VPC. If the configuration has not changed during deployment, you do not need to set this parameter (that is, the request does not need to include the **MountHost** field). To clear the NAS configuration, set the value of this field to an empty string in the request (that is, the value of the **MountHost** field in the request is "").
        self.mount_host = mount_host
        # The SAE namespace ID. Only namespaces with names consisting of lowercase letters and hyphens (-) are supported. The name must start with a letter. Obtain the namespace by calling the [DescribeNamespaceList](https://help.aliyun.com/document_detail/126547.html) API operation.
        self.namespace_id = namespace_id
        # The configuration for mounting NAS. Valid values:
        # 
        # - **mountPath**: The container mount path.
        # 
        # - **readOnly**: If the value is **false**, it indicates read and write permission.
        # 
        # - **nasId**: The NAS ID.
        # 
        # - **mountDomain**: The container mount target address. For more information, see [DescribeMountTargets](https://help.aliyun.com/document_detail/62626.html).
        # 
        # - **nasPath**: The relative file directory of NAS.
        self.nas_configs = nas_configs
        # Do not configure this field; configure **NasConfigs** instead. The ID of the mounted NAS. It must be in the same region as the cluster. It must have available mount target creation quotas, or its mount target must already be on a vSwitch within the VPC. If you do not specify this parameter and the **mountDescs** field exists, the system automatically purchases a NAS and mounts it to a vSwitch within the VPC by default.
        # 
        # If the configuration has not changed during deployment, you do not need to set this parameter (that is, the request does not need to include the **NASId** field). To clear the NAS configuration, set the value of this field to an empty string in the request (that is, the value of the **NASId** field in the request is "").
        self.nas_id = nas_id
        # The application version:
        # 
        # - lite: Lightweight Edition
        # 
        # - std: Standard Edition
        # 
        # - pro: Professional Edition
        self.new_sae_version = new_sae_version
        # Set the identity authentication service RAM role.
        # 
        # > Create an OpenID Connect (OIDC) identity provider and an identity provider role in the same region beforehand. For more information, see<props="china">[Create an OIDC identity provider](https://help.aliyun.com/zh/ram/developer-reference/api-ims-2019-08-15-createoidcprovider?spm=a2c4g.11186623.help-menu-28625.d_4_1_0_3_2_7.7f0443efmdpxa3) and[Create a role SSO identity provider](https://help.aliyun.com/zh/ram/developer-reference/api-ims-2019-08-15-createsamlprovider?spm=a2c4g.11186623.help-menu-28625.d_4_1_0_3_2_2.632244b1s8QbQt)<props="intl">[Create an OIDC identity provider](https://www.alibabacloud.com/help/zh/ram/developer-reference/api-ims-2019-08-15-createoidcprovider) and[Create a role SSO identity provider](https://www.alibabacloud.com/help/zh/ram/developer-reference/api-ims-2019-08-15-createsamlprovider).
        self.oidc_role_name = oidc_role_name
        # The AccessKey ID for OSS read and write operations.
        self.oss_ak_id = oss_ak_id
        # The AccessKey Secret for OSS read and write operations.
        self.oss_ak_secret = oss_ak_secret
        # OSS mount description. Parameter description:
        # 
        # - **bucketName**: The Bucket name.
        # 
        # - **bucketPath**: The directory or OSS object you created in OSS. If the OSS mount directory does not exist, an exception is triggered.
        # 
        # - **mountPath**: The container path in SAE. If the path exists, it is overwritten. If the path does not exist, it is created.
        # 
        # - **readOnly**: Whether the container path has read permission for the mounted directory resource. Valid values:
        # 
        #   - **true**: Read-only permission.
        # 
        #   - **false**: Read and write permission.
        self.oss_mount_descs = oss_mount_descs
        # The application package type. Valid values:
        # 
        # - If you deploy with Java, supported types are **FatJar**, **War**, and **Image**.
        # 
        # - If you deploy with PHP, supported types are:
        # 
        #   - **PhpZip**
        # 
        #   - **IMAGE_PHP_5_4**
        # 
        #   - **IMAGE_PHP_5_4_ALPINE**
        # 
        #   - **IMAGE_PHP_5_5**
        # 
        #   - **IMAGE_PHP_5_5_ALPINE**
        # 
        #   - **IMAGE_PHP_5_6**
        # 
        #   - **IMAGE_PHP_5_6_ALPINE**
        # 
        #   - **IMAGE_PHP_7_0**
        # 
        #   - **IMAGE_PHP_7_0_ALPINE**
        # 
        #   - **IMAGE_PHP_7_1**
        # 
        #   - **IMAGE_PHP_7_1_ALPINE**
        # 
        #   - **IMAGE_PHP_7_2**
        # 
        #   - **IMAGE_PHP_7_2_ALPINE**
        # 
        #   - **IMAGE_PHP_7_3**
        # 
        #   - **IMAGE_PHP_7_3_ALPINE**
        # 
        # - If you deploy with Python, supported types are **PythonZip** and **Image**.
        # 
        # - If you deploy with .NET Core, supported types are **DotnetZip** and **Image**.
        # 
        #   > When you select DotnetZip, Dotnet is the version number of the .NET Core environment. Supported versions are .NET 3.1, .NET 5.0, .NET 6.0, .NET 7.0, and .NET 8.0. The Dotnet, Command, and CommandArgs options are required.
        # 
        # This parameter is required.
        self.package_type = package_type
        # The URL of the deployment package. This parameter is required when **Package Type** is **FatJar**, **War**, or **PythonZip**.
        self.package_url = package_url
        # The version number of the deployment package. This parameter is required when **Package Type** is **FatJar**, **War**, or **PythonZip**.
        self.package_version = package_version
        # The PHP version that the PHP deployment package depends on. Images do not support this.
        self.php = php
        # The mount path for PHP application monitoring. Ensure that the PHP server loads the configuration file from this path. You do not need to focus on the configuration content; SAE automatically renders the correct configuration file.
        self.php_arms_config_location = php_arms_config_location
        # The content of the PHP configuration file.
        self.php_config = php_config
        # The mount path for PHP application startup configuration. Ensure that the PHP server uses this configuration file to start.
        self.php_config_location = php_config_location
        # The script to execute after the container starts. A script is triggered immediately after the container is created. Format: `{"exec":{"command":["cat","/etc/group"]}}`
        self.post_start = post_start
        # The script to execute before the container stops. A script is triggered before the container is deleted. Format: `{"exec":{"command":["cat","/etc/group"]}}`
        self.pre_stop = pre_stop
        # The technology stack language for creating the application. Valid values:
        # 
        # - **java**: Java language.
        # 
        # - **php**: PHP language.
        # 
        # - **python**: Python language.
        # 
        # - **dotnet**: .NET Core language.
        # 
        # - **other**: Multi-language, such as C++, Go, and Node.js.
        self.programming_language = programming_language
        # Enable K8s Service service discovery. Valid values:
        # 
        # - **serviceName**: The service name. Format: `custom-namespace ID`. The suffix `-namespace ID` cannot be customized; specify it based on the application\\"s namespace. For example, if you select the default namespace in the China (Beijing) region, it is `-cn-beijing-default`.
        # 
        # - **namespaceId**: The namespace ID.
        # 
        # - **portProtocols**: The port and protocol. The port range is [1, 65535]. Supported protocols are **TCP** and **UDP**.
        # 
        # - portAndProtocol: The port and protocol. The port range is [1, 65535]. Supported protocols are TCP and **UDP**. **portProtocols** is recommended. If **portProtocols** is set, only **portProtocols** takes effect.
        # 
        # - **enable**: Enable K8s Service service discovery.
        self.pvtz_discovery_svc = pvtz_discovery_svc
        # The Python environment. Supports **PYTHON 3.9.15**.
        self.python = python
        # Custom installation of module dependencies. By default, the system installs dependencies defined in requirements.txt in the root directory. If you do not configure or customize packages, you can specify the dependencies to install.
        self.python_modules = python_modules
        # Application startup status check. Containers that fail multiple health checks are shut down and restarted. Containers that do not pass the health check will not receive SLB traffic. Supported methods are **exec**, **httpGet**, and **tcpSocket**. For examples, see the **Liveness** parameter.
        # 
        # > Select only one method for the health check.
        self.readiness = readiness
        # The initial number of instances.
        # 
        # This parameter is required.
        self.replicas = replicas
        # The resource type. Supports NULL (default), default, and haiguang (Haiguang server) types.
        self.resource_type = resource_type
        # The SAE version. Supported versions:
        # 
        # - **v1**
        # 
        # - **v2**
        self.sae_version = sae_version
        # The **Secret** mount description. Use secrets created on the namespace secret page to inject secret information into the container. Parameter description:
        # 
        # - **secretId**: The secret instance ID. Obtain it by calling the ListSecrets API operation.
        # 
        # - **key**: The key value.
        # 
        # > You can mount all keys by passing the `sae-sys-secret-all` parameter.
        # 
        # - **mountPath**: The mount path.
        self.secret_mount_desc = secret_mount_desc
        # The security group ID.
        self.security_group_id = security_group_id
        # The grayscale tags for application configuration.
        self.service_tags = service_tags
        # Container configuration information.
        self.sidecar_containers_config = sidecar_containers_config
        # The configuration for collecting logs to Simple Log Service (SLS).
        # 
        # - Use SLS resources automatically created by SAE: `[{"logDir":"","logType":"stdout"},{"logDir":"/tmp/a.log"}]`.
        # 
        # - Use custom SLS resources: `[{"projectName":"test-sls","logType":"stdout","logDir":"","logstoreName":"sae","logtailName":""},{"projectName":"test","logDir":"/tmp/a.log","logstoreName":"sae","logtailName":""}]`.
        # 
        # Parameter description:
        # 
        # - **projectName**: The name of the Project on SLS.
        # 
        # - **logDir**: The log path.
        # 
        # - **logType**: The log type. **stdout** indicates container standard output logs; you can set only one such entry. If you do not set this, the system collects file logs.
        # 
        # - **logstoreName**: The name of the Logstore on SLS.
        # 
        # - **logtailName**: The name of the Logtail on SLS. If you do not specify this, the system creates a new Logtail.
        # 
        # If the SLS collection configuration has not changed during multiple deployments, you do not need to set this parameter (that is, the request does not need to include the **SlsConfigs** field). If you no longer need the SLS collection feature, set the value of this field to an empty string in the request (that is, the value of the **SlsConfigs** field in the request is "").
        # 
        # > Projects automatically created with an application are deleted when the application is deleted. Therefore, when selecting an existing Project, do not select a Project automatically created by SAE.
        self.sls_configs = sls_configs
        # SLS log tags.
        self.sls_log_env_tags = sls_log_env_tags
        # Enable application startup probes.
        # 
        # - Successful check: Indicates that the application started successfully. If you configured Liveness and Readiness checks, the system performs Liveness and Readiness checks after the application starts successfully.
        # 
        # - Failed check: Indicates that the application failed to start. The system reports an exception and automatically restarts the application.
        # 
        # > * Supported methods are exec, httpGet, and tcpSocket. For examples, see the Liveness parameter.
        # >
        # > * Select only one method for the health check.
        self.startup_probe = startup_probe
        # The graceful shutdown timeout duration. Default is 30 seconds. Valid values are 1 to 300.
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # The time zone. Default is **Asia/Shanghai**.
        self.timezone = timezone
        # Tomcat file configuration. Set to "" or "{}" to delete the configuration:
        # 
        # - **port**: The port range is 1024 to 65535. Ports less than 1024 require root permissions to operate. Because the container is configured with Admin permissions, specify a port greater than 1024. If you do not configure this, the default is 8080.
        # 
        # - **contextPath**: The access path. Default is the root directory "/".
        # 
        # - **maxThreads**: Configure the connection pool size. Default is 400.
        # 
        # - uriEncoding: The encoding format for Tomcat, including **UTF-8**, **ISO-8859-1**, **GBK**, and **GB2312**. If you do not set this, the default is **ISO-8859-1**.
        # 
        # - **useBodyEncodingForUri**: Whether to use **BodyEncoding for URL**. Default is **true**.
        self.tomcat_config = tomcat_config
        # The virtual switch (vSwitch) where the application instance\\"s Elastic Network Interface (ENI) is located. This vSwitch must be within the specified VPC. This vSwitch also has a binding relationship with the SAE namespace. If you do not specify this parameter, the system uses the vSwitch ID bound to the namespace by default.
        self.v_switch_id = v_switch_id
        # The VPC corresponding to the SAE namespace. In SAE, a namespace can only correspond to one VPC, and you cannot change it. The first time you create an SAE application in a namespace, a binding relationship forms. Multiple namespaces can correspond to one VPC. If you do not specify this parameter, the system uses the VPC ID bound to the namespace by default.
        self.vpc_id = vpc_id
        # Set the startup command for WAR package deployed applications. The procedure is the same as configuring the startup command for image deployments. For more information, see [Set the startup command](https://help.aliyun.com/document_detail/96677.html).
        self.war_start_options = war_start_options
        # The Tomcat version that the WebContainer deployment package depends on. Supported versions:
        # 
        # - **apache-tomcat-7.0.91**
        # 
        # - **apache-tomcat-8.5.42**
        # 
        # This parameter is not supported when **Package Type** is **Image**.
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

        if self.labels is not None:
            result['Labels'] = self.labels

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

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

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

