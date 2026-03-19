package com.example.springbootdemo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;

@SpringBootApplication
public class SpringBootDemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(SpringBootDemoApplication.class, args);
	}

	@RestController
	static class DemoController {

		@GetMapping("/api/hello")
		public Map<String, Object> hello() {
			return Map.of(
					"message", "Hello from Spring Boot demo",
					"status", "ok",
					"version", "v1");
		}
	}
}
