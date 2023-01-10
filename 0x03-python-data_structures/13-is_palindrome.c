#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a
 * palindrome
 * @head: list to be checked
 * Return: 0 if false, 1 if true
 */


int is_palindrome(listint_t **head)
{

if (head == NULL || *head == NULL)
return (1);
return (check_palindrome(head, *head));
}

/**
 * check_palindrome - function to check if the list is palindrome
 * @head: ptr to the beginning of the list
 * @last: ptr to the end of the list
 * Return: 0 if not palindrom else 1
 */
int check_palindrome(listint_t **head, listint_t *last)
{
if (last == NULL)
return (1);
if (check_palindrome(head, last->next) && (*head)->n == last->n)
{
*head = (*head)->next;
return (1);
}
return (0);
}
