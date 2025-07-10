console.log('TypeScript LeetCode Practice Environment Ready!');

// Example function for testing
export function greet(name: string): string {
    return `Hello, ${name}! Welcome to LeetCode practice in TypeScript.`;
}

// Run if this file is executed directly
if (require.main === module) {
    console.log(greet('Developer'));
} 