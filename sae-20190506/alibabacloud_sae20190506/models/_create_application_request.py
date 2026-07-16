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
        rasp_config: main_models.CreateApplicationRequestRaspConfig = None,
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
        # The ARN of the RAM role required for cross-account image pulling. For more information, see [Grant permissions across Alibaba Cloud accounts by using a RAM role](https://help.aliyun.com/document_detail/223585.html).
        self.acr_assume_role_arn = acr_assume_role_arn
        # The instance ID of the Container Registry Enterprise instance. This parameter is required when **ImageUrl** is set to a Container Registry Enterprise Edition image.
        self.acr_instance_id = acr_instance_id
        # The AliyunAgent version.
        self.agent_version = agent_version
        # The application description. The description can be up to 1024 characters in length.
        self.app_description = app_description
        # The application name. The name can contain digits, letters, and hyphens (-). The name must start with a letter and cannot end with a hyphen (-). The name can be up to 36 characters in length.
        # 
        # This parameter is required.
        self.app_name = app_name
        # Set this parameter to micro_service to create a microservice application.
        self.app_source = app_source
        # Specifies whether to associate an EIP. Valid values:
        # 
        # - **true**: associate an EIP.
        # - **false**: do not associate an EIP.
        self.associate_eip = associate_eip
        # Specifies whether to automatically configure the network environment. Valid values:
        # 
        # - **true**: SAE automatically configures the network environment when the application is created. The values of **NamespaceId**, **VpcId**, **vSwitchId**, and **SecurityGroupId** are ignored.
        # - **false**: SAE manually configures the network environment when the application is created.
        # 
        # > If this parameter is set to **true**, any other **NamespaceId** value that is passed is ignored.
        self.auto_config = auto_config
        # The base application ID.
        self.base_app_id = base_app_id
        # The command that is used to start the image. The command must be an executable object in the container. Example:
        # 
        # ```
        # command:
        #       - echo
        #       - abc
        #       - >
        #       - file0
        # ```
        # In the preceding example, `Command="echo", CommandArgs=["abc", ">", "file0"]`.
        # 
        # 
        # >Notice: This parameter is required when PackageType is set to DotnetZip.
        self.command = command
        # The arguments of the image startup command. These are the arguments required by the startup command specified in **Command**. Format:
        # 
        # `["a","b"]`
        # 
        # In the preceding example, `CommandArgs=["abc", ">", "file0"]`, where `["abc", ">", "file0"]` must be converted to the String type. The internal format is a JSON array. If this parameter is not required, leave it empty.
        # >Notice: This parameter is required when PackageType is set to DotnetZip.
        self.command_args = command_args
        # The **ConfigMap** mount description. Use a ConfigMap created on the namespace configuration items page to inject configuration information into the container. Parameter description:
        # 
        # - **configMapId**: the ConfigMap instance ID. You can obtain the ID by invoking the [ListNamespacedConfigMaps](https://help.aliyun.com/document_detail/176917.html) operation.
        # - **key**: the key.
        # 
        # > You can mount all keys by passing the `sae-sys-configmap-all` parameter.
        # 
        # - **mountPath**: the mount path.
        self.config_map_mount_desc = config_map_mount_desc
        # The CPU specifications required for each instance, in millicores. This parameter cannot be set to 0. Only the following defined specifications are supported:
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
        # - **hostName**: the domain name or hostname.
        # - **ip**: the IP address.
        self.custom_host_alias = custom_host_alias
        # The custom image type. Set this parameter to an empty string if the image is not a custom image:
        # 
        # - internet: public image
        # - intranet: private image
        self.custom_image_network_type = custom_image_network_type
        # Specifies whether to immediately deploy the application. Valid values:
        # 
        # - **true**: default value. The application is deployed immediately.
        # - **false**: the application is deployed later.
        self.deploy = deploy
        # The disk storage size, in GB.
        self.disk_size = disk_size
        # The version of the .NET framework:
        # 
        # - .NET 3.1
        # - .NET 5.0
        # - .NET 6.0
        # - .NET 7.0
        # - .NET 8.0
        self.dotnet = dotnet
        # The version of the application runtime environment in the HSF framework, such as the Ali-Tomcat container.
        self.edas_container_version = edas_container_version
        # The shared ephemeral storage configuration.
        self.empty_dir_desc = empty_dir_desc
        # Specifies whether to enable the CPU Burst feature:
        # 
        # - true: Enabled.
        # - false: Disabled.
        self.enable_cpu_burst = enable_cpu_burst
        # Specifies whether to enable application monitoring for non-Java applications based on eBPF technology. Valid values:
        # - **true**: enabled.
        # - **false**: disabled. This is the default value.
        self.enable_ebpf = enable_ebpf
        # Specifies whether to reuse the namespace agent version configuration.
        self.enable_namespace_agent_version = enable_namespace_agent_version
        # Specifies whether to reuse the namespace SLS log configuration.
        self.enable_namespace_sls_config = enable_namespace_sls_config
        # Specifies whether to enable the new ARMS feature:
        # 
        # - true: Enabled.
        # - false: Disabled.
        self.enable_new_arms = enable_new_arms
        # Specifies whether to enable Prometheus custom metric collection.
        self.enable_prometheus = enable_prometheus
        # Specifies whether to enable sidecar resource isolation:
        # 
        # - true: Isolated.
        # - false: Not isolated.
        self.enable_sidecar_resource_isolated = enable_sidecar_resource_isolated
        # The container environment variable parameters. You can customize environment variables or reference a ConfigMap. To reference a ConfigMap, create a ConfigMap instance first. For more information, see [CreateConfigMap](https://help.aliyun.com/document_detail/176914.html). Valid values:
        # - Custom configuration
        #     - **name**: the name of the environment variable.
        #     - **value**: the value of the environment variable. This takes priority over valueFrom.
        # - Reference a ConfigMap (valueFrom)
        #     - **name**: the name of the environment variable. You can reference a single key or all keys. To reference all keys, enter `sae-sys-configmap-all-<ConfigMap name>`, such as `sae-sys-configmap-all-test1`.
        #     - **valueFrom**: the environment variable reference. Set the value to `configMapRef`.
        #         - **configMapId**: the ConfigMap ID.
        #         - **key**: the key. If you reference all keys, do not set this field.
        self.envs = envs
        self.gpu_config = gpu_config
        # The K8s Headless Service-based service registration and discovery.
        # - serviceName: the service name.
        # - namespaceId: the namespace ID.
        self.headless_pvtz_discovery_svc = headless_pvtz_discovery_svc
        # The Nginx version.
        # - nginx 1.20
        # - nginx 1.22
        # - nginx 1.24
        # - nginx 1.26
        # - nginx 1.28
        self.html = html
        # The corresponding secret ID.
        self.image_pull_secrets = image_pull_secrets
        # The image address. This parameter is required when **Package Type** is set to **Image**.
        self.image_url = image_url
        # The init container configuration.
        self.init_containers_config = init_containers_config
        # Specifies whether the application is stateful.
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
        # The summary of configurations for log collection to Kafka. Valid values:
        # 
        # - **kafkaEndpoint**: the service registration address of the Kafka API.
        # - **kafkaInstanceId**: the Kafka instance ID.
        # - **kafkaConfigs**: the summary of configurations for one or more log entries. For more information about the valid values, see the **kafkaConfigs** request parameter in this topic.
        self.kafka_configs = kafka_configs
        self.labels = labels
        # The container health check. Containers that fail the health check are shutdown and recovered. The following methods are supported:
        # 
        # - **exec**: for example, `{"exec":{"command":["sh","-c","cat/home/admin/start.sh"]},"initialDelaySeconds":30,"periodSeconds":30,"timeoutSeconds":2}`
        # - **httpGet**: for example, `{"httpGet":{"path":"/","port":18091,"scheme":"HTTP","isContainKeyWord":true,"keyWord":"SAE"},"initialDelaySeconds":11,"periodSeconds":10,"timeoutSeconds":1}`
        # - **tcpSocket**: for example, `{"tcpSocket":{"port":18091},"initialDelaySeconds":11,"periodSeconds":10,"timeoutSeconds":1}`
        # 
        # > You can use only one method for health checks.
        # 
        # Parameter description:
        # 
        # - **exec.command**: the health check command.
        # - **httpGet.path**: the access path.
        # - **httpGet.scheme**: **HTTP** or **HTTPS**.
        # - **httpGet.isContainKeyWord**: **true** indicates that the keyword is included. **false** indicates that the keyword is not included. If this field is missing, the advanced feature is not used.
        # - **httpGet.keyWord**: the custom keyword. The **isContainKeyWord** field must be present when this field is used.
        # - **tcpSocket.port**: the port for TCP connection detection.
        # - **initialDelaySeconds**: the health check delay detection time. Default value: 10. Unit: seconds.
        # - **periodSeconds**: the health check period. Default value: 30. Unit: seconds.
        # - **timeoutSeconds**: the health check timeout period. Default value: 1. Unit: seconds. If this parameter is set to 0 or is not set, the default timeout period is 1 second.
        self.liveness = liveness
        self.loki_configs = loki_configs
        # The memory required for each instance, in MB. This parameter cannot be set to 0. The memory has a one-to-one mapping with CPU. Only the following defined specifications are supported:
        # - **1024**: corresponds to 500 and 1000 millicores of CPU.
        # - **2048**: corresponds to 500, 1000, and 2000 millicores of CPU.
        # - **4096**: corresponds to 1000, 2000, and 4000 millicores of CPU.
        # - **8192**: corresponds to 2000, 4000, and 8000 millicores of CPU.
        # - **12288**: corresponds to 12000 millicores of CPU.
        # - **16384**: corresponds to 4000, 8000, and 16000 millicores of CPU.
        # - **24576**: corresponds to 12000 millicores of CPU.
        # - **32768**: corresponds to 16000 millicores of CPU.
        # - **65536**: corresponds to 8000, 16000, and 32000 millicores of CPU.
        # - **131072**: corresponds to 32000 millicores of CPU.
        self.memory = memory
        # Specifies the Nacos registry. Valid values:
        # - **0**: SAE built-in Nacos.
        # - **1**: self-managed Nacos.
        # - **2**: MSE commercial edition Nacos.
        self.micro_registration = micro_registration
        # The registry configuration.
        self.micro_registration_config = micro_registration_config
        # Configures the microservice governance feature.
        # 
        # - Specifies whether to enable microservice governance (enable):
        # 
        #    - true: Enabled.
        # 
        #   - false: Disabled.
        # 
        # - Configures lossless online/offline (mseLosslessRule):
        # 
        #   - delayTime: the delay time.
        # 
        #   - enable: specifies whether to enable the lossless online feature. true indicates enabled. false indicates disabled.
        # 
        #   - notice: specifies whether to enable the notification feature. true indicates enabled. false indicates disabled.
        # 
        #   - warmupTime: the warm-up duration for traffic ramping, in seconds.
        self.microservice_engine_config = microservice_engine_config
        # We recommend that you do not set this parameter. Set **NasConfigs** instead. The NAS mount description. If the configuration does not change during deployment, you do not need to set this parameter (that is, the **MountDesc** field does not need to be included in the request). To clear the NAS configuration, set the value of this field to an empty string (that is, set the value of the **MountDesc** field to "" in the request).
        self.mount_desc = mount_desc
        # We recommend that you do not set this parameter. Set **NasConfigs** instead. The mount target of the NAS file system in the VPC of the application. If the configuration does not change during deployment, you do not need to set this parameter (that is, the **MountHost** field does not need to be included in the request). To clear the NAS configuration, set the value of this field to an empty string (that is, set the value of the **MountHost** field to "" in the request).
        self.mount_host = mount_host
        # The SAE namespace ID. Only namespaces whose names contain lowercase letters and hyphens (-) are supported. The name must start with a letter.
        # You can obtain namespaces by calling the [DescribeNamespaceList](https://help.aliyun.com/document_detail/126547.html) operation.
        self.namespace_id = namespace_id
        # The NAS mount configuration. Valid values:
        # 
        # - **mountPath**: the container mount path.
        # - **readOnly**: set to **false** to grant read and write permission.
        # - **nasId**: the NAS ID.
        # - **mountDomain**: the container mount target address. For more information, see [DescribeMountTargets](https://help.aliyun.com/document_detail/62626.html).
        # - **nasPath**: the NAS relative file directory.
        self.nas_configs = nas_configs
        # We recommend that you do not set this parameter. Set **NasConfigs** instead. The ID of the mounted NAS file system. The NAS file system must be in the same region as the cluster. The NAS file system must have available mount target creation quota, or its mount target must already be on a vSwitch in the VPC. If this parameter is left empty and the **mountDescs** field exists, a NAS file system is automatically purchased and mounted to a vSwitch in the VPC.
        # 
        # If the configuration does not change during deployment, you do not need to set this parameter (that is, the **NASId** field does not need to be included in the request). To clear the NAS configuration, set the value of this field to an empty string (that is, set the value of the **NASId** field to "" in the request).
        self.nas_id = nas_id
        # The application version:
        # 
        # - lite: Lite Edition
        # - std: Standard Edition
        # - pro: Professional Edition
        self.new_sae_version = new_sae_version
        # Specifies the RAM role for identity authentication.
        # > Create an OIDC identity provider and an identity provider role in the same region in advance. For more information, see <props="china">[CreateOIDCProvider](https://www.alibabacloud.com/help/en/ram/developer-reference/api-ims-2019-08-15-createoidcprovider) and [CreateSAMLProvider](https://www.alibabacloud.com/help/en/ram/developer-reference/api-ims-2019-08-15-createsamlprovider)<props="intl">[CreateOIDCProvider](https://www.alibabacloud.com/help/zh/ram/developer-reference/api-ims-2019-08-15-createoidcprovider) and [CreateSAMLProvider](https://www.alibabacloud.com/help/zh/ram/developer-reference/api-ims-2019-08-15-createsamlprovider).
        self.oidc_role_name = oidc_role_name
        # The AccessKey ID for OSS read and write operations.
        self.oss_ak_id = oss_ak_id
        # The AccessKey Secret for OSS read and write operations.
        self.oss_ak_secret = oss_ak_secret
        # The OSS mount description. Parameter description:
        # 
        # - **bucketName**: the bucket name.
        # - **bucketPath**: the folder or object that you created in OSS. If the OSS mount folder does not exist, an exception is triggered.
        # - **mountPath**: the container path in SAE. If the path already exists, it is an overwrite relationship. If the path does not exist, it is created.
        # - **readOnly**: specifies whether the container path has read-only permission on the mounted folder resources. Valid values:
        #     - **true**: read-only permission.
        #     - **false**: read and write permission.
        self.oss_mount_descs = oss_mount_descs
        # The type of the application deployment package. Valid values:
        # 
        # - If you use Java for deployment, **FatJar**, **War**, and **Image** are supported.
        # - If you use PHP for deployment, the following types are supported:
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
        # - If you use Python for deployment, **PythonZip** and **Image** are supported.
        # 
        # - If you use .NET Core for deployment, **DotnetZip** and **Image** are supported.
        #   > 
        #   > When DotnetZip is selected, Dotnet specifies the version of the .NET Core runtime. .NET 3.1, .NET 5.0, .NET 6.0, .NET 7.0, and .NET 8.0 are supported. The Dotnet, Command, and CommandArgs parameters are required.
        # 
        # This parameter is required.
        self.package_type = package_type
        # The address of the deployment package. This parameter is required when **Package Type** is set to **FatJar**, **War**, or **PythonZip**.
        self.package_url = package_url
        # The version of the deployment package. This parameter is required when **Package Type** is set to **FatJar**, **War**, or **PythonZip**.
        self.package_version = package_version
        # The PHP version on which the deployment package depends. Not supported for images.
        self.php = php
        # The mount path for PHP application monitoring. Make sure that the PHP server loads the configuration file from this path.
        # You do not need to manage the configuration content. SAE automatically renders the correct configuration file.
        self.php_arms_config_location = php_arms_config_location
        # The content of the PHP configuration file.
        self.php_config = php_config
        # The mount path for the PHP application startup configuration. Make sure that the PHP server uses this configuration file to start.
        self.php_config_location = php_config_location
        # The script that is run after the container is started. A script is triggered and run immediately after the container is created. Format: `{"exec":{"command":["cat","/etc/group"]}}`
        self.post_start = post_start
        # The script that is run before the container is stopped. A script is triggered and run before the container is deleted. Format: `{"exec":{"command":["cat","/etc/group"]}}`
        self.pre_stop = pre_stop
        # The programming language of the technology stack used to create the application. Valid values:
        # 
        # - **java**: Java.
        # - **php**: PHP.
        # - **python**: Python.
        # - **dotnet**: .NET Core.
        # - **other**: multiple languages, such as C++, Go, and Node.js.
        self.programming_language = programming_language
        # Enables K8s Service-based service registration and discovery. Valid values:
        # 
        # - **serviceName**: the service name. Format: `custom name-namespace ID`. The suffix `-namespace ID` cannot be customized and must be set based on the namespace of the application. For example, if you select the default namespace in the China (Beijing) region, the suffix is `-cn-beijing-default`.
        # - **namespaceId**: the namespace ID.
        # - **portProtocols**: the port and protocol. Valid port values: [1,65535]. Valid protocol values: **TCP** and **UDP**.
        # - **portAndProtocol**: the port and protocol. Valid port values: [1,65535]. Valid protocol values: **TCP** and **UDP**. **portProtocols is recommended. If portProtocols is set, only portProtocols takes effect**.
        # - **enable**: enables K8s Service-based service registration and discovery.
        self.pvtz_discovery_svc = pvtz_discovery_svc
        # The Python environment. **PYTHON 3.9.15** is supported.
        self.python = python
        # The custom installation module dependencies. By default, the dependencies defined in the requirements.txt file in the root folder are installed. If the file is not configured or you need custom packages, specify the dependencies to install.
        self.python_modules = python_modules
        self.rasp_config = rasp_config
        # The application startup status check. Containers that fail multiple health checks are shut down and restarted. Containers that do not pass the health check do not receive SLB traffic. The **exec**, **httpGet**, and **tcpSocket** methods are supported. For specific examples, see the **Liveness** parameter.
        # 
        # > You can use only one method for health checks.
        self.readiness = readiness
        # The initial number of instances.
        # 
        # This parameter is required.
        self.replicas = replicas
        # The resource type. Valid values: NULL (default), default, and haiguang (Hygon server).
        self.resource_type = resource_type
        # The SAE version. Valid values:
        # 
        # - **v1**
        # - **v2**
        self.sae_version = sae_version
        # The **Secret** mount description. Use a secret created on the namespace secrets page to inject sensitive information into the container. Parameter description:
        # 
        # - **secretId**: the secret instance ID. You can obtain the ID by calling the ListSecrets operation.
        # - **key**: the key.
        # 
        # > You can mount all keys by passing the `sae-sys-secret-all` parameter.
        # 
        # - **mountPath**: the mount path.
        self.secret_mount_desc = secret_mount_desc
        # The security group ID.
        self.security_group_id = security_group_id
        # The canary release tags configured for the application.
        self.service_tags = service_tags
        # The sidecar container configuration.
        self.sidecar_containers_config = sidecar_containers_config
        # The configurations for log collection to Simple Log Service.
        # 
        # - Use SLS resources that are automatically created by SAE: `[{"logDir":"","logType":"stdout"},{"logDir":"/tmp/a.log"}]`.
        # - Use custom SLS resources: `[{"projectName":"test-sls","logType":"stdout","logDir":"","logstoreName":"sae","logtailName":""},{"projectName":"test","logDir":"/tmp/a.log","logstoreName":"sae","logtailName":""}]`.
        # 
        # Parameter description:
        # 
        # - **projectName**: the Project name in Simple Log Service.  
        # - **logDir**: the log path.
        # - **logType**: the log type. **stdout** indicates container standard output logs. You can configure only one entry for this type. If this parameter is not set, file logs are collected.
        # - **logstoreName**: the Logstore name in Simple Log Service.
        # - **logtailName**: the Logtail name in Simple Log Service. If this parameter is not specified, a new Logtail is created.
        # 
        # If the SLS collection configuration does not change during multiple deployments, you do not need to set this parameter (that is, the **SlsConfigs** field does not need to be included in the request). If you no longer need the SLS collection feature, set the value of this field to an empty string (that is, set the value of the **SlsConfigs** field to "" in the request).
        # 
        # > Projects that are automatically created with the application are deleted when the application is deleted. Therefore, do not select a project that is automatically created by SAE when you select an existing project.
        self.sls_configs = sls_configs
        # sls log tags
        self.sls_log_env_tags = sls_log_env_tags
        # Enables the application startup probe.
        # 
        # - Check succeeded: indicates that the application started successfully. If you configured Liveness and Readiness checks, they are performed after the application starts successfully.
        # - Check failed: indicates that the application failed to start. An exception is reported and the application is automatically restarted.
        # > 
        # > - The exec, httpGet, and tcpSocket methods are supported. For specific examples, see the Liveness parameter.
        # > - You can use only one method for health checks.
        self.startup_probe = startup_probe
        # The timeout period for graceful shutdown. Default value: 30. Unit: seconds. Valid values: 1 to 300.
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # The time zone. Default value: **Asia/Shanghai**.
        self.timezone = timezone
        # The Tomcat configuration. Set this parameter to "" or "{}" to delete the configuration:
        # 
        # - **port**: the port number. Valid values: 1024 to 65535. Ports less than 1024 require root permissions. Because the container is configured with admin permissions, specify a port greater than 1024. Default value: 8080.
        # - **contextPath**: the access path. Default value: root directory "/".
        # - **maxThreads**: the maximum number of connections in the connection pool. Default value: 400.
        # - **uriEncoding**: the encoding format of Tomcat. Valid values: **UTF-8**, **ISO-8859-1**, **GBK**, and **GB2312**. Default value: **ISO-8859-1**.
        # - **useBodyEncodingForUri**: specifies whether to use **BodyEncoding for URL**. Default value: **true**.
        self.tomcat_config = tomcat_config
        # The vSwitch where the elastic network interface controller (NIC) of the application instance resides. The vSwitch must be in the specified VPC. The vSwitch also has a binding relationship with the SAE namespace. If you leave this parameter empty, the vSwitch attached to the namespace is used by default.
        self.v_switch_id = v_switch_id
        # The VPC that corresponds to the SAE namespace. In SAE, a namespace can correspond to only one VPC, and the mapping cannot be modified. The binding relationship is established when the first SAE application is created in the namespace. Multiple namespaces can correspond to the same VPC. If you leave this parameter empty, the VPC bound to the namespace is used by default.
        self.vpc_id = vpc_id
        # The startup command for deploying a WAR package application. The configuration procedure is the same as that for the startup command of an image deployment. For more information, see [Configure a startup command](https://help.aliyun.com/document_detail/96677.html).
        self.war_start_options = war_start_options
        # The version of Tomcat on which the WebContainer deployment package depends. Valid values:
        # 
        # - **apache-tomcat-7.0.91**
        # - **apache-tomcat-8.5.42**
        # 
        # This parameter is not supported when **Package Type** is set to **Image**.
        self.web_container = web_container

    def validate(self):
        if self.init_containers_config:
            for v1 in self.init_containers_config:
                 if v1:
                    v1.validate()
        if self.rasp_config:
            self.rasp_config.validate()
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

        if self.rasp_config is not None:
            result['RaspConfig'] = self.rasp_config.to_map()

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

        if m.get('RaspConfig') is not None:
            temp_model = main_models.CreateApplicationRequestRaspConfig()
            self.rasp_config = temp_model.from_map(m.get('RaspConfig'))

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

class CreateApplicationRequestRaspConfig(DaraModel):
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

