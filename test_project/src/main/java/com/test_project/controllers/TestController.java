
package com.test_project.controllers;
                     
import com.test_project.models.Test;
import com.test_project.repositories.TestRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;
    
@RestController
@RequestMapping("/api")
public class TestController {
    
    @Autowired
    TestRepository testRepository;
    
    
    @GetMapping("/test")
    public List<Test> getAllTest() {
        return testRepository.findAll();
    }
        
    @GetMapping("/test/{id}")
    public Test getTest(@PathVariable(value = "id") Long id){
        Test test = new Test();
        return testRepository.findById(id).orElse(test);
    }
            
    @PostMapping("/test")
    public void setTest() {
        Test test = new Test();
        testRepository.save(test);
    }
    
    @DeleteMapping("/Test")
    public void deleteTest(Long id) {
        testRepository.deleteById(id);
    }
}
    